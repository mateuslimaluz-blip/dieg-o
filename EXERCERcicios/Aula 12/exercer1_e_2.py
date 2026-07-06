'''Pegue sua API de produtos da aula anterior e adicione a rota PUT /produtos/<int:id> para atualizar um
produto. Retorne 404 se o produto não existir.'''
from flask import Flask, jsonify, request
import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nota FLOAT NOT NULL,
               serie TEXT NOT NULL
)
""")

cursor.execute("""
    INSERT INTO alunos (nome, nota, serie) VALUES
    ("Mateus", 1.5, "3°"),
    ("Vitor", 2.9, "2°"),
    ("Ana", 6.7, "3°"),
    ("Carimbo", 6.0, "1°"),
    ("Giuseppe", 9.9, "3°"),
    ("Gui", 5.5, "2°"),
    ("Rock lee", 7.8, "3°"),
    ("Boruto é ruim", 4.6, "2°"),
    ("Neymar", 10.0, "1°"),
    ("Ancelloti", 9.5, "1°")
""")
conexao.commit()

# começando a atividade de verdade
# ROTA put

conexao.execute(
    "UPDATE alunos SET nome = ?, nota = ?, serie = ? WHERE id = ?",
    ("MATEUS MR GOLANG", 10.0, "1°", 1)
)

conexao.commit()

# DELETE 

conexao.execute("DELETE FROM alunos WHERE id = ?", (10,))

conexao.commit() # a teoria diz que na tabela o ancelloti não deveria existir e eu não devo ter apenas mateus no id 1 

# parte do flask                         '''("Vitor beta usador de windows", 1.1, "1°", 2)'''

app = Flask(__name__) 

"""rota GET pq não ta mostrando no navegador"""

@app.route("/alunos", methods =["GET"])
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")

    alunos = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(alunos)


def conectar():
    conexao = sqlite3.connect("escola.db")
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route("/alunos/<int:id>", methods = ["PUT"])
def atualizar(id):
    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE alunos SET nome = ?, nota = ?, serie = ? WHERE id =?",
        (dados["nome"], dados.get("nota"), dados.get("serie"), id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    if afetadas == 0:
       return jsonify({ "erro": "aluno não achado"}), 404
    return jsonify ({"id": id, **dados})


# route delete 
@app.route("/alunos/<int:id>", methods = ["DELETE"])
def apagar(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    conexao.commit()
    
    afetadas = cursor.rowcount
    conexao.close()
    if afetadas == 0:
        return jsonify ({"mensagem": "aluno nao achado"}), 404
    return jsonify ({"mensagem": "aluno deixou de existir"})

if __name__ == "__main__":
    app.run(debug=True)