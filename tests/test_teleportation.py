"""Tests for the quantum teleportation implementation."""
import math
import pytest
from src.teleportation import (
    build_teleportation_circuit,
    quantum_teleportation,
    verify_teleportation_fidelity,
)


def test_build_circuit_structure():
    """Circuit must have 3 qubits and 2 classical bits."""
    qc = build_teleportation_circuit(1.0, 0.0)
    assert qc.num_qubits == 3
    assert qc.num_clbits == 2


def test_teleportation_all_correction_paths_reachable():
    """All four classical outcomes (00, 01, 10, 11) must be reachable.

    Alice's two measurements are uniformly distributed regardless of the
    input state, so all four outcomes should appear in a large shot count.
    """
    counts, _ = quantum_teleportation(
        alpha=1 / math.sqrt(2), beta=1 / math.sqrt(2), shots=4096, return_circuit=True
    )
    observed = set(counts.keys())
    # All four correction branches should be hit with 4096 shots
    assert len(observed) == 4, (
        f"Expected 4 distinct measurement outcomes, got {len(observed)}: {observed}"
    )


def test_teleportation_counts_sum_to_shots():
    """Total measurement count must equal the requested shot count."""
    shots = 512
    counts, _ = quantum_teleportation(1.0, 0.0, shots=shots)
    assert sum(counts.values()) == shots


def test_teleportation_counts_keys_are_two_bit_strings():
    """Result keys must all be 2-bit classical strings."""
    counts, _ = quantum_teleportation(1.0, 0.0, shots=128, return_circuit=True)
    assert all(len(k) == 2 for k in counts.keys())


def test_teleportation_normalization():
    """Non-unit-norm inputs must be accepted and normalized automatically."""
    # alpha=3, beta=4 → norm=5 → should not raise
    counts, _ = quantum_teleportation(alpha=3.0, beta=4.0, shots=128)
    assert sum(counts.values()) == 128


def test_teleportation_returns_circuit_when_requested():
    """Circuit is returned only when return_circuit=True."""
    _, circuit = quantum_teleportation(1.0, 0.0, shots=64, return_circuit=True)
    assert circuit is not None
    assert circuit.num_qubits == 3


def test_invalid_state_raises():
    """Both amplitudes being zero must raise ValueError."""
    with pytest.raises(ValueError):
        quantum_teleportation(0.0, 0.0)

def test_teleportation_fidelity():
    """Bob's qubit should match the original state with near-perfect fidelity."""
    fid = verify_teleportation_fidelity(
        alpha=1 / math.sqrt(2),
        beta=1j / math.sqrt(2),
    )
    assert fid > 0.999, f"Fidelity only {fid:.4f} — teleportation failed"

def test_teleportation_fidelity_rejects_zero_state():
    """The fidelity helper should reject the zero vector."""
    with pytest.raises(ValueError):
        verify_teleportation_fidelity(0.0, 0.0)
