# Medical Image Encryption using Paillier's Encryption Scheme

## Overview
This project demonstrates the encryption and decryption of medical images using Paillier's encryption scheme. Paillier's encryption scheme is a probabilistic asymmetric algorithm, widely used for secure computations on encrypted data.

## Features
- **Encryption**: Upload a medical image file to encrypt it using Paillier's encryption scheme.
- **Decryption**: Decrypt the encrypted image using the corresponding private key.
- **Copy Keys**: Option to copy the public and private keys to the clipboard for further use.
   
## Usage
1. Run the Flask web application:
   ```bash
   python app.py
   ```
2. Open a web browser and go to `http://localhost:5000`.
3. Upload a medical image for encryption in the Encryption section.
4. Once the encryption is complete, the encrypted image will be displayed, and you can download it.
5. Copy the public and private keys using the "Copy Keys" buttons in the Encryption and Decryption sections, respectively.
6. Paste the keys in the Decryption section and upload the encrypted image for decryption.
7. Once the decryption is complete, the decrypted image will be displayed, and you can download it.

## Dependencies
- Flask
- Pillow
- Numpy

## Credits
This project was developed as part of the IT352 - Information Assurance and Security course under the guidance of Prof. Jaidhar CD.

Developers:
- Suresh Naik (211IT016)
- Prasanna Kumar (211IT047)
- Vishwa Mohan Reddy G (211IT082)
