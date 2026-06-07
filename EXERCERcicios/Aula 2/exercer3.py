"""Crie uma tupla com 6 números (4, 7, 2, 9, 1, 5). Use count para contar quantas vezes o número 7
aparece. Use index para descobrir em qual posição o número 9 está."""
num = (4, 7, 2, 9, 1, 5)
quantidade = num.count(7)

o_nove = num.index(9)

print(f"o 7 é {quantidade} vez e o 9 está em {o_nove}")