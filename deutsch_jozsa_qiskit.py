from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit_aer.noise import NoiseModel
from qiskit.providers.fake_provider import GenericBackendV2
import matplotlib.pyplot as plt

# The code applies the Deutsch-josza algorithm with n=2.

# Create a quantum circuit
# 3 qubits total:
# - qubit 0 and 1 are input qubits
# - qubit 2 is the output qubit
# 2 classical bits are used for measurement
qc = QuantumCircuit(3, 2)

# An X gate is applied followed by a hadamard gate to put it in the state |−⟩ .
qc.x(2)
qc.h(2)

# A hadamard gate is applied to the two input qubits.
qc.h(0)
qc.h(1)

# The oracle is applied. Here a balanced oracle is applied- the CNOT gate.  
qc.cx(0, 2)
qc.cx(1, 2)

# Hadamard gate is applied again after oracle. This creates interference.
qc.h(0)
qc.h(1)

# Measurement
qc.measure(0, 0)
qc.measure(1, 1)

# Simulator
simulator = Aer.get_backend('aer_simulator')

# Noise model
fake_backend = GenericBackendV2(num_qubits=5)
noise_model = NoiseModel.from_backend(fake_backend)

# Run noisy simulation
job = simulator.run(
    qc,
    noise_model=noise_model,
    
    # The number of shots is the number of times the code is implemented or iterated. The more the shots the better dominant result we get.
    shots=1024
)

result = job.result()
counts = result.get_counts()

# Determine result
dominant_state = max(counts, key=counts.get)

# Print the ouput of whether the function is constant or balanced
if dominant_state == '00':
    print("Constant")
else:
    print("Balanced")

# Print the counts of each qubit
print(counts)

# Plot a histogram to see the count of each qubit and visualize the noise.
plot_histogram(counts)

# Display the histogram
plt.show()
