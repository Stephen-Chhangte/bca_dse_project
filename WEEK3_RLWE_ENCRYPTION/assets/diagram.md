# RLWE Post-Quantum Encryption Workflow

```mermaid
graph TD
    A["Parameter Setup

n=256, q=7681, sigma=3.0"] --> B["Key Generation


Sample s, e ~ Gaussian


Compute b = a*s + e (mod q)"]
B --> C["Message Encoding


Map Bits to {0, q/2}"]
C --> D["Encryption


Sample r, e1, e2 ~ Gaussian


Compute u = a*r + e1


Compute v = br + e2 + m(q/2)"]
D --> E["Transmission


Ciphertext (u, v)"]
E --> F["Decryption


Compute phase = v - u*s (mod q)"]
F --> G["Threshold Decoding


Recover Original Bits"]