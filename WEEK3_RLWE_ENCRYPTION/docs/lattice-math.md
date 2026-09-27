# Ring Learning With Errors (RLWE) Mathematical Foundations

## Algebraic Structure
RLWE operates over the polynomial quotient ring Z_q[x] / (x^n + 1) where:
* n is a power of 2 defining the polynomial degree bound (e.g., n = 256).
* q is a prime modulus satisfying q = 1 mod 2n.
* x^n + 1 is the cyclotomic reduction polynomial ensuring bounded degree.

## Cryptographic Operations
1. Key Generation:
   * Select secret s and error e from a discrete Gaussian distribution.
   * Sample uniform polynomial a from Z_q[x] / (x^n + 1).
   * Public key: (a, b = a * s + e mod q).

2. Encryption (Message binary vector m mapped to quotient ring):
   * Sample small noise terms r, e1, e2 from Gaussian distribution.
   * Compute ciphertext components:
     u = a * r + e1 mod q
     v = b * r + e2 + m * floor(q/2) mod q

3. Decryption:
   * Compute noisy phase:
     phase = v - u * s mod q
   * Recover original message bits by thresholding phase values relative to q/2.