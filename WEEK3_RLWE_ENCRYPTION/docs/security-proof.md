# RLWE Post-Quantum Security Proof Summary

## Quantum Hardness Reduction
The security of RLWE relies on the worst-case hardness of high-dimensional lattice problems over ideal lattices:

* **Shortest Vector Problem (SVP)**: Finding the shortest non-zero vector in a lattice.
* **Shortest Independent Vectors Problem (SIVP)**: Finding \(n\) linearly independent short vectors.

Shor's quantum algorithm can break classical RSA/ECC in polynomial time by solving integer factorization and discrete logarithms. However, quantum algorithms provide no known subexponential speedup for worst-case lattice problems like SVP and SIVP, making RLWE a foundational building block for NIST post-quantum standards (e.g., ML-KEM/Kyber).