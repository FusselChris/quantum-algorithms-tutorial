![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![Qiskit 1.2](https://img.shields.io/badge/Qiskit-1.2-orange)
![Tests](https://img.shields.io/badge/Tests-28%20passing-brightgreen)
[![CI](https://github.com/FusselChris/quantum-algorithms-tutorial/actions/workflows/ci.yml/badge.svg)](https://github.com/FusselChris/quantum-algorithms-tutorial/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Quantum Algorithms Tutorial

**A clean, well-tested, production-style educational package** demonstrating core quantum algorithms (Teleportation + Grover’s Search) with a creative astrophysics toy model — built to showcase strong software engineering + quantum computing skills.

> **Educational project only**  
> This repository is for learning and demonstration. The code is intentionally simplified and not intended for production cryptographic or security-critical use.

## Overview

This repository provides practical implementations of fundamental quantum algorithms with comprehensive explanations and interactive Jupyter notebooks. Perfect for developers, researchers, and students looking to understand quantum computing concepts through hands-on coding, including applications to astrophysical phenomena like black holes and gravitational waves.

## Built for learning & demonstration
I created this repo to bridge classical programming skills with quantum computing. It includes a 28-test suite, full CI/CD, and a creative black-hole toy model that connects quantum information theory to astrophysics — exactly the kind of interdisciplinary thinking valued in physics, CS, and quantum engineering programs.

## Features

- **Quantum Teleportation**: Complete implementation with circuit visualization
![Teleportation circuit](https://raw.githubusercontent.com/FusselChris/quantum-algorithms-tutorial/main/images/teleportation_circuit.png)
- **Grover's Search Algorithm**: Optimized quantum search with correctness-verified performance analysis
![Grover circuit](https://raw.githubusercontent.com/FusselChris/quantum-algorithms-tutorial/main/images/grover_circuit.png)
- **Black Hole Toy Model**: A reproducible educational model for scrambling, entanglement entropy, and horizon-scale quantities. Deliberately a toy model, not a full semiclassical gravity solver.
![Black Hole circuit](https://raw.githubusercontent.com/FusselChris/quantum-algorithms-tutorial/main/images/black_hole_circuit.png)
- **Interactive Notebooks**: Step-by-step tutorials with explanations
- **Unit Tests**: 28-test suite covering circuit structure, correctness, fidelity, and edge cases
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
**Interactive Notebooks:** * [Open tutorial.ipynb in nbviewer](https://nbviewer.org/github/FusselChris/quantum-algorithms-tutorial/blob/main/notebooks/tutorial.ipynb)
* [Open quantum_for_astrophysics.ipynb in nbviewer](https://nbviewer.org/github/FusselChris/quantum-algorithms-tutorial/blob/main/notebooks/quantum_for_astrophysics.ipynb)

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

The repository includes educational quantum-inspired models for astrophysical ideas.

#### Black Hole Physics
- Toy-model scrambling and Hawking-radiation entanglement
- Event-horizon-scale quantities such as Schwarzschild radius and Hawking temperature
- Information-paradox style demonstrations

#### Gravitational Waves
- Simplified strain-amplitude scaling with distance
- Time-dependent oscillatory behaviour
- Quantum-entanglement themed pedagogical analogies

### Physics Note

These simulations are intentionally simplified. They are meant to teach qualitative relationships and coding patterns, not to replace real numerical relativity or semiclassical gravity calculations.

### Running the Astrophysics Notebook

```bash
jupyter notebook notebooks/quantum_for_astrophysics.ipynb
```

## Directory Structure

```text
quantum-algorithms-tutorial/
├── src/
│   ├── __init__.py          # Marks src as a Python package
│   ├── teleportation.py     # Quantum teleportation implementation
│   ├── grover.py            # Grover's search algorithm
│   └── black_hole_toy.py    # Black hole toy model and astrophysics simulations
├── tests/
│   ├── test_teleportation.py  # 9 tests — circuit structure, correctness, fidelity
│   ├── test_grover.py         # 7 tests — marked state correctness, dominance, validation
│   └── test_black_hole_toy.py # 16 tests — entropy, physics properties, validation
├── .github/
│   └── workflows/
│       └── ci.yml             # CI: Python 3.10 / 3.11 / 3.12
├── notebooks/
│   ├── tutorial.ipynb
│   └── quantum_for_astrophysics.ipynb
├── requirements.txt
└── README.md
```

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

