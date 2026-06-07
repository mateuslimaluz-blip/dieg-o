"""Adicione à classe Produto um método chamado desconto() que recebe um percentual e retorna o novo preço
com desconto aplicado.
Exemplo: produto com preço 100.0 e desconto de 10 deve retornar 90.0."""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def amostrar(self):
        return self.nome, self.preco
    
    def desconto(self):
        preco_descontado = self.preco * (1 - 0.15)
        return preco_descontado
    
object1 = Produto("BANANA", 5)
print(object1.amostrar())

object2 = Produto("COMPUTADOR PICHAU GAMER ATENA 3 INTEL I7 GEFORCE 16 GB HD 1 TERABYTE", 6767)
print(object2.amostrar())
print(f"preco sem desconto é esse {object2.preco} agora {object2.desconto():.2f} toma ai seu desconto")
# agora vou ir fazer o 1 da aula 4 com esse codiguin hihi levei vantagi 