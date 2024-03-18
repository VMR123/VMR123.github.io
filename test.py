from PIL import Image
import numpy as np
import Paillier
import ImageCryptography

def encrypt_decrypt_and_show_image(input_image_path):
    # Step 1: Generate Paillier keys
    public_key, private_key = Paillier.generate_keys()

    # Step 2: Open the input image
    input_image = Image.open(input_image_path)

    # Step 3: Encrypt the image
    encrypted_image = ImageCryptography.ImgEncrypt(public_key, input_image)

    # Step 4: Show the encrypted image
    ImageCryptography.save_and_show_encrypted_img(encrypted_image, 'encrypted_image.pkl')

    # Step 5: Decrypt the encrypted image
    decrypted_image = ImageCryptography.ImgDecrypt(public_key, private_key, encrypted_image)

    # Step 6: Show the decrypted image
    decrypted_image.show()

# You need to provide the path to the image you want to encrypt

public_key, private_key = Paillier.generate_keys()
print(public_key)
print(private_key)

