from PIL import Image
import numpy as np
import pickle
import os
import Paillier

def ImgEncrypt(public_key, plainimg):
    """
    args:
        public_key: Paillier PublicKey object
        plainimg: PIL Image object
        
    returns:
        cipherimg: Encryption of plainimg
    Encrypts an image
    """
    
    cipherimg = np.asarray(plainimg)
    shape = cipherimg.shape
    cipherimg = cipherimg.flatten().tolist()
    cipherimg = [Paillier.Encrypt(public_key, pix) for pix in cipherimg]
    
    return np.asarray(cipherimg).reshape(shape)


def ImgDecrypt(public_key, private_key, cipherimg):
    """
    args:
        public_key: Paillier PublicKey object
        private_key: Paillier PrivateKey object
        cipherimg: encryption of Image
        
    returns:
        Image object which is the decryption of cipherimage
    Decrypts ecnrypted image
    """
    shape = cipherimg.shape
    plainimg = cipherimg.flatten().tolist()
    plainimg = [Paillier.Decrypt(public_key, private_key, pix) for pix in plainimg]
    plainimg = [pix if pix < 255 else 255 for pix in plainimg]
    plainimg = [pix if pix > 0 else 0 for pix in plainimg]
    
    return Image.fromarray(np.asarray(plainimg).reshape(shape).astype(np.uint8))


def homomorphicBrightness(public_key, cipherimg, factor):
    """
    args:
        public_key: Paillier PublicKey object
        cipherimg: n dimensional array containing encryption of image pixels
        factor: Amount of brightness to be added (-ve for decreasing brightness)
    
    returns:
        n dimensional array containing encryption of image pixels with brightness adjusted
    
    Function to demonstrate homomorphism
    Performs brightness adjust operation on the encrypted image
    """
    shape = cipherimg.shape
    brightimg = cipherimg.flatten().tolist()
    brightimg = [Paillier.homomorphic_add_constant(public_key, pix, factor) for pix in brightimg]
    
    return np.asarray(brightimg).reshape(shape)


def saveEncryptedImg(cipherimg, filename):
    """
    args:
        cipherimg: Encryption of an image
        filename: filename to save encryption (saved under encrypted-images directory)
        
    saves Encryption of image int a file
    """
    filename = "encrypted-images/" + filename
    fstream = open(filename, "wb")
    pickle.dump(cipherimg, fstream)
    fstream.close()


def loadEncryptedImg(filename):
    """
    args:
        filename: filename of the Encrypted object under encrypted-images directory
        
    returns:
        n-dimensional array containing ecryption of image
    loads Encrypted image object from file
    """
    filename = "encrypted-images/" + filename    
    fstream = open(filename, "rb")
    cipherimg = pickle.load(fstream)
    fstream.close()
    return cipherimg

def save_and_show_encrypted_img(cipherimg, filename):
    """
    args:
        cipherimg: Encryption of an image (as a numpy array)
        filename: filename to save encryption (saved under encrypted-images directory)
        
    saves Encryption of image into a file and shows a visual representation
    """
    directory = "encrypted-images"
    if not os.path.exists(directory):
        os.makedirs(directory)  # This will create the directory if it does not exist

    filepath = os.path.join(directory, filename)
    with open(filepath, "wb") as fstream:
        pickle.dump(cipherimg, fstream)

    # Optionally, save the visual representation as an image
    normalized_img = (cipherimg - np.min(cipherimg)) / (np.max(cipherimg) - np.min(cipherimg))
    normalized_img = (normalized_img * 255).astype(np.uint8)
    
    img_to_show = Image.fromarray(normalized_img)
    img_to_show.show()

    # Save the visual representation as an image with a different extension (e.g., PNG)
    visual_filepath = os.path.join(directory, 'visual_' + filename.replace('.pkl', '.png'))
    img_to_show.save(visual_filepath)

    return filepath, visual_filepath

def encrypt_decrypt_and_show_image(input_image_path):
    # Step 1: Generate Paillier keys
    public_key, private_key = Paillier.generate_keys()

    # Step 2: Open the input image
    input_image = Image.open(input_image_path)

    # Step 3: Encrypt the image
    encrypted_image = ImgEncrypt(public_key, input_image)

    # Step 4: Save the encrypted image
    encrypted_image_path = 'encrypted_image.pkl'
    save_and_show_encrypted_img(encrypted_image, encrypted_image_path)

    # Step 5: Decrypt the encrypted image
    decrypted_image = ImgDecrypt(public_key, private_key, encrypted_image)

    # Step 6: Save the decrypted image
    decrypted_image_path = 'decrypted_image.png'
    decrypted_image.save(decrypted_image_path)

    # Step 7: Show the decrypted image
    decrypted_image.show()

    return encrypted_image_path, decrypted_image_path


def encrypt_and_show_image(input_image_path,public_key):
    
    # Open the input image
    input_image = Image.open(input_image_path)

    # Encrypt the image
    encrypted_image = ImgEncrypt(public_key, input_image)

    # Save the encrypted image
    encrypted_image_path = 'encrypted_image.pkl'
    save_and_show_encrypted_img(encrypted_image, encrypted_image_path)

    return encrypted_image_path

def decrypt_and_show_image(encrypted_image_path,public_key, private_key):

    # Load the encrypted image
    encrypted_image = loadEncryptedImg(encrypted_image_path)

    # Decrypt the encrypted image
    decrypted_image = ImgDecrypt(public_key, private_key, encrypted_image)

    # Save the decrypted image
    decrypted_image_path = 'decrypted_image.png'
    decrypted_image.save(decrypted_image_path)

    return decrypted_image_path
