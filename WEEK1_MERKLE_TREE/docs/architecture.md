# Merkle Tree Architecture & Cryptographic Design

## Overview
A Merkle Tree is a binary cryptographic tree structure where each leaf node represents the SHA-256 hash of an individual data block or audit log. Parent nodes are calculated by concatenating and hashing child hash pairs:

Parent Hash = SHA-256(Left Child Hash + Right Child Hash)

## Key Properties & Guarantees
1. Data Integrity Auditing: The Merkle Root acts as a single, tamper-evident digest representing the state of all underlying logs.
2. Logarithmic Audit Proofs: Inclusion proofs require only O(log N) sibling hashes to verify membership, avoiding the need to process the entire dataset.
3. Odd Node Handling: If an odd number of nodes exists at any tree level, the final node is duplicated to maintain binary balancing.