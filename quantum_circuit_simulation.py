from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_bell_state():
    # Create a quantum circuit with 2 qubits and 2 classical bits
    circuit = QuantumCircuit(2, 2)

    # Apply Hadamard gate to the first qubit
    circuit.h(0)

    # Apply CNOT gate with control qubit 0 and target qubit 1
    circuit.cx(0, 1)

    # alt, Apply CNOT gate with control qubit 1 and target qubit 0
    # circuit.cx(1, 0)

    # Measure both qubits
    circuit.measure([0, 1], [0, 1])

    return circuit
    
    # Alt Measure both qubits
    # circuit.measure([1, 0], [1, 0])

    # return circuit

def simulate_circuit(circuit, shots=1000):
    # Create an AerSimulator instance
    simulator = AerSimulator()

    # Run the simulation
    job = simulator.run(circuit, shots=shots)

    # Get the results
    result = job.result()

    # Get the counts of measurement outcomes
    counts = result.get_counts(circuit)

    return counts

def plot_results(counts):
    plot_histogram(counts)
    plt.show()

# Main execution
if __name__ == "__main__":
    circuit = create_bell_state()
    print("Quantum Circuit:")
    print(circuit)

    counts = simulate_circuit(circuit)
    print("\nSimulation Results:")
    print(counts)

    plot_results(counts)