from flask import request, jsonify
from app import app, db
from models import Colaborador, RelatorioDespesa

@app.route('/criar_bd', methods=['GET'])
def criar_bd():
    db.create_all()
    return jsonify({'message': 'Banco de dados criado com sucesso!'})

# Exemplo de rota para listar todos os colaboradores
@app.route('/colaboradores', methods=['GET'])
def listar_colaboradores():
    colaboradores = Colaborador.query.all()
    output = [{'id': c.id, 'nome': c.nome, 'cargo': c.cargo} for c in colaboradores]
    return jsonify({'colaboradores': output})

# Exemplo de rota para criar um novo colaborador
@app.route('/colaboradores', methods=['POST'])
def criar_colaborador():
    data = request.get_json()
    novo_colaborador = Colaborador(nome=data['nome'], cargo=data['cargo'])
    db.session.add(novo_colaborador)
    db.session.commit()
    return jsonify({'message': 'Colaborador criado com sucesso!'})

# Outras rotas para CRUD de colaboradores e relatórios de despesa podem ser adicionadas aqui

# Exemplo de rota para listar todos os relatórios de despesa
@app.route('/relatorios', methods=['GET'])
def listar_relatorios():
    relatorios = RelatorioDespesa.query.all()
    output = [{'id': r.id, 'descricao': r.descricao, 'valor': r.valor} for r in relatorios]
    return jsonify({'relatorios': output})

# Outras rotas para CRUD de relatórios de despesa podem ser adicionadas aqui
