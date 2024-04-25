import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Caminho para o diretório do frontend
frontend_path = os.path.join(os.path.dirname(__file__), 'frontend')

app = Flask(__name__, template_folder=frontend_path)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Rota para servir o arquivo HTML principal
@app.route('/')
def index():
    return render_template('index.html')

# Importando as rotas
from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=8000)
