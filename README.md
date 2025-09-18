> **⚠️ IMPORTANT SECURITY WARNING ⚠️**
>
> **This repository is for educational use only and is not production-hardened.**
>
> **The code may lack comprehensive security and reliability checks.**
>
> **DO NOT use this repository or its code for quantum-cryptographic or security-critical production applications without an independent security audit.**

# Quantum Algorithms Tutorial
A hands-on tutorial repository demonstrating quantum algorithms like Quantum Teleportation, Grover's Search, and quantum simulations for astrophysics using Qiskit, targeted at technical learners new to quantum programming.
## Overview
This repository provides practical implementations of fundamental quantum algorithms with comprehensive explanations and interactive Jupyter notebooks. Perfect for developers, researchers, and students looking to understand quantum computing concepts through hands-on coding, including applications to astrophysical phenomena like black holes and gravitational waves.
## Features
- **Quantum Teleportation**: Complete implementation with circuit visualization
- **Grover's Search Algorithm**: Optimized quantum search with performance analysis
- **Black Hole Toy Model**: Quantum simulation of simplified black hole physics and gravitational wave patterns
- **Interactive Notebooks**: Step-by-step tutorials with explanations
- **Unit Tests**: Comprehensive test suite for all implementations
- **Documentation**: Detailed API documentation and usage examples

## Installation

### Prerequisites
- Python 3.8+
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
from src.teleportation import QuantumTeleportation
from src.grover import GroverSearch
from src.black_hole_toy import BlackHoleToyModel

# Quantum Teleportation Example
teleporter = QuantumTeleportation()
result = teleporter.teleport_state()
print(f"Teleportation success: {result}")

# Grover's Search Example
grover = GroverSearch(n_qubits=3)
result = grover.search([2, 5])  # Search for items at indices 2 and 5
print(f"Found items: {result}")

# Black Hole Toy Model Example
black_hole = BlackHoleToyModel(mass=10, spin=0.5)
entanglement = black_hole.hawking_radiation_entanglement()
print(f"Hawking radiation entanglement: {entanglement}")

# Gravitational wave simulation
gw_amplitude = black_hole.gravitational_wave_amplitude(distance=100, time=0.1)
print(f"Gravitational wave amplitude: {gw_amplitude}")
```

### Astrophysics Quantum Simulations

The repository now includes quantum simulations for astrophysical phenomena:

#### Black Hole Physics
- Hawking radiation entanglement simulation
- Event horizon quantum effects
- Information paradox demonstrations

#### Gravitational Waves
- Quantum-enhanced detection algorithms
- Wave amplitude calculations
- Interferometer sensitivity modeling

### Running the Astrophysics Notebook

```bash
jupyter notebook notebooks/quantum_for_astrophysics.ipynb
```

This notebook includes:
- Interactive black hole parameter exploration
- Gravitational wave visualization
- Quantum entanglement analysis
- Performance comparisons with classical methods

### Directory Structure

```
quantum-algorithms-tutorial/
├── src/
│   ├── teleportation.py      # Quantum teleportation implementation
│   ├── grover.py             # Grover's search algorithm
│   └── black_hole_toy.py     # Black hole toy model and astrophysics simulations
├── tests/
│   ├── test_teleportation.py
│   ├── test_grover.py
│   └── test_black_hole_toy.py # Tests for astrophysics simulations
├── notebooks/
│   ├── tutorial.ipynb        # Main quantum algorithms tutorial
│   └── quantum_for_astrophysics.ipynb  # Astrophysics applications
├── requirements.txt
└── README.md
```

## Requirements for Astrophysics Simulations

Additional dependencies for the black hole toy model:

```bash
pip install numpy scipy matplotlib qiskit[visualization] jupyter
```

For advanced visualizations:

```bash
pip install plotly seaborn
```

## Testing

Run all tests including the new astrophysics simulations:

```bash
python -m pytest tests/
```

Run specific astrophysics tests:

```bash
python -m pytest tests/test_black_hole_toy.py -v
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## References

- Qiskit Documentation: https://qiskit.org/documentation/
- Quantum Computing for Astrophysics: Recent advances in quantum simulation applications
- Black Hole Information Paradox: Quantum computational approaches
