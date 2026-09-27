# Advanced Cryptography & Defensive Security Portfolio

A high-fidelity, modular Python cybersecurity portfolio comprising integrity verification structures, ransomware early warning systems, and post-quantum lattice-based encryption algorithms.
Repository Structure
.
├── WEEK1_MERKLE_TREE/              # Merkle Tree Integrity Verification
│   ├── src/
│   ├── tests/
│   ├── examples/
│   └── docs/ & results/
├── WEEK2_RANSOMWARE_CANARY/        # Ransomware Early Warning Canary Trap
│   ├── src/
│   ├── tests/
│   ├── examples/
│   └── docs/ & results/
└── WEEK3_RLWE_ENCRYPTION/          # Ring Learning With Errors (RLWE) PQC
├── src/
├── tests/
├── examples/
└── docs/ & results/
Module Breakdown
1. Merkle Tree Integrity Verification (Week 1)
Objective: Implement a cryptographic binary Merkle tree structure using SHA-256 for efficient and tamper-evident data verification.

Key Features: Recursive node hashing, Merkle root computation, and cryptographic proof-of-inclusion generation.

Execution: python -m WEEK1_MERKLE_TREE.examples.demo_merkle

2. Ransomware Early Warning Canary Trap (Week 2)
Objective: Deploy decoy honeyfiles combined with continuous cryptographic hash monitoring to detect unauthorized file tampering and ransomware encryption in real-time.

Key Features: Baseline SHA-256 integrity checks, automated polling, and emergency JSON alert log dispatch upon anomaly detection.

Execution: python -m WEEK2_RANSOMWARE_CANARY.examples.demo_ransomware_defense

3. Ring Learning With Errors (RLWE) Encryption (Week 3)
Objective: Implement a post-quantum public-key encryption scheme operating over the polynomial quotient ring Z_q[x] / (x^n + 1).

Key Features: Discrete Gaussian noise sampling, polynomial multiplication and reduction modulo (x^n + 1), ciphertext generation, and threshold decoding.

Execution: python -m WEEK3_RLWE_ENCRYPTION.examples.demo_rlwe_encryption

Installation & Requirements
Ensure Python 3.8+ and required dependencies are installed:

pip install numpy pytest matplotlib

Running Unit Tests
Execute the complete test suite across all modules:

pytest