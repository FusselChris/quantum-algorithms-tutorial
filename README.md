![CI](https://github.com/FusselChris/quantum-algorithms-tutorial/actions/workflows/ci.yml/badge.svg)

> **⚠️ IMPORTANT SECURITY WARNING ⚠️**
>
> **This repository is for educational use only and is not production-hardened.**
>
> **DO NOT use this code for quantum-cryptographic or security-critical production applications without an independent security audit.**

# Quantum Algorithms Tutorial

A hands-on tutorial repository demonstrating quantum algorithms including Quantum Teleportation, Grover's Search, and quantum simulations for astrophysics using Qiskit — targeted at technical learners new to quantum programming.

## Overview

This repository provides practical implementations of fundamental quantum algorithms with comprehensive explanations and interactive Jupyter notebooks. Perfect for developers, researchers, and students looking to understand quantum computing concepts through hands-on coding, including applications to astrophysical phenomena like black holes and gravitational waves.

## Features

- **Quantum Teleportation**: Complete implementation with circuit visualization
- **Grover's Search Algorithm**: Optimized quantum search with correctness-verified performance analysis
- **Black Hole Toy Model**: Quantum simulation of simplified black hole physics and gravitational wave patterns
- **Interactive Notebooks**: Step-by-step tutorials with explanations
- **Unit Tests**: 26-test suite with 99% code coverage across all modules
- **CI/CD Pipeline**: GitHub Actions workflow running on Python 3.10, 3.11, and 3.12

## Installation

### Prerequisites

- Python 3.10+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/FusselChris/quantum-algorithms-tutorial.git
cd quantum-algorithms-tutorial
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter notebook:
```bash
jupyter notebook notebooks/tutorial.ipynb
```

## Usage

### Quick Start

```python
from src.teleportation import build_teleportation_circuit, quantum_teleportation
from src.grover import grovers_algorithm
from src.black_hole_toy import BlackHoleToyModel

# Quantum Teleportation Example
counts, circuit = quantum_teleportation(alpha=1.0, beta=0.0, shots=1024, return_circuit=True)
print(f"Teleportation measurement outcomes: {counts}")

# Grover's Search Example
counts, _ = grovers_algorithm(n=3, marked="101", shots=1024)
most_probable = max(counts, key=counts.get)
print(f"Grover found: {most_probable}")  # Should print: 101

# Black Hole Toy Model Example
black_hole = BlackHoleToyModel(mass=10, spin=0.5)
entanglement = black_hole.hawking_radiation_entanglement()
print(f"Hawking radiation entanglement entropy: {entanglement:.4f} bits")

gw_amplitude = black_hole.gravitational_wave_amplitude(distance=100, time=0.1)
print(f"Gravitational wave strain amplitude: {gw_amplitude:.3e}")

effects = black_hole.event_horizon_quantum_effects()
print(f"Schwarzschild radius: {effects['schwarzschild_radius_m']:.0f} m")
print(f"Hawking temperature: {effects['hawking_temperature_K']:.2e} K")
```

### Astrophysics Quantum Simulations

The repository includes quantum simulations for astrophysical phenomena:

#### Black Hole Physics
- Hawking radiation entanglement simulation
- Event horizon quantum effects
- Information paradox demonstrations

#### Gravitational Waves
- Gravitational wave strain amplitude modelling
- Distance scaling verification
- Quantum entanglement analysis

### Running the Astrophysics Notebook

```bash
jupyter notebook notebooks/quantum_for_astrophysics.ipynb
```

### Directory Structure

quantum-algorithms-tutorial/
├── src/
│ ├── _init_.py
│ ├── teleportation.py # Quantum teleportation implementation
│ ├── grover.py # Grover's search algorithm
│ └── black_hole_toy.py # Black hole toy model and astrophysics simulations
├── tests/
│ ├── test_teleportation.py # 7 tests — circuit structure, correctness, edge cases
│ ├── test_grover.py # 7 tests — marked state correctness, dominance, validation
│ └── test_black_hole_toy.py # 12 tests — entropy, physics properties, validation
├── .github/
│ └── workflows/
│ └── ci.yml # CI: Python 3.10 / 3.11 / 3.12
├── notebooks/
│ ├── tutorial.ipynb
│ └── quantum_for_astrophysics.ipynb
├── requirements.txt
└── README.md


## Testing

Run the full test suite with coverage:

```bash
python -m pytest tests/ -v --cov=src --cov-report=term-missing
```

Run a specific module's tests:

```bash
python -m pytest tests/test_black_hole_toy.py -v
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## References

- [Qiskit Documentation](https://docs.quantum.ibm.com/)
- [Grover's Algorithm — Nielsen & Chuang, Quantum Computation and Quantum Information](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)
- [Hawking Radiation — S.W. Hawking, "Particle Creation by Black Holes" (1975)](https://link.springer.com/article/10.1007/BF02345020)
- [Black Hole Information Paradox: Quantum computational approaches](https://arxiv.org/abs/2203.05523)

