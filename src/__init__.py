"""Quantum Algorithms Tutorial Package.

This package contains implementations of fundamental quantum algorithms
including quantum teleportation, Grover's search, and a black hole toy model
for astrophysics simulations.
"""

__version__ = "1.1.0"
__author__ = "FusselChris"

# Teleportation
from .teleportation import build_teleportation_circuit, quantum_teleportation

# Grover's Search
from .grover import grovers_algorithm

# Black Hole Toy Model
from .black_hole_toy import black_hole_toy_model, BlackHoleToyModel

__all__ = [
    "build_teleportation_circuit",
    "quantum_teleportation",
    "grovers_algorithm",
    "black_hole_toy_model",
    "BlackHoleToyModel",
]
