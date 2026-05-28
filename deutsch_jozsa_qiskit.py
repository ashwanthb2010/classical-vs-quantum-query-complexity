from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit_aer.noise import NoiseModel
from qiskit.providers.fake_provider import GenericBackendV2
import matplotlib.pyplot as plt

qc = QuantumCircuit(3, 2)

# Output qubit
qc.x(2)
qc.h(2)

# Superposition
qc.h(0)
qc.h(1)

#  Balanced oracle
qc.cx(0, 2)
qc.cx(1, 2)

# Interference
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
    shots=1024
)

result = job.result()
counts = result.get_counts()

# Determine result
dominant_state = max(counts, key=counts.get)

if dominant_state == '00':
    print("Constant")
else:
    print("Balanced")

print(counts)
plot_histogram(counts)
plt.show()
