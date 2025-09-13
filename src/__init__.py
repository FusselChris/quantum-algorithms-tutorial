"""Quantum Algorithms Tutorial Package.

This package contains implementations of fundamental quantum algorithms
including quantum teleportation and Grover's search algorithm.
"""

__version__ = "1.0.0"
__author__ = "FusselChris"
__email__ = "contact@example.com"

# Import main algorithm classes for easy access
from .teleportation import QuantumTeleportation
from .grover import GroverSearch

__all__ = [
    'QuantumTeleportation',
    'GroverSearch',
]
