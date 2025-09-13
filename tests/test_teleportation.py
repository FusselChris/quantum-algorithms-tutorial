import pytest

from src.teleportation import build_teleportation_circuit, quantum_teleportation


def test_build_circuit_structure():
    qc = build_teleportation_circuit(1.0, 0.0)
    # 3 qubits, 2 classical bits
    assert qc.num_qubits == 3
    assert qc.num_clbits == 2


def test_teleportation_counts_keys():
    counts, _ = quantum_teleportation(1.0, 0.0, shots=128, return_circuit=True)
    # Keys should be 2-bit classical outcomes from Alice's measurements
    assert all(len(k) == 2 for k in counts.keys())


def test_invalid_state_raises():
    with pytest.raises(ValueError):
        quantum_teleportation(0.0, 0.0)
