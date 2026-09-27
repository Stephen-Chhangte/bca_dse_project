# Merkle Tree Audit System & Cryptographic Verification

A robust Python implementation of a Merkle Tree data integrity audit system built using SHA-256 cryptographic hashing. Designed for cryptographic verification, automated audit logging, and inclusion proof validation.

## Repository Structure

.
├── WEEK1_MERKLE_TREE/
│   ├── src/
│   │   ├── init.py
│   │   └── merkle_tree.py
│   ├── tests/
│   │   └── test_merkle.py
│   ├── examples/
│   │   └── demo_audit.py
│   ├── docs/
│   │   ├── architecture.md
│   │   └── threat-model.md
│   ├── assets/
│   │   └── diagram.md
│   └── results/
│       └── audit_results.md
├── requirements.txt
└── README.md


## Features
- SHA-256 Hashing: Generates cryptographic leaf and internal node digests.
- Logarithmic Proofs: Generates and verifies O(log N) audit proofs.
- Tamper Detection: Instantly flags modified or corrupted log entries.
- Balanced Binary Architecture: Automatically duplicates odd leaf nodes to maintain tree symmetry.

## Quick Start

1. Install dependencies:
   pip install -r requirements.txt

2. Run the audit demonstration:
   python -m WEEK1_MERKLE_TREE.examples.demo_audit

3. Run automated unit tests:
   pytest WEEK1_MERKLE_TREE/tests/

## Cryptographic Security Summary
- Hash Standard: SHA-256 (2^256 security level against collision and preimage attacks)
- Proof Time Complexity: O(log N) verification speed

# Ransomware Early Warning Detection via Cryptographic Honeyfiles and Canary Traps

A high-fidelity early warning system using decoy honeyfiles and cryptographic hash baseline comparisons to detect unauthorized ransomware encryption and file tampering.

## Repository Structure

```text
WEEK2_RANSOMWARE_CANARY/
├── src/
│   ├── __init__.py
│   └── canary_monitor.py
├── tests/
│   └── test_canary.py
├── examples/
│   └── demo_ransomware_defense.py
├── docs/
│   ├── architecture.md
│   └── threat-model.md
├── assets/
│   └── diagram.md
├── results/
│   ├── audit_results.md
│   ├── canary_alert.json
│   └── detection_workflow.png
├── requirements.txt
└── README.md
Quick Start
Run the demonstration:
python -m WEEK2_RANSOMWARE_CANARY.examples.demo_ransomware_defense

Run automated unit tests:
pytest WEEK2_RANSOMWARE_CANARY/tests/