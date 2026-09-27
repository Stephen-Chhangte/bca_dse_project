import numpy as np

class RLWECipher:
    def __init__(self, n=256, q=7681, std_dev=3.0):
        """
        Parameters for RLWE encryption:
        - n: Polynomial degree bound (dimension, power of 2)
        - q: Prime modulus matching q = 1 mod 2n condition
        - std_dev: Standard deviation for discrete Gaussian noise generation
        """
        self.n = n
        self.q = q
        self.std_dev = std_dev

    def _sample_gaussian_poly(self):
        """Samples error coefficients from a discrete Gaussian approximation."""
        return np.random.normal(0, self.std_dev, self.n).round().astype(int) % self.q

    def _poly_mul(self, a, b):
        """Polynomial multiplication in the quotient ring Z_q[x] / (x^n + 1)."""
        res = np.polymul(a, b).astype(int)
        # Reduction modulo (x^n + 1): x^n = -1 mod (x^n + 1)
        reduced = np.zeros(self.n, dtype=int)
        for idx, val in enumerate(res):
            degree = idx % self.n
            sign = -1 if (idx // self.n) % 2 == 1 else 1
            reduced[degree] = (reduced[degree] + sign * val) % self.q
        return reduced

    def generate_keypair(self):
        """Generates public key (a, b) and secret key s."""
        # Uniform public polynomial 'a'
        a = np.random.randint(0, self.q, size=self.n)
        # Secret polynomial 's' and error polynomial 'e' sampled from Gaussian noise
        s = self._sample_gaussian_poly()
        e = self._sample_gaussian_poly()
        
        # Public key b = a * s + e (mod q, x^n + 1)
        b = (self._poly_mul(a, s) + e) % self.q
        return {"public_key": (a, b), "secret_key": s}

    def encrypt(self, public_key, message_bits):
        """
        Encrypts a binary message vector using RLWE.
        - public_key: Tuple (a, b)
        - message_bits: Array of binary values (0 or 1) of length n
        """
        a, b = public_key
        # Message encoding: map 0 -> 0, 1 -> q // 2
        m_poly = message_bits * (self.q // 2)

        # Sample small random noise terms
        r = self._sample_gaussian_poly()
        e1 = self._sample_gaussian_poly()
        e2 = self._sample_gaussian_poly()

        # Ciphertext components:
        # u = a * r + e1
        # v = b * r + e2 + m
        u = (self._poly_mul(a, r) + e1) % self.q
        v = (self._poly_mul(b, r) + e2 + m_poly) % self.q
        return (u, v)

    def decrypt(self, secret_key, ciphertext):
        """Decrypts RLWE ciphertext (u, v) using secret key s."""
        u, v = ciphertext
        # Phase = v - u * s (mod q, x^n + 1)
        u_s = self._poly_mul(u, secret_key)
        phase = (v - u_s) % self.q

        # Decision thresholding to decode binary payload
        decrypted_bits = np.zeros(self.n, dtype=int)
        for i in range(self.n):
            val = phase[i]
            # Distance from 0 vs distance from q//2
            dist_zero = min(val, self.q - val)
            dist_half = abs(val - (self.q // 2))
            decrypted_bits[i] = 1 if dist_half < dist_zero else 0
            
        return decrypted_bits