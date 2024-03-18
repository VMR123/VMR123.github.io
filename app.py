import streamlit as st
from PIL import Image
from ImageCryptography import *

def main():
    st.title("Image Encryption and Decryption")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Encrypt Image"):
            # Generate Paillier keys
            public_key, private_key = Paillier.generate_keys()

            # Perform encryption
            encrypted_image = encrypt_image(uploaded_file, public_key)

            # Save encrypted image
            encrypted_image_path = "encrypted_image.png"
            encrypted_image.save(encrypted_image_path)
            st.success("Image encrypted successfully.")

            # Provide download link for encrypted image
            st.markdown(get_download_link(encrypted_image_path, "Download Encrypted Image"), unsafe_allow_html=True)

            if st.button("Decrypt Image"):
                # Perform decryption
                decrypted_image = decrypt_image(encrypted_image, private_key)

                # Save decrypted image
                decrypted_image_path = "decrypted_image.png"
                decrypted_image.save(decrypted_image_path)
                st.success("Image decrypted successfully.")

                # Provide download link for decrypted image
                st.markdown(get_download_link(decrypted_image_path, "Download Decrypted Image"), unsafe_allow_html=True)

def encrypt_image(input_image, public_key):
    image = Image.open(input_image)
    encrypted_image = ImgEncrypt(public_key, image)
    return encrypted_image

def decrypt_image(encrypted_image, private_key):
    decrypted_image = ImgDecrypt(public_key, private_key, encrypted_image)
    return decrypted_image

def get_download_link(file_path, text):
    with open(file_path, "rb") as file:
        data = file.read()
    href = f"<a href='data:file/png;base64,{data.decode('utf-8')}' download='{file_path}'>{text}</a>"
    return href

if __name__ == "__main__":
    main()
