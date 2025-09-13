"""Grover's algorithm implementation using Qiskit.

Function `grovers_algorithm` constructs and runs Grover for a single-solution
oracle over n qubits. For flexibility, you can pass a custom oracle circuit.
"""
from __future__ import annotations

from typing import Optional, Tuple, Dict

from qiskit import QuantumCircuit
try:
    from qiskit_aer import Aer
except Exception:  # pragma: no cover
    from qiskit import Aer  # type: ignore


def _diffusion_operator(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n, name="diffusion")
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    return qc


def _mark_oracle_for_bitstring(n: int, marked: str) -> QuantumCircuit:
    if len(marked) != n or any(c not in "01" for c in marked):
        raise ValueError("marked must be an n-bit string of 0/1")
    qc = QuantumCircuit(n, name="oracle")
    # Flip qubits that are 0 in the marked string so that |marked> -> |11..1>
    for i, bit in enumerate(marked):
        if bit == '0':
            qc.x(i)
    # Phase flip on |11..1>
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    # Undo the flips
    for i, bit in enumerate(marked):
        if bit == '0':
            qc.x(i)
    return qc


def grovers_algorithm(n: int, marked: str = "1" , shots: int = 1024,
                      custom_oracle: Optional[QuantumCircuit] = None,
                      return_circuit: bool = False) -> Tuple[Dict[str, int], Optional[QuantumCircuit]]:
    """Run Grover's algorithm on n qubits to find a marked state.

    Args:
        n: number of search qubits
        marked: n-bit string of the marked item. Ignored if custom_oracle provided.
        shots: number of shots on simulator
        custom_oracle: optional custom phase oracle QuantumCircuit on n qubits
        return_circuit: also return full circuit when True
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    oracle = custom_oracle if custom_oracle is not None else _mark_oracle_for_bitstring(n, marked.zfill(n))
    diffusion = _diffusion_operator(n)

    qc = QuantumCircuit(n, n, name="grover")
    # Initialize uniform superposition
    qc.h(range(n))

    # Number of Grover iterations ~ floor(pi/4 * sqrt(N))
    import math
    iterations = max(1, int(math.floor((math.pi/4) * (2**(n/2)))))

    for _ in range(iterations):
        qc.compose(oracle, range(n), inplace=True)
        qc.compose(diffusion, range(n), inplace=True)

    qc.measure(range(n), range(n))

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)

    if return_circuit:
        return counts, qc
    return counts, None


__all__ = [
    "grovers_algorithm",
]
