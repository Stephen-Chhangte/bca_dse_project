import numpy as np
import json
from WEEK3_RLWE_ENCRYPTION.src.rlwe_cipher import RLWECipher

def run_demo():
    print("=" * 65)
    print(" RING LEARNING WITH ERRORS (RLWE) QUANTUM-RESISTANT ENCRYPTION ")
    print("=" * 65)

    # Initialize RLWE scheme parameters
    n, q, std_dev = 256, 7681, 3.0
    rlwe = RLWECipher(n=n, q=q, std_dev=std_dev)
    print(f"[+] Parameter Setup: Degree n={n}, Prime Modulus q={q}, Error Sigma={std_dev}")

    # 1. Key Generation
    keypair = rlwe.generate_keypair()
    pk_a, pk_b = keypair["public_key"]
    sk = keypair["secret_key"]
    print("[1] Keypair Generated:")
    print(f"    Public Key 'a' Sample: {pk_a[:4]} ...")
    print(f"    Public Key 'b' Sample: {pk_b[:4]} ...")
    print(f"    Secret Key 's' Sample: {sk[:4]} ...\n")

    # 2. Message Preparation (Ascii -> Binary Vector)
    plaintext_msg = "QUANTUM_SAFE"
    bit_array = []
    for char in plaintext_msg:
        bit_array.extend([int(b) for b in format(ord(char), '08b')])
    
    # Pad message bits to match dimension n
    padded_bits = np.zeros(n, dtype=int)
    padded_bits[:len(bit_array)] = bit_array
    print(f"[2] Encoded Binary Payload (First 16 bits): {padded_bits[:16]}\n")

    # 3. Encryption
    ciphertext = rlwe.encrypt(keypair["public_key"], padded_bits)
    u, v = ciphertext
    print("[3] Encryption Executed:")
    print(f"    Ciphertext Component 'u' Sample: {u[:4]} ...")
    print(f"    Ciphertext Component 'v' Sample: {v[:4]} ...\n")

    # 4. Decryption
    decrypted_bits = rlwe.decrypt(keypair["secret_key"], ciphertext)
    print(f"[4] Decrypted Binary Payload (First 16 bits): {decrypted_bits[:16]}")

    # Reconstruct Text
    dec_bits_trimmed = decrypted_bits[:len(bit_array)]
    char_chunks = [dec_bits_trimmed[i:i+8] for i in range(0, len(dec_bits_trimmed), 8)]
    recovered_msg = "".join([chr(int("".join(map(str, chunk)), 2)) for chunk in char_chunks])
    print(f"[+] Recovered Plaintext: '{recovered_msg}'")

    bit_match = np.array_equal(padded_bits, decrypted_bits)
    print(f"[+] Integrity Verification: {'PASSED (100% Match)' if bit_match else 'FAILED'}\n")

    # Save output summary log to results/rlwe_execution_log.json
    log_data = {
        "parameters": {"n": n, "q": q, "std_dev": std_dev},
        "plaintext": plaintext_msg,
        "recovered_text": recovered_msg,
        "status": "SUCCESS" if bit_match else "FAILURE"
    }
    with open("WEEK3_RLWE_ENCRYPTION/results/rlwe_execution_log.json", "w") as f:
        json.dump(log_data, f, indent=2)
    print("[+] Execution Summary Saved to 'results/rlwe_execution_log.json'")
    print("=" * 65)

if __name__ == "__main__":
    run_demo()