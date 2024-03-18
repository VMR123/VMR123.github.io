import streamlit as st
from PIL import Image
import numpy as np
from ImageCryptography import *

def main():
    st.title("Image Encryption and Decryption")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        encrypt_button = st.button("Encrypt Image")
        if encrypt_button:
            with st.spinner("Encrypting..."):
                # Generate Paillier keys
                public_key, private_key = Paillier.generate_keys()

                # Perform encryption
                encrypted_image = encrypt_image(uploaded_file, public_key)

                # Save encrypted image
                encrypted_image_path = "encrypted_image.png"
                Image.fromarray(encrypted_image.astype(np.uint8)).save(encrypted_image_path)
                st.success("Image encrypted successfully.")

                # Provide download link for encrypted image
                st.markdown(get_download_link(encrypted_image_path, "Download Encrypted Image"), unsafe_allow_html=True)

        decrypt_button = st.button("Decrypt Image")
        if decrypt_button:
            with st.spinner("Decrypting..."):
                # Perform decryption
                decrypted_image = decrypt_image(encrypted_image, private_key)

                # Save decrypted image
                decrypted_image_path = "decrypted_image.png"
                Image.fromarray(decrypted_image.astype(np.uint8)).save(decrypted_image_path)
                st.success("Image decrypted successfully.")

                # Provide download link for decrypted image
                st.markdown(get_download_link(decrypted_image_path, "Download Decrypted Image"), unsafe_allow_html=True)

def encrypt_image(input_image, public_key):
    image = Image.open(input_image)
    image_array = np.array(image)
    encrypted_image = ImgEncrypt(public_key, image_array)
    return encrypted_image

def decrypt_image(encrypted_image, private_key):
    decrypted_image = ImgDecrypt(public_key, private_key, encrypted_image)
    return decrypted_image

def get_download_link(file_path, text):
    with open(file_path, "rb") as file:
        data = file.read()
    href = f"<a href='data:file/png;base64,{data.decode('latin-1')}' download='{file_path}'>{text}</a>"
    return href

if __name__ == "__main__":
    main()
