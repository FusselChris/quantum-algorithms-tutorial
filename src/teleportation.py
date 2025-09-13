"""Quantum Teleportation implementation using Qiskit.

This module provides a function `quantum_teleportation` that builds and runs the
standard 3-qubit quantum teleportation protocol. It returns the result counts and
(optionally) the circuit for inspection/drawing.
"""
from __future__ import annotations

from typing import Dict, Optional, Tuple

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
try:
    # Aer moved under qiskit_aer in recent versions
    from qiskit_aer import Aer
except Exception:  # pragma: no cover - fallback for older installs
    from qiskit import Aer  # type: ignore


def build_teleportation_circuit(alpha: complex = 1.0, beta: complex = 0.0) -> QuantumCircuit:
    """Build the standard 3-qubit quantum teleportation circuit.

    Qubit mapping:
      - q0: Alice's input qubit (|psi> = alpha|0> + beta|1>)
      - q1: Alice's half of the Bell pair
      - q2: Bob's half of the Bell pair (target for teleported state)

    Args:
        alpha: amplitude of |0> for the state to teleport
        beta: amplitude of |1> for the state to teleport

    Returns:
        QuantumCircuit implementing teleportation with classical bits c0,c1 for Alice's measurements.
    """
    qc = QuantumCircuit(3, 2, name="teleportation")

    # Prepare arbitrary input state on q0 with Statevector initialize
    sv = Statevector([alpha, beta]).data
    qc.initialize(sv, 0)

    # Create Bell pair between q1 and q2 (Alice-Bob entanglement)
    qc.h(1)
    qc.cx(1, 2)

    # Bell-state measurement (BSM) on (q0, q1)
    qc.cx(0, 1)
    qc.h(0)

    # Measure Alice's qubits -> classical bits c0 (from q0) and c1 (from q1)
    qc.measure(0, 0)
    qc.measure(1, 1)

    # Conditional corrections on Bob's qubit q2
    qc.x(2).c_if(qc.cregs[0], 0b10)  # if c1 == 1
    qc.z(2).c_if(qc.cregs[0], 0b01)  # if c0 == 1

    return qc


def quantum_teleportation(alpha: complex = 1.0, beta: complex = 0.0, shots: int = 1024,
                          return_circuit: bool = False) -> Tuple[Dict[str, int], Optional[QuantumCircuit]]:
    """Run quantum teleportation for input state alpha|0> + beta|1>.

    Args:
        alpha: amplitude for |0>
        beta: amplitude for |1>
        shots: number of shots to execute on qasm simulator
        return_circuit: when True, also return the built QuantumCircuit

    Returns:
        (counts, circuit?) where counts are measurement results of classical bits c0c1.
        The teleported state ends on qubit q2; to verify, one can append measurements of q2
        in computational basis or perform state tomography in separate routines.
    """
    # Normalize in case the user passed non-normalized amplitudes
    import numpy as np
    norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
    if norm == 0:
        raise ValueError("State amplitudes cannot both be zero")
    alpha_n, beta_n = alpha / norm, beta / norm

    qc = build_teleportation_circuit(alpha_n, beta_n)

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)

    if return_circuit:
        return counts, qc
    return counts, None


__all__ = [
    "build_teleportation_circuit",
    "quantum_teleportation",
]
