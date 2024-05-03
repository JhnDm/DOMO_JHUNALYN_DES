from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate a DES Key
def generate_des_key():
    return get_random_bytes(8)  

# Create a Cipher Instance
def create_cipher(key, mode):
    return DES.new(key, mode)

#  Convert String to Byte[] Array
def string_to_bytes(data):
    return data.encode('utf-8')

#  Encryption
def encrypt_message(cipher, plaintext):
    padded_data = pad_data(plaintext)
    return cipher.encrypt(padded_data)

# Decryption
def decrypt_message(cipher, ciphertext):
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad_data(decrypted_data)

# Helper function for padding
def pad_data(data):
    block_size = DES.block_size
    pad_len = block_size - (len(data) % block_size)
    padding = bytes([pad_len]) * pad_len
    return data + padding

# Helper function for unpadding
def unpad_data(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Generate DES key securely
des_key = generate_des_key()

# Create Cipher instance with ECB mode (DES is a block cipher)
des_cipher = create_cipher(des_key, DES.MODE_ECB)

# Continue encrypting and decrypting until 'exit' is entered
while True:
    plaintext = input("Enter the plaintext message (type 'exit' to quit): ")
    if plaintext.lower() == 'exit':
        print("Exiting...")
        break
    
    # Convert plaintext to bytes
    plaintext_bytes = string_to_bytes(plaintext)

    # Encryption
    encrypted_data = encrypt_message(des_cipher, plaintext_bytes)
    print("Encrypted Text (in hex):", encrypted_data.hex())

    # Decryption
    decrypted_data = decrypt_message(des_cipher, encrypted_data)
    print("Decrypted Text:", decrypted_data.decode('utf-8'))
