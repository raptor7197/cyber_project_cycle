# Hybrid Encryption

A hybrid encryption implementation combining RSA asymmetric encryption for secure key exchange with AES symmetric encryption for fast data processing. This approach uses RSA-2048 to encrypt a randomly generated AES-256 key, which then encrypts the actual data, providing both security and efficiency. 

## Aim of this project 

The system enables secure file encryption/decryption with automatic key management and supports cross-platform compatibility. Install dependencies with `pip install pycryptodome` and use the provided scripts for generating RSA key pairs, encrypting files with public keys, and decrypting with private keys. Perfect for securing large files while maintaining the security benefits of public-key cryptography.
