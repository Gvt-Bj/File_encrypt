# File_encrypt
A file encryption python script to encrypt and decrypt a 256-bit key with SHA-256, and used to encrypt/decrypt with AES (via Fernet).

# Simple FileCrypt

A **A beginner-friendly file encryption/decryption tool** written in Python.  
This project shows how to protect files using a password and AES encryption (via Fernet).

---

## Features
- Password-based encryption using **AES + HMAC** (via `cryptography.fernet`)
- Clean, short, and easy-to-read Python code (~40 lines)
- Works on any file type (text, images, PDFs, etc.)
- One-file script — no configs, no dependencies besides `cryptography`

---

## Requirements

Install the required package:
```bash
pip install cryptography
