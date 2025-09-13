# Contributing to Quantum Algorithms Tutorial

We welcome contributions to the Quantum Algorithms Tutorial! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Guidelines](#development-guidelines)
- [Testing Requirements](#testing-requirements)
- [Documentation Standards](#documentation-standards)
- [Pull Request Process](#pull-request-process)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

## Code of Conduct

This project adheres to a code of conduct that promotes a welcoming and inclusive environment for all contributors. By participating, you agree to:

- Be respectful and inclusive in all interactions
- Focus on constructive feedback and collaboration
- Help create a positive learning environment
- Report any unacceptable behavior to project maintainers

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git for version control
- Basic understanding of quantum computing concepts (helpful but not required)
- Familiarity with Qiskit framework

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/quantum-algorithms-tutorial.git
   cd quantum-algorithms-tutorial
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Run tests to verify setup**
   ```bash
   python -m pytest tests/ -v
   ```

## How to Contribute

### Types of Contributions

We appreciate various types of contributions:

- **Code improvements**: Bug fixes, algorithm optimizations, new features
- **Documentation**: README updates, code comments, tutorial enhancements
- **Tests**: Unit tests, integration tests, test coverage improvements
- **Examples**: Additional quantum algorithms, use case demonstrations
- **Educational content**: Explanations, visualizations, learning materials

### Areas for Contribution

- **Algorithm implementations**: Additional quantum algorithms beyond teleportation and Grover's
- **Performance optimizations**: Circuit optimization, execution efficiency
- **Visualization improvements**: Circuit diagrams, result plotting
- **Educational content**: Better explanations, step-by-step tutorials
- **Test coverage**: More comprehensive test suites
- **Documentation**: API docs, usage examples, troubleshooting guides

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Write docstrings for all public functions and classes
- Keep functions focused and modular
- Use type hints where appropriate

### Code Structure

```python
def quantum_function(param: int) -> float:
    """
    Brief description of the function.
    
    Args:
        param: Description of the parameter
        
    Returns:
        Description of return value
        
    Raises:
        SpecificError: When this error occurs
    """
    # Implementation here
    return result
```

### Quantum Circuit Guidelines

- Use clear qubit and classical bit naming
- Add circuit comments for complex operations
- Optimize circuit depth when possible
- Include circuit visualization where helpful
- Document quantum gate choices and reasoning

## Testing Requirements

### Test Coverage

- All new code must include corresponding tests
- Aim for >90% test coverage
- Test both success and failure cases
- Include edge cases and boundary conditions

### Test Types

1. **Unit Tests**: Test individual functions and methods
   ```python
   def test_quantum_teleportation_success():
       teleporter = QuantumTeleportation()
       result = teleporter.teleport_state()
       assert result['success'] is True
   ```

2. **Integration Tests**: Test algorithm workflows
   ```python
   def test_grover_search_integration():
       grover = GroverSearch(n_qubits=3)
       result = grover.search([2, 5])
       assert len(result) == 2
   ```

3. **Property Tests**: Test mathematical properties
   ```python
   def test_quantum_fidelity_bounds():
       # Test that fidelity is always between 0 and 1
       pass
   ```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test file
python -m pytest tests/test_teleportation.py -v
```

## Documentation Standards

### Code Documentation

- Use NumPy-style docstrings
- Document all parameters and return values
- Include usage examples in docstrings
- Explain quantum concepts for educational purposes

### README Updates

- Update installation instructions if dependencies change
- Add new algorithms to the features list
- Update usage examples for new functionality
- Maintain accurate directory structure documentation

### Jupyter Notebooks

- Include clear explanations between code cells
- Add visualizations where helpful
- Test all cells before committing
- Export notebooks with cleared outputs

## Pull Request Process

### Before Submitting

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add appropriate tests
   - Update documentation

3. **Test your changes**
   ```bash
   python -m pytest tests/ -v
   python -m flake8 src/ tests/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add quantum phase estimation algorithm"
   ```

### Commit Message Guidelines

- Use conventional commit format: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`
- Keep first line under 50 characters
- Include detailed description if needed

Example:
```
feat(algorithms): add quantum phase estimation

- Implement QPE for eigenvalue estimation
- Add comprehensive test suite
- Include usage example in notebook
- Update documentation with algorithm explanation
```

### Pull Request Template

When submitting a pull request, include:

**Description**
- What changes were made and why
- Any breaking changes
- Screenshots or diagrams if relevant

**Testing**
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Test coverage maintained or improved

**Documentation**
- [ ] Code is properly documented
- [ ] README updated if necessary
- [ ] Examples updated if necessary

### Review Process

1. Submit pull request with clear description
2. Address any automated check failures
3. Respond to reviewer feedback promptly
4. Make requested changes in additional commits
5. Pull request will be merged after approval

## Bug Reports

### Before Reporting

- Search existing issues to avoid duplicates
- Try to reproduce the bug with minimal example
- Test with the latest version

### Bug Report Template

**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.9.5]
- Qiskit version: [e.g., 0.45.0]
- Repository version/commit: [e.g., main branch, commit abc123]

**Additional Context**
- Error messages
- Screenshots
- Relevant code snippets

## Feature Requests

### Guidelines

- Explain the motivation for the feature
- Describe the expected behavior
- Consider implementation complexity
- Align with project educational goals

### Feature Request Template

**Feature Description**
Clear description of the proposed feature

**Motivation**
Why this feature would be valuable

**Implementation Ideas**
Suggestions for how to implement

**Educational Value**
How this helps users learn quantum computing

**Additional Context**
Any other relevant information

## Recognition

Contributors will be recognized in:

- Repository contributors list
- Acknowledgments section of README
- Release notes for significant contributions
- Conference presentations (with permission)

## Questions?

If you have questions about contributing:

- Open an issue with the "question" label
- Check existing documentation
- Review similar projects for reference

Thank you for contributing to quantum computing education! 🚀
