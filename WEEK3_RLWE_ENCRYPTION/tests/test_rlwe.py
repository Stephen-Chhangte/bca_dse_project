import numpy as np
import pytest
from WEEK3_RLWE_ENCRYPTION.src.rlwe_cipher import RLWECipher

@pytest.fixture
def rlwe():
    return RLWECipher(n=128, q=7681, std_dev=3.0)

def test_keypair_generation(rlwe):
    keypair = rlwe.generate_keypair()
    pk_a, pk_b = keypair["public_key"]
    sk = keypair["secret_key"]
    
    assert len(pk_a) == rlwe.n
    assert len(pk_b) == rlwe.n
    assert len(sk) == rlwe.n

def test_encryption_decryption(rlwe):
    keypair = rlwe.generate_keypair()
    
    # Generate random binary message vector
    message_bits = np.random.randint(0, 2, size=rlwe.n)
    
    ciphertext = rlwe.encrypt(keypair["public_key"], message_bits)
    decrypted_bits = rlwe.decrypt(keypair["secret_key"], ciphertext)
    
    # Verify bit-for-bit accuracy
    np.testing.assert_array_equal(decrypted_bits, message_bits)