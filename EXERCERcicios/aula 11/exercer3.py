'''Crie uma API Flask completa para produtos com banco SQLite:
• Rota GET /produtos – lista todos do banco.
• Rota POST /produtos – insere no banco (valide que o preço foi enviado).
• Teste criando produtos, reiniciando o servidor e confirmando que eles continuam salvos. Salve os testes
num arquivo testes.http.'''
from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)
def conectar():
    conexao = sqlite3.connect("escolabased.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectar()
    conexao.execute('''
        CREATE TABLE IF NOT EXISTS alunitos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    nota REAL
                    )
''')
    conexao.commit()
    conexao.close()

@app.route("/alunos", methods = ["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM alunitos")
    alunitos = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(alunitos)

@app.route("/alunos", methods=["POST"])
def criar():
    novo = request.get_json()

    if "nome" not in novo:
        return jsonify({"erro": "O campo nome é obrigatório"}), 400
    
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO alunitos (nome, nota) VALUES (?,?)",
            (novo["nome"], novo.get("nota"))
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return jsonify({"id": novo_id, **novo}), 201

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)