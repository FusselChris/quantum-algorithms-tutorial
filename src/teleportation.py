"""Quantum Teleportation implementation using Qiskit.

This module provides a function `quantum_teleportation` that builds and runs the
standard 3-qubit quantum teleportation protocol. It returns the result counts and
(optionally) the circuit for inspection/drawing.

Protocol summary:
  1. Prepare arbitrary input state |psi> = alpha|0> + beta|1> on qubit q0.
  2. Create Bell pair between q1 (Alice) and q2 (Bob).
  3. Alice performs Bell-state measurement on (q0, q1), collapsing to 2 classical bits.
  4. Bob applies conditional X and Z corrections on q2 based on Alice's bits.
  5. Bob's qubit q2 now holds the original state |psi>.
"""
from __future__ import annotations

from typing import Dict, Optional, Tuple

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.quantum_info import Statevector, partial_trace, state_fidelity
try:
    from qiskit_aer import Aer
except Exception:  # pragma: no cover
    from qiskit import Aer  # type: ignore


def build_teleportation_circuit(alpha: complex = 1.0, beta: complex = 0.0) -> QuantumCircuit:
    """Build the standard 3-qubit quantum teleportation circuit.

    Qubit mapping:
      - q[0]: Alice's input qubit (|psi> = alpha|0> + beta|1>)
      - q[1]: Alice's half of the Bell pair
      - q[2]: Bob's half of the Bell pair (receives teleported state)

    Classical bit mapping:
      - c[0]: Alice's measurement of q[0] — controls Bob's Z correction
      - c[1]: Alice's measurement of q[1] — controls Bob's X correction

    Args:
        alpha: amplitude of |0> for the state to teleport.
        beta:  amplitude of |1> for the state to teleport.

    Returns:
        QuantumCircuit implementing the full teleportation protocol.
    """
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(q, c, name="teleportation")

    # --- Step 1: Prepare input state on q[0] ---
    sv = Statevector([alpha, beta]).data
    qc.initialize(sv, q[0])
    qc.barrier(label="init")

    # --- Step 2: Create Bell pair between q[1] and q[2] ---
    qc.h(q[1])
    qc.cx(q[1], q[2])
    qc.barrier(label="bell_pair")

    # --- Step 3: Bell-state measurement on (q[0], q[1]) ---
    qc.cx(q[0], q[1])
    qc.h(q[0])
    qc.barrier(label="bsm")

    # Measure Alice's qubits into classical register
    qc.measure(q[0], c[0])   # c[0] <- q[0] measurement
    qc.measure(q[1], c[1])   # c[1] <- q[1] measurement
    qc.barrier(label="measure")

    # --- Step 4: Bob's conditional corrections on q[2] ---
    # If c[1] == 1 (q[1] was |1>), apply X gate
    # If c[0] == 1 (q[0] was |1>), apply Z gate
    with qc.if_test((c[1], 1)):
        qc.x(q[2])
    with qc.if_test((c[0], 1)):
        qc.z(q[2])

    return qc


def quantum_teleportation(
    alpha: complex = 1.0,
    beta: complex = 0.0,
    shots: int = 1024,
    return_circuit: bool = False,
) -> Tuple[Dict[str, int], Optional[QuantumCircuit]]:
    """Run quantum teleportation for input state alpha|0> + beta|1>.

    Normalizes the input amplitudes automatically if they are not already
    unit-norm. Uses the Aer qasm_simulator backend.

    Args:
        alpha: amplitude for |0>.
        beta:  amplitude for |1>.
        shots: number of shots to execute on the simulator.
        return_circuit: when True, also return the built QuantumCircuit.

    Returns:
        Tuple of (counts, circuit_or_None). counts maps classical bit
        strings (c0 c1) to observed frequencies. circuit is the full
        QuantumCircuit when return_circuit=True, else None.

    Raises:
        ValueError: if both amplitudes are zero (un-normalizable state).
    """
    norm = np.sqrt(abs(alpha) ** 2 + abs(beta) ** 2)
    if norm == 0:
        raise ValueError("State amplitudes cannot both be zero.")
    alpha_n, beta_n = alpha / norm, beta / norm

    qc = build_teleportation_circuit(alpha_n, beta_n)

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)

    if return_circuit:
        return counts, qc
    return counts, None


def verify_teleportation_fidelity(
    alpha: complex = 1.0,
    beta: complex = 0.0,
) -> float:
    """Verify teleportation fidelity with a measurement-free reference circuit.

    Builds a coherent version of the teleportation protocol and compares
    Bob's final qubit to the intended input state without collapsing the
    state by measurement.

    Args:
        alpha: amplitude for |0>.
        beta:  amplitude for |1>.

    Returns:
        Fidelity in [0, 1]. A value > 0.999 confirms correct teleportation.

    Raises:
        ValueError: if both amplitudes are zero.
    """
    norm = np.sqrt(abs(alpha) ** 2 + abs(beta) ** 2)
    if norm == 0:
        raise ValueError("State amplitudes cannot both be zero.")

    alpha_n, beta_n = alpha / norm, beta / norm

    qc = QuantumCircuit(3, name="teleportation_fidelity")
    qc.initialize([alpha_n, beta_n], 0)

    # Standard teleportation preparation.
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)

    # Coherent correction stage (no measurement collapse).
    qc.cx(1, 2)
    qc.cz(0, 2)

    final_state = Statevector.from_instruction(qc)
    bob_state = partial_trace(final_state, [0, 1])
    target_state = Statevector([alpha_n, beta_n])

    return float(state_fidelity(bob_state, target_state))


__all__ = [
    "build_teleportation_circuit",
    "quantum_teleportation",
    "verify_teleportation_fidelity",
]
