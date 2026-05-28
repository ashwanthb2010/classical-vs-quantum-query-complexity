# classical-vs-quantum-query-complexity

This project explores the difference between classical and quantum query complexity using the Deutsch–Jozsa algorithm.

The paper includes:
- Mathematical derivation of Deutsch and Deutsch–Jozsa algorithms
- Classical vs quantum comparison
- Circuit analysis
- Qiskit implementation
- Noisy simulation analysis

## What is the Deutsch–Jozsa Algorithm?

The Deutsch–Jozsa algorithm is one of the first quantum algorithms to demonstrate a clear computational advantage over classical methods. It determines whether a function is constant or balanced using only a single oracle query.

## Repository Contents

- `Deutsch_Jozsa_Algorithm_with_Qiskit.pdf` — Full research paper
- `deutsch_jozsa_qiskit.py` — Qiskit implementation
- `images/` — Circuit diagrams and histogram outputs

## Tools Used

- Python
- Qiskit
- IBM Quantum Aer Simulator

## Running the Code

Install Qiskit:

```bash
pip install qiskit qiskit-aer
```

Run the Python file:

```bash
python deutsch_jozsa_qiskit.py
```

## References

- David Deutsch and Richard Jozsa, *Rapid solution of problems by quantum computation* (1992)
- Chris Bernhardt, *Quantum Computing for Everyone*
- Qiskit Documentation

## Author

Ashwanth B
