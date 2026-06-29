"""Crie um script que conecte a um banco loja.db, crie uma tabela produtos (id, nome, preco) e insira 3
produtos."""
import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco DECIMAL NOT NULL 
                 )
""")
conexao.commit()

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?,?)",
    ("batata",12.50)
)
cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?,?)",
    ("pao" , 7.50)
)
cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?,?)",
    ("Pichau" , 700.50)
)
conexao.commit()
conexao.close()