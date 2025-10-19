# Hybrid Encryption

A hybrid encryption implementation combining RSA asymmetric encryption for secure key exchange with AES symmetric encryption for fast data processing. This approach uses RSA-2048 (you are free to use anyother algos) to encrypt a randomly generated AES-256 key (again free to use any algo), which then encrypts the actual data, providing both security and efficiency. 

## Aim of this project 

The system enables secure file encryption/decryption with automatic key management and supports cross-platform compatibility. Install dependencies with `pip install pycryptodome` just a sample use any libraries you find comfortable and use the provided scripts for generating RSA key pairs, encrypting files with public keys, and decrypting with private keys. Perfect for securing large files while maintaining the security benefits of public-key cryptography.

Refence repository :  https://github.com/raptor7197/Hybrid-Encryption/
This is my Implementation try something different maybe try implementing it with websockets to make E2E more secure 
