# Compression and Encryption Tool

This project implements a basic tool that first compresses text data using Huffman coding, and then encrypts the compressed data using the RSA encryption algorithm.

The goal is to reduce the size of the data before securing it, combining data compression and cryptographic security in one pipeline.

## Features

- Compresses text input using Huffman coding.
- Encrypts the compressed binary using RSA (2048-bit keys).
- Decryption and decompression restore the original text exactly.
- Uses Python libraries (pycryptodome) for cryptographic operations.
- Binary data and encryption keys are safely stored using pickle.

## File Structure

compression_encryption_tool/
├── compress_encrypt.py       # Compresses and encrypts text
├── decrypt_decompress.py     # Decrypts and decompresses the encrypted data
├── huffman_custom.py         # Huffman coding logic
├── sample_input.txt          # Sample input text file
└── output_encrypted.bin      # Encrypted binary file (generated)

## Requirements

Install the required Python packages:

pip install pycryptodome

## How to Use

1. Put your input text in sample_input.txt.
2. Run the compression and encryption script:

   python compress_encrypt.py

3. To decrypt and decompress:

   python decrypt_decompress.py

4. The output will be saved as output_decrypted.txt.

## Security Note

This project is a simplified demonstration of compression and encryption. It is not intended for production use or to replace full-featured encryption libraries or tools.

## License

This project is open-source and free to use under the MIT License.
