from app import db

class Colaborador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)

class RelatorioDespesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_colaborador = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    aprovado = db.Column(db.Boolean, default=False)
    assinado = db.Column(db.Boolean, default=False)
