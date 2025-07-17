import base64
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from huffman_custom import HuffmanCoding
 # pip install huffman

# --------- Step 1: Huffman Compression ----------
def compress_text(text):
    h = HuffmanCoding()
    compressed_data, tree = h.compress(text)
    return compressed_data, tree, h

# --------- Step 2: RSA Key Generation ----------
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

# --------- Step 3: RSA Encryption ----------
def encrypt_data(data_bytes, public_key_bytes):
    public_key = RSA.import_key(public_key_bytes)
    cipher = PKCS1_OAEP.new(public_key)
    
    # Split into blocks (RSA max = 245 bytes for 2048-bit key)
    encrypted_blocks = []
    for i in range(0, len(data_bytes), 200):
        block = data_bytes[i:i+200]
        encrypted_blocks.append(cipher.encrypt(block))

    return b"".join(encrypted_blocks)

# --------- Step 4: Save Output ----------
def save_to_file(encrypted_data, tree, private_key):
    with open("output_encrypted.bin", "wb") as f:
        pickle.dump((encrypted_data, tree, private_key), f)

# --------- Main ----------
if __name__ == "__main__":
    with open("sample_input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Compress
    compressed_data, tree, huff_obj = compress_text(text)

    # Encode compressed binary string to bytes
    compressed_bytes = huff_obj.encode_binary(compressed_data)

    # RSA encryption
    public_key, private_key = generate_keys()
    encrypted_data = encrypt_data(compressed_bytes, public_key)

    # Save to file
    save_to_file(encrypted_data, tree, private_key)

    print("✅ Compression and encryption completed. Output saved to 'output_encrypted.bin'")