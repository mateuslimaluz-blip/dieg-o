'''Crie um script que leia e imprima todos os produtos do banco loja.db criado no exercício 1, usando fetchall.'''
import sqlite3
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

conexao.row_factory = sqlite3.Row

cursor.execute(
    "SELECT * FROM produtos"
)                           # fetchall = todas as linhas
todos = cursor.fetchall()
print(todos)

um = cursor.fetchone()
print(um)
print(dict(um))

conexao.close()
"""
for linhas in todos:
    print(dict(linhas))
"""