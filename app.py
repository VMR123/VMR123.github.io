import streamlit as st
from PIL import Image
from ImageCryptography import *

def main():
    st.title('Image Cryptography')

    # Generate keys
    public_key, private_key = Paillier.generate_keys()

    # Display keys
    st.header('Public Key:')
    st.write(public_key)
    st.header('Private Key:')
    st.write(private_key)

    # Upload image for encryption
    st.subheader('Encryption')
    uploaded_file = st.file_uploader("Upload image for encryption", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        # Perform encryption
        encrypted_image_path, decrypted_image_path = encrypt_decrypt_and_show_image(uploaded_file, public_key)

        # Display encrypted image
        st.image(encrypted_image_path, caption='Encrypted Image', use_column_width=True)

        # Download link for encrypted image
        st.markdown(get_download_link(encrypted_image_path, 'Download Encrypted Image'), unsafe_allow_html=True)

        # Display decryption section
        st.subheader('Decryption')
        st.info("Use the same keys and the encrypted image to decrypt.")

def encrypt_decrypt_and_show_image(uploaded_file, public_key):
    # Open the uploaded image
    input_image = Image.open(uploaded_file)

    # Perform encryption
    encrypted_image = ImgEncrypt(public_key, input_image)

    # Save the encrypted image
    encrypted_image_path = 'encrypted_image.png'
    encrypted_image.save(encrypted_image_path)

    # Perform decryption (for demonstration purposes)
    decrypted_image = ImgDecrypt(public_key, private_key, encrypted_image)

    # Save the decrypted image
    decrypted_image_path = 'decrypted_image.png'
    decrypted_image.save(decrypted_image_path)

    return encrypted_image_path, decrypted_image_path

def get_download_link(file_path, text):
    with open(file_path, "rb") as file:
        data = file.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="{file_path}">{text}</a>'
    return href

if __name__ == '__main__':
    main()
