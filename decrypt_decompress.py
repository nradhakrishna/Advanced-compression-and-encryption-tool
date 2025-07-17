import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from huffman_custom import HuffmanCoding

# --------- Step 1: Load Encrypted Data ----------
def load_from_file():
    with open("output_encrypted.bin", "rb") as f:
        encrypted_data, tree, private_key = pickle.load(f)
    return encrypted_data, tree, private_key

# --------- Step 2: RSA Decryption ----------
def decrypt_data(encrypted_data, private_key_bytes):
    private_key = RSA.import_key(private_key_bytes)
    cipher = PKCS1_OAEP.new(private_key)

    decrypted_bytes = bytearray()
    block_size = 256  # For 2048-bit key (256 bytes per encrypted block)

    for i in range(0, len(encrypted_data), block_size):
        block = encrypted_data[i:i+block_size]
        decrypted_bytes += cipher.decrypt(block)

    return bytes(decrypted_bytes)

# --------- Step 3: Huffman Decompression ----------
def decompress_data(decrypted_bytes, tree):
    h = HuffmanCoding()
    binary_str = h.bytes_to_binary(decrypted_bytes)
    original_text = h.decompress(binary_str, tree)
    return original_text

# --------- Main ----------
if __name__ == "__main__":
    encrypted_data, tree, private_key = load_from_file()

    # Decrypt with RSA
    decrypted_bytes = decrypt_data(encrypted_data, private_key)

    # Decompress with Huffman
    original_text = decompress_data(decrypted_bytes, tree)

    with open("output_decrypted.txt", "w", encoding="utf-8") as f:
        f.write(original_text)

    print("✅ Decryption and decompression completed. Output saved to 'output_decrypted.txt'")
