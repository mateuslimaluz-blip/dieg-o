"""Crie uma classe Produto com os atributos nome e preco. Crie dois objetos com produtos diferentes e imprima
o nome e o preço de cada um."""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def amostrar(self):
        return self.nome, self.preco
    
object1 = Produto("BANANA", 5)
print(object1.amostrar())

object2 = Produto("COMPUTADOR PICHAU GAMER ATENA 3 INTEL I7 GEFORCE 16 GB HD 1 TERABYTE", 6767)
print(object2.amostrar(
    
))
