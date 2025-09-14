from qiskit import QuantumCircuit
from qiskit.circuit.random import random_circuit
from qiskit.quantum_info import Statevector, entropy
from qiskit_aer import AerSimulator

def black_hole_toy_model(num_qubits=3):
    """
    Toy model for black hole information paradox: Simulates scrambling with random unitary.
    Qubits: 0 - infalling matter, 1 - black hole, 2 - radiation.
    Returns:
        circuit: The quantum circuit.
        ent: Entanglement entropy of radiation subsystem.
    """
    circuit = QuantumCircuit(num_qubits)
    # Step 1: Prepare infalling matter (e.g., |1>)
    circuit.x(0)
    circuit.barrier()
    # Step 2: Entangle with black hole (simple model)
    circuit.h(1)
    circuit.cx(0, 1) # Entangle matter with BH
    circuit.barrier()
    # Step 3: Simulate evaporation - create Hawking pair (entangle BH with radiation)
    circuit.cx(1, 2)
    circuit.barrier()
    # Step 4: Scrambling - apply random unitary to 'black hole' system (qubits 1 and 2)
    scrambling_circuit = random_circuit(2, depth=3, measure=False) # Simple random circuit
    circuit = circuit.compose(scrambling_circuit, qubits=[1, 2])
    circuit.barrier()
    # Simulate and compute state
    simulator = AerSimulator(method='statevector')
    circuit.save_statevector()
    result = simulator.run(circuit).result()
    state = result.get_statevector()
    # Compute entanglement entropy of radiation (qubit 2) vs. rest
    # Reduced density matrix for subsystem [2]
    reduced_state = Statevector(state).to_density_matrix().partial_trace([0, 1])
    ent = entropy(reduced_state)
    return circuit, ent
