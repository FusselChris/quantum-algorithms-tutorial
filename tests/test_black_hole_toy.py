"""Tests for the black hole toy model and BlackHoleToyModel class."""
import math
import pytest
from src.black_hole_toy import black_hole_toy_model, BlackHoleToyModel


# --- black_hole_toy_model function tests ---

def test_entropy_is_positive():
    """Entanglement entropy of a scrambled radiation qubit must be > 0."""
    _, ent = black_hole_toy_model()
    assert ent > 0, f"Expected positive entropy, got {ent}"


def test_entropy_bounded():
    """Von Neumann entropy of a single qubit is at most 1 bit."""
    _, ent = black_hole_toy_model()
    assert ent <= 1.05, f"Entropy {ent} exceeds single-qubit maximum of 1 bit"


def test_returns_circuit_and_float():
    """Function must return (QuantumCircuit, float)."""
    from qiskit import QuantumCircuit
    circuit, ent = black_hole_toy_model()
    assert isinstance(circuit, QuantumCircuit)
    assert isinstance(ent, float)


# --- BlackHoleToyModel class tests ---

def test_schwarzschild_radius_scales_with_mass():
    """A 20 M☉ black hole should have twice the Schwarzschild radius of a 10 M☉ one."""
    bh10 = BlackHoleToyModel(mass=10)
    bh20 = BlackHoleToyModel(mass=20)
    assert math.isclose(bh20.schwarzschild_radius, 2 * bh10.schwarzschild_radius, rel_tol=1e-9)


def test_hawking_temperature_positive():
    """Hawking temperature must be strictly positive."""
    bh = BlackHoleToyModel(mass=10, spin=0.5)
    assert bh.hawking_temperature > 0


def test_hawking_temperature_inverse_mass():
    """Heavier black holes have lower Hawking temperatures."""
    bh_light = BlackHoleToyModel(mass=1)
    bh_heavy = BlackHoleToyModel(mass=100)
    assert bh_light.hawking_temperature > bh_heavy.hawking_temperature


def test_hawking_radiation_entanglement_returns_float():
    """hawking_radiation_entanglement() must return a non-negative float."""
    bh = BlackHoleToyModel(mass=10, spin=0.0)
    ent = bh.hawking_radiation_entanglement()
    assert isinstance(ent, float)
    assert ent >= 0


def test_event_horizon_quantum_effects_keys():
    """event_horizon_quantum_effects() must return all expected keys."""
    bh = BlackHoleToyModel(mass=10, spin=0.3)
    result = bh.event_horizon_quantum_effects()
    expected_keys = {
        "schwarzschild_radius_m",
        "hawking_temperature_K",
        "spin",
        "surface_gravity_m_s2",
    }
    assert expected_keys == set(result.keys())


def test_gravitational_wave_amplitude_is_finite():
    """Gravitational wave amplitude must be a finite float."""
    bh = BlackHoleToyModel(mass=10, spin=0.0)
    h = bh.gravitational_wave_amplitude(distance=100, time=0.1)
    assert math.isfinite(h)


def test_gravitational_wave_amplitude_decreases_with_distance():
    """More distant sources produce weaker strain (ignoring time oscillation at t=0)."""
    bh = BlackHoleToyModel(mass=30, spin=0.0)
    h_near = bh.gravitational_wave_amplitude(distance=10, time=0.0)
    h_far = bh.gravitational_wave_amplitude(distance=1000, time=0.0)
    assert abs(h_near) > abs(h_far)


def test_invalid_mass_raises():
    """Zero or negative mass must raise ValueError."""
    with pytest.raises(ValueError):
        BlackHoleToyModel(mass=0)
    with pytest.raises(ValueError):
        BlackHoleToyModel(mass=-5)


def test_invalid_spin_raises():
    """Spin outside [0, 1) must raise ValueError."""
    with pytest.raises(ValueError):
        BlackHoleToyModel(mass=10, spin=1.0)
    with pytest.raises(ValueError):
        BlackHoleToyModel(mass=10, spin=-0.1)
