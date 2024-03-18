import streamlit as st
from PIL import Image
import base64
from ImageCryptography import *

def main():
    st.title("Image Encryption and Decryption")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Original Image", use_column_width=True)

        if st.button("Encrypt Image"):
            with st.spinner("Encrypting..."):
                encrypted_image_path = encrypt_and_show_image(uploaded_file, public_key)

            st.success("Image encrypted successfully!")
            st.image(encrypted_image_path, caption="Encrypted Image", use_column_width=True)
            st.markdown(get_binary_file_downloader_html(encrypted_image_path, "Encrypted Image"), unsafe_allow_html=True)

        if st.button("Decrypt Image"):
            with st.spinner("Decrypting..."):
                decrypted_image_path = decrypt_and_show_image(encrypted_image_path, public_key, private_key)

            st.success("Image decrypted successfully!")
            st.image(decrypted_image_path, caption="Decrypted Image", use_column_width=True)
            st.markdown(get_binary_file_downloader_html(decrypted_image_path, "Decrypted Image"), unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:file/png;base64,{bin_str}" download="{file_label}.png">Download {file_label}</a>'
    return href

if __name__ == "__main__":
    public_key, private_key = Paillier.generate_keys()
    main()
