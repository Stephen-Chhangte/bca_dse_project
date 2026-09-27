from WEEK1_MERKLE_TREE.src.merkle_tree import MerkleTree

def run_demo():
    logs = [
        "2026-09-27 10:00:00 - User Alice Login",
        "2026-09-27 10:05:12 - Transaction #10492 ($500.00)",
        "2026-09-27 10:12:44 - User Bob Password Change",
        "2026-09-27 10:15:30 - Admin System Configuration Export"
    ]

    print("==================================================")
    print(" MERKLE TREE DATA INTEGRITY AUDIT DEMO")
    print("==================================================")
    
    tree = MerkleTree(logs)
    root = tree.get_root()
    print(f"Total Audit Logs Processed: {len(logs)}")
    print(f"Calculated Merkle Root Hash:\n  --> {root}\n")

    target_idx = 1
    target_log = logs[target_idx]
    proof = tree.get_proof(target_idx)

    print(f"Auditing Entry: '{target_log}'")
    is_valid = tree.verify_proof(target_log, proof, root)
    print(f"Verification Result: {'PASSED (Integrity Confirmed)' if is_valid else 'FAILED'}\n")

    tampered_log = target_log + " [MODIFIED]"
    print(f"Auditing Tampered Entry: '{tampered_log}'")
    is_valid_tampered = tree.verify_proof(tampered_log, proof, root)
    print(f"Verification Result: {'PASSED' if is_valid_tampered else 'TAMPERING DETECTED (Mismatch)'}")
    print("==================================================")

if __name__ == "__main__":
    run_demo()