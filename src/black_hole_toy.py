"""Educational black hole toy model for quantum computing tutorials.

This module intentionally models qualitative relationships only. It is useful
for teaching scrambling, entanglement entropy, horizon-scale quantities, and
simple scaling laws. It is not a semiclassical gravity solver.
"""
from __future__ import annotations

import math
from typing import Dict, Tuple

from qiskit import QuantumCircuit
from qiskit.circuit.random import random_circuit
from qiskit.quantum_info import Statevector, entropy, partial_trace

# Physical constants in SI units.
G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054_571_817e-34
K_B = 1.380_649e-23
M_SUN = 1.988_47e30
MPC_TO_M = 3.085_677_581_491_367e22

# Schwarzschild radius per solar mass, in metres.
RS_PER_SOLAR_MASS_METRES = 2.0 * G * M_SUN / C**2


def _require_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")


def black_hole_toy_model(
    num_qubits: int = 3,
    scrambling_seed: int = 42,
) -> Tuple[QuantumCircuit, float]:
    """Toy model for black hole information scrambling.

    The first three qubits are used as:
      - q0: infalling matter
      - q1: black hole interior
      - q2: Hawking radiation

    Any extra qubits are left idle, which keeps the API flexible while
    preserving the original 3-qubit educational model.

    Args:
        num_qubits: total qubits in the circuit, must be at least 3.
        scrambling_seed: deterministic seed for the scrambling circuit.

    Returns:
        (circuit, entanglement_entropy_bits)
    """
    if num_qubits < 3:
        raise ValueError(f"num_qubits must be at least 3, got {num_qubits}")

    circuit = QuantumCircuit(num_qubits, name="black_hole_toy")

    # Prepare infalling matter in |1>.
    circuit.x(0)
    circuit.barrier()

    # Entangle matter with the black hole interior.
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.barrier()

    # Simulate Hawking evaporation by entangling the interior with radiation.
    circuit.cx(1, 2)
    circuit.barrier()

    # Deterministic scrambling on the interior and radiation subsystem.
    scrambling = random_circuit(2, depth=3, measure=False, seed=scrambling_seed)
    circuit = circuit.compose(scrambling, qubits=[1, 2])
    circuit.barrier()

    # Compute the radiation entropy from the final pure state.
    state = Statevector.from_instruction(circuit)
    radiation_reduced = partial_trace(state, [0, 1])
    entanglement_entropy = float(entropy(radiation_reduced, base=2))

    return circuit, entanglement_entropy


class BlackHoleToyModel:
    """Educational black hole model with simple horizon-scale calculations.

    This is a teaching tool, not a physically complete astrophysical model.
    """

    _RS_PER_SOLAR_MASS_METRES = RS_PER_SOLAR_MASS_METRES

    def __init__(self, mass: float = 10.0, spin: float = 0.0) -> None:
        if mass <= 0:
            raise ValueError(f"mass must be positive, got {mass}")
        if not (0.0 <= spin < 1.0):
            raise ValueError(f"spin must be in [0, 1), got {spin}")
        self.mass = mass
        self.spin = spin

    @property
    def schwarzschild_radius(self) -> float:
        """Schwarzschild radius in metres: r_s = 2GM/c²."""
        return self._RS_PER_SOLAR_MASS_METRES * self.mass

    @property
    def hawking_temperature(self) -> float:
        """Hawking temperature in Kelvin, Schwarzschild approximation."""
        mass_kg = self.mass * M_SUN
        return (HBAR * C**3) / (8.0 * math.pi * G * mass_kg * K_B)

    def hawking_radiation_entanglement(
        self,
        num_qubits: int = 3,
        scrambling_seed: int = 42,
    ) -> float:
        """Return the toy-model entanglement entropy of the radiation qubit."""
        _, ent = black_hole_toy_model(
            num_qubits=num_qubits,
            scrambling_seed=scrambling_seed,
        )
        return ent

    def event_horizon_quantum_effects(self) -> Dict[str, float]:
        """Return a compact summary of toy horizon-scale quantities."""
        mass_kg = self.mass * M_SUN
        surface_gravity = C**4 / (4.0 * G * mass_kg)

        return {
            "mass_solar_masses": self.mass,
            "spin": self.spin,
            "schwarzschild_radius_m": self.schwarzschild_radius,
            "hawking_temperature_K": self.hawking_temperature,
            "surface_gravity_m_s2": surface_gravity,
        }

    def gravitational_wave_amplitude(
        self,
        distance: float = 100.0,
        time: float = 0.0,
    ) -> float:
        """Simplified gravitational-wave strain amplitude.

        This is a pedagogical toy estimate, not a full gravitational-wave model.
        It captures the two key tutorial ideas:
          - strain decreases with distance
          - the signal oscillates in time

        Args:
            distance: observer distance in megaparsecs, must be positive.
            time: observation time in seconds.

        Returns:
            Dimensionless strain amplitude.
        """
        _require_positive(distance, "distance")

        r_s = self.schwarzschild_radius
        d_m = distance * MPC_TO_M
        omega = C / r_s

        # Toy scaling that preserves the correct distance dependence.
        h0 = 2.0 * r_s / d_m
        return h0 * math.cos(omega * time)


__all__ = [
    "black_hole_toy_model",
    "BlackHoleToyModel",
]
