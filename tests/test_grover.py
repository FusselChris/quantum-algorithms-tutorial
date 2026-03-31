"""Tests for Grover's search algorithm implementation."""
import pytest
from src.grover import grovers_algorithm


def test_grover_finds_marked_state_2_qubits():
    """The marked state must be the most frequently measured outcome."""
    marked = "11"
    counts, _ = grovers_algorithm(n=2, marked=marked, shots=1024)
    most_probable = max(counts, key=counts.get)
    assert most_probable == marked, (
        f"Expected '{marked}' to be most probable, got '{most_probable}'. Counts: {counts}"
    )


def test_grover_finds_marked_state_3_qubits():
    """Grover works correctly across different problem sizes."""
    marked = "101"
    counts, _ = grovers_algorithm(n=3, marked=marked, shots=1024)
    most_probable = max(counts, key=counts.get)
    assert most_probable == marked, (
        f"Expected '{marked}' to be most probable, got '{most_probable}'. Counts: {counts}"
    )

def test_grover_marked_state_dominates():
    """Marked state should be the most probable measurement outcome."""
    marked = "11"
    counts, _ = grovers_algorithm(n=2, marked=marked, shots=2048)
    total = sum(counts.values())
    most_probable = max(counts, key=counts.get)
    dominant_fraction = counts[most_probable] / total
    assert most_probable == marked, (
        f"Expected '{marked}' to dominate, but '{most_probable}' did. Counts: {counts}"
    )
    assert dominant_fraction > 0.5, (
        f"Expected >50% probability on '{marked}', got {dominant_fraction:.2%}"
    )

def test_grover_counts_have_length_n():
    """All result keys must be bitstrings of length n."""
    counts, _ = grovers_algorithm(n=2, marked="11", shots=128, return_circuit=True)
    assert all(len(k) == 2 for k in counts.keys())


def test_grover_returns_circuit_when_requested():
    """Circuit is returned only when return_circuit=True."""
    counts, circuit = grovers_algorithm(n=2, marked="01", shots=128, return_circuit=True)
    assert circuit is not None
    assert circuit.num_qubits == 2


def test_invalid_n_raises():
    """n=0 must raise a ValueError."""
    with pytest.raises(ValueError):
        grovers_algorithm(n=0)


def test_invalid_marked_raises():
    """A marked string of wrong length must raise a ValueError."""
    with pytest.raises(ValueError):
        grovers_algorithm(n=3, marked="11")  # length 2 ≠ n=3
