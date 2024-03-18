from flask import Flask, render_template, request, send_file
from ImageCryptography import *

app = Flask(__name__)

@app.route('/')
def index():
    # Generate keys
    public_key, private_key = Paillier.generate_keys()
    return render_template('index.html', public_key=public_key, private_key=private_key)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    # Save the uploaded file temporarily
    input_image_path = 'temp_input_image.png'
    file.save(input_image_path)
    
    # Perform encryption
    encrypted_image_path, decrypted_image_path = encrypt_decrypt_and_show_image(input_image_path)
    
    # Return paths for encrypted and decrypted images
    return encrypted_image_path, decrypted_image_path

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
