from flask import Flask, request, jsonify
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64

app = Flask(__name__)

# Carregar chave privada do arquivo
with open("private_key.pem", "rb") as key_file:
    private_key_data = key_file.read()

# Carregar chave privada
private_key = serialization.load_pem_private_key(
    private_key_data,
    password=None,  # Nenhuma senha, pois a chave não é criptografada
    backend=default_backend()
)

@app.route('/sign', methods=['POST'])
def sign_document():
    document = request.json['document'].encode()

    # Assinar documento
    signature = private_key.sign(
        document,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Codificar a assinatura em base64 para envio
    encoded_signature = base64.b64encode(signature).decode()

    return jsonify({'signature': encoded_signature})

if __name__ == '__main__':
    app.run(debug=True)
