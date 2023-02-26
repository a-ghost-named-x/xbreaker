#!/usr/bin/python3
import binascii

ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

ciphertext_bytes = binascii.unhexlify(ciphertext)
key_bytes = key.encode()

plaintext_bytes = bytearray()
for i in range(len(ciphertext_bytes)):
    plaintext_bytes.append(ciphertext_bytes[i] ^ key_bytes[i % len(key_bytes)])

plaintext = plaintext_bytes.decode()
print("Plaintext:", plaintext)
