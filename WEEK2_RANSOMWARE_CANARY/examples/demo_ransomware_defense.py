import time
import json
from WEEK2_RANSOMWARE_CANARY.src.canary_monitor import CanaryTrap

def run_demo():
    print("=" * 60)
    print(" RANSOMWARE EARLY WARNING CANARY DETECTION DEMO ")
    print("=" * 60)

    honeyfile = "WEEK2_RANSOMWARE_CANARY/results/passwords_decoy.xlsx"
    trap = CanaryTrap(honeyfile)
    print(f"[+] Initialized Honeyfile: {honeyfile}")
    print(f"[+] Baseline SHA-256 Digest: {trap.baseline_hash}\n")

    # Step 1: Normal System State
    print("[1] Performing Routine System Inspection...")
    status = trap.inspect()
    print(f"    Status: {status['status']} | Event: {status['event']}\n")

    # Step 2: Simulated Ransomware Attack
    print("[2] Simulating Ransomware Attack (Encrypting Honeyfile)...")
    time.sleep(1)
    with open(honeyfile, "wb") as f:
        f.write(b"\x00\x01\x02\x03[ENCRYPTED_BY_RANSOMWARE_SIMULATOR]\x99\xFF")

    # Step 3: Early Warning Detection Trigger
    print("[3] Performing Post-Incident Inspection...")
    status = trap.inspect()
    print(f"    Status: {status['status']} | Event: {status['event']}")
    print(f"    Alert Triggered At: {status['timestamp']}")
    print(f"    New Tampered Hash:  {status['tampered_hash']}\n")

    # Save output log to results/canary_alert.json
    with open("WEEK2_RANSOMWARE_CANARY/results/canary_alert.json", "w") as f:
        json.dump(status, f, indent=2)
    print("[+] Emergency Alert Log Exported to 'results/canary_alert.json'")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()