from src.grover import grovers_algorithm


def test_grover_counts_have_length_n():
    counts, _ = grovers_algorithm(n=2, marked="11", shots=128, return_circuit=True)
    # Ensure keys are length-2 bitstrings
    assert all(len(k) == 2 for k in counts.keys())


def test_invalid_n_raises():
    import pytest
    with pytest.raises(ValueError):
        grovers_algorithm(n=0)
