# Cryptographic Threat Model & Security Analysis

## 1. Threat Scenarios & Mitigations

### Scenario A: Unauthorized Log Modification
* **Attack**: An adversary modifies an existing log entry inside a historical audit database.
* **Mitigation**: Modifying any leaf node alters its calculated SHA-256 hash, causing a cascading hash mismatch all the way up to the Merkle Root. Verification using `verify_proof()` instantly fails.

### Scenario B: Preimage Attacks
* **Attack**: An attacker attempts to forge a fake log block that yields the exact same leaf hash as a legitimate entry.
* **Mitigation**: SHA-256 provides strong preimage resistance (\(2^{256}\) security level), making collision or preimage generation computationally infeasible.

### Scenario C: Length Extension Attacks
* **Attack**: An adversary attempts to exploit standard cryptographic hashing methods during string concatenation.
* **Mitigation**: Using SHA-256 over fixed binary structures prevents typical length extension vulnerabilities in leaf-and-parent traversal.