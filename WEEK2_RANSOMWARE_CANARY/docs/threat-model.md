# Threat Model: Canary Decoy Defense

## Threat Vector Analysis

### Scenario A: Bulk Automated Encryption (Ransomware)
* **Threat**: Malicious payloads search file systems for common extensions (`.xlsx`, `.docx`, `.pdf`) and encrypt sequentially.
* **Mitigation**: Canary traps use enticing filenames (`passwords_decoy.xlsx`). Encrypting a canary immediately alerts security orchestrators to kill parent processes.

### Scenario B: Data Destruction / Deletion
* **Threat**: Attackers attempt to scrub honeyfiles to avoid detection or obscure tracks.
* **Mitigation**: `CanaryTrap.inspect()` checks file existence; missing targets immediately trigger `CANARY_FILE_DELETED` critical alerts.