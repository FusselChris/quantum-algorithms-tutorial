# Quantum Algorithms Tutorial

A hands-on tutorial repository demonstrating quantum algorithms like Quantum Teleportation and Grover's Search using Qiskit, targeted at technical learners new to quantum programming.

## Overview

This repository provides practical implementations of fundamental quantum algorithms with comprehensive explanations and interactive Jupyter notebooks. Perfect for developers, researchers, and students looking to understand quantum computing concepts through hands-on coding.

## Features

- **Quantum Teleportation**: Complete implementation with circuit visualization
- **Grover's Search Algorithm**: Optimized quantum search with performance analysis
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

# Quantum Teleportation Example
teleporter = QuantumTeleportation()
result = teleporter.teleport_state()
print(f"Teleportation success: {result}")

# Grover's Search Example
grover = GroverSearch(n_qubits=3)
result = grover.search([2, 5])  # Search for items at indices 2 and 5
print(f"Found items: {result}")
```

### Directory Structure

```
quantum-algorithms-tutorial/
├── src/
│   ├── __init__.py
│   ├── teleportation.py    # Quantum teleportation implementation
│   └── grover.py           # Grover's search algorithm
├── tests/
│   ├── test_teleportation.py
│   └── test_grover.py
├── notebooks/
│   └── tutorial.ipynb      # Interactive tutorial
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Algorithms Implemented

### 1. Quantum Teleportation

Quantum teleportation allows the transfer of quantum information from one location to another using quantum entanglement and classical communication.

**Key Features:**
- Bell state preparation
- Quantum measurements
- Classical communication simulation
- State reconstruction
- Fidelity verification

### 2. Grover's Search Algorithm

Grover's algorithm provides a quadratic speedup for searching unsorted databases.

**Key Features:**
- Oracle construction
- Amplitude amplification
- Optimal iteration calculation
- Multi-target search support
- Success probability analysis

## Testing

Run the test suite:

```bash
python -m pytest tests/ -v
```

For coverage report:

```bash
python -m pytest tests/ --cov=src --cov-report=html
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Code style and standards
- Testing requirements
- Pull request process
- Bug reporting

## Educational Resources

### Prerequisites Knowledge
- Basic linear algebra
- Python programming
- Basic quantum mechanics concepts (helpful but not required)

### Learning Path
1. Start with `notebooks/tutorial.ipynb` for interactive learning
2. Explore source code in `src/` directory
3. Run and modify the examples
4. Check out the test files for additional usage patterns

## Performance Notes

- All algorithms are optimized for educational clarity over performance
- Simulation times increase exponentially with qubit count
- Use IBM Quantum Experience for larger circuits

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- IBM Qiskit team for the excellent quantum computing framework
- Quantum computing research community
- Contributors and educators in quantum algorithm development

## Citation

If you use this tutorial in your research or education, please cite:

```bibtex
@misc{quantum_algorithms_tutorial,
  author = {FusselChris},
  title = {Quantum Algorithms Tutorial: Hands-on Qiskit Implementation},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/FusselChris/quantum-algorithms-tutorial}
}
```

## Support

For questions, suggestions, or issues:

- Open an issue on GitHub
- Check existing documentation
- Review the tutorial notebook for examples

Happy quantum computing! 🚀
