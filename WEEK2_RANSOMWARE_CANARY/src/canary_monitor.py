import os
import hashlib
import json
import time

class CanaryTrap:
    def __init__(self, filepath, secret_phrase="HONEYFILE_CANARY_TRAP"):
        self.filepath = filepath
        self.secret_phrase = secret_phrase
        self.baseline_hash = None
        self._generate_honeyfile()

    def _compute_hash(self):
        """Calculates the SHA-256 hash of the canary file."""
        if not os.path.exists(self.filepath):
            return None
        hasher = hashlib.sha256()
        with open(self.filepath, "rb") as f:
            hasher.update(f.read())
        return hasher.hexdigest()

    def _generate_honeyfile(self):
        """Creates an attractive decoy document initialized with cryptographic canary contents."""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        canary_content = f"CONFIDENTIAL FINANCIAL RECORDS - DO NOT ALTER\n[CANARY_MARKER: {self.secret_phrase}]\n"
        with open(self.filepath, "w") as f:
            f.write(canary_content)
        self.baseline_hash = self._compute_hash()

    def inspect(self):
        """Monitors canary status: flags modification (encryption/tampering) or deletion."""
        if not os.path.exists(self.filepath):
            return {
                "status": "ALERT",
                "event": "CANARY_FILE_DELETED",
                "file": self.filepath,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        
        current_hash = self._compute_hash()
        if current_hash != self.baseline_hash:
            return {
                "status": "ALERT",
                "event": "RANSOMWARE_ENCRYPTION_DETECTED",
                "file": self.filepath,
                "baseline_hash": self.baseline_hash,
                "tampered_hash": current_hash,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

        return {
            "status": "OK",
            "event": "NO_TAMPERING",
            "file": self.filepath,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }