"""Black Hole Toy Model — quantum simulation of simplified black hole physics.

Provides:
  - ``black_hole_toy_model``: function demonstrating black hole information
    scrambling and Hawking radiation entanglement entropy.
  - ``BlackHoleToyModel``: class-based API for astrophysics simulations,
    including Hawking radiation entanglement, event horizon effects, and
    gravitational wave amplitude modelling.
"""
from __future__ import annotations

import math
from typing import Tuple

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.random import random_circuit
from qiskit.quantum_info import Statevector, entropy, partial_trace
from qiskit_aer import AerSimulator


def black_hole_toy_model(num_qubits: int = 3) -> Tuple[QuantumCircuit, float]:
    """Toy model for the black hole information paradox.

    Simulates scrambling with a random unitary over three qubits:
      - Qubit 0: infalling matter
      - Qubit 1: black hole interior
      - Qubit 2: Hawking radiation

    Args:
        num_qubits: total number of qubits (default 3).

    Returns:
        Tuple of (circuit, entanglement_entropy) where entanglement_entropy
        is the von Neumann entropy of the radiation subsystem (qubit 2).
    """
    circuit = QuantumCircuit(num_qubits)

    # Prepare infalling matter in |1>
    circuit.x(0)
    circuit.barrier()

    # Entangle matter with black hole interior
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.barrier()

    # Simulate Hawking evaporation: entangle black hole with radiation
    circuit.cx(1, 2)
    circuit.barrier()

    # Scrambling: apply random unitary to black hole + radiation qubits
    scrambling = random_circuit(2, depth=3, measure=False)
    circuit = circuit.compose(scrambling, qubits=[1, 2])
    circuit.barrier()

    # Simulate and extract statevector
    simulator = AerSimulator(method="statevector")
    circuit_copy = circuit.copy()
    circuit_copy.save_statevector()
    result = simulator.run(circuit_copy).result()
    state = Statevector(result.get_statevector())

    # Compute entanglement entropy of radiation (qubit 2) by tracing out qubits 0 and 1
    reduced = partial_trace(state, [0, 1])
    ent = float(entropy(reduced, base=2))

    return circuit, ent


class BlackHoleToyModel:
    """Class-based API for quantum astrophysics simulations.

    Models a simplified black hole with mass and spin parameters, providing
    methods for Hawking radiation entanglement, event horizon quantum effects,
    and gravitational wave amplitude calculations.

    Args:
        mass: Black hole mass in solar masses (M☉). Must be > 0.
        spin: Dimensionless spin parameter a* in [0, 1). 0 = Schwarzschild,
              approaching 1 = maximally rotating Kerr black hole.

    Raises:
        ValueError: if mass <= 0 or spin is outside [0, 1).
    """

    # Schwarzschild radius constant: r_s = 2GM/c^2.
    # In SI units with G=6.674e-11, M_sun=1.989e30, c=3e8:
    #   r_s per solar mass ≈ 2953 metres
    _RS_PER_SOLAR_MASS_METRES = 2.0 * 6.674e-11 * 1.989e30 / (3e8 ** 2)

    def __init__(self, mass: float = 10.0, spin: float = 0.0) -> None:
        if mass <= 0:
            raise ValueError(f"mass must be positive, got {mass}")
        if not (0.0 <= spin < 1.0):
            raise ValueError(f"spin must be in [0, 1), got {spin}")
        self.mass = mass
        self.spin = spin

    # ------------------------------------------------------------------
    # Derived properties
    # ------------------------------------------------------------------

    @property
    def schwarzschild_radius(self) -> float:
        """Schwarzschild radius in metres: r_s = 2GM/c²."""
        return self._RS_PER_SOLAR_MASS_METRES * self.mass

    @property
    def hawking_temperature(self) -> float:
        """Hawking temperature in Kelvin (Schwarzschild approximation).

        T_H = ℏc³ / (8π G M k_B)
        """
        hbar = 1.0546e-34
        c = 3e8
        G = 6.674e-11
        k_B = 1.381e-23
        M_kg = self.mass * 1.989e30
        return (hbar * c ** 3) / (8.0 * math.pi * G * M_kg * k_B)

    # ------------------------------------------------------------------
    # Quantum simulation methods
    # ------------------------------------------------------------------

    def hawking_radiation_entanglement(self, num_qubits: int = 3) -> float:
        """Simulate Hawking radiation entanglement entropy.

        Runs the black hole toy model circuit and returns the von Neumann
        entanglement entropy of the radiation subsystem.

        Args:
            num_qubits: number of qubits in the simulation (default 3).

        Returns:
            Entanglement entropy (bits) of the radiation qubit.
        """
        _, ent = black_hole_toy_model(num_qubits=num_qubits)
        return ent

    def event_horizon_quantum_effects(self) -> dict:
        """Return key quantum parameters at the event horizon.

        Returns a dictionary with:
          - ``schwarzschild_radius_m``: r_s in metres
          - ``hawking_temperature_K``: T_H in Kelvin
          - ``spin``: dimensionless spin parameter
          - ``surface_gravity``: κ = c⁴ / (4GM) for Schwarzschild (m/s²)
        """
        G = 6.674e-11
        c = 3e8
        M_kg = self.mass * 1.989e30
        kappa = c ** 4 / (4.0 * G * M_kg)
        return {
            "schwarzschild_radius_m": self.schwarzschild_radius,
            "hawking_temperature_K": self.hawking_temperature,
            "spin": self.spin,
            "surface_gravity_m_s2": kappa,
        }

    def gravitational_wave_amplitude(
        self, distance: float = 100.0, time: float = 0.0
    ) -> float:
        """Simplified gravitational wave strain amplitude h(t).

        Uses a toy quadrupole formula:
            h ≈ (4G/c⁴) · (M·r_s²·ω²) / d · cos(ω·t)

        where ω = c / r_s (characteristic frequency at the Schwarzschild radius)
        and d is the observer distance in Megaparsecs.

        Args:
            distance: observer distance in Megaparsecs (Mpc). Default 100 Mpc.
            time: observation time in seconds. Default 0.

        Returns:
            Dimensionless strain amplitude h (float).
        """
        G = 6.674e-11
        c = 3e8
        MPC_TO_M = 3.086e22
        M_kg = self.mass * 1.989e30
        r_s = self.schwarzschild_radius
        omega = c / r_s  # characteristic orbital frequency proxy
        d_m = distance * MPC_TO_M
        h = (4.0 * G / c ** 4) * (M_kg * r_s ** 2 * omega ** 2) / d_m
        return h * math.cos(omega * time)


__all__ = [
    "black_hole_toy_model",
    "BlackHoleToyModel",
]
