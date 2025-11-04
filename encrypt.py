# encrypt.py
# A script to encrypt/decrypt files using Fernet (AES + HMAC)
# pip install cryptography

from cryptography.fernet import Fernet
import sys
import getpass
import base64
import hashlib

def make_key(password):
    # derive 32-byte key from password using SHA256
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_file(path, key):
    with open(path, "rb") as f:
        data = f.read()
    token = Fernet(key).encrypt(data)
    with open(path + ".enc", "wb") as f:
        f.write(token)
    print("Encrypted ->", path + ".enc")

def decrypt_file(path, key):
    with open(path, "rb") as f:
        data = f.read()
    plain = Fernet(key).decrypt(data)
    out = path.replace(".enc", "") + ".dec"
    with open(out, "wb") as f:
        f.write(plain)
    print("Decrypted ->", out)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 simple_filecrypt.py [encrypt|decrypt] <file>")
        sys.exit(1)

    mode, filename = sys.argv[1], sys.argv[2]
    pwd = getpass.getpass("Password: ")
    key = make_key(pwd)

    if mode == "encrypt":
        encrypt_file(filename, key)
    elif mode == "decrypt":
        decrypt_file(filename, key)
    else:
        print("Unknown mode:", mode)

if __name__ == "__main__":
    main()
