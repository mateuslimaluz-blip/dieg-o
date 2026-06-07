'''Reescreva a classe Produto da aula anterior usando atributos privados __nome e __preco. Implemente getters
e setters para ambos. O setter de preço deve impedir valores negativos.'''
"""TEM QUE FAZER A AULA 3 PRIMEIRO goty"""
# que se dane vou usar property dnv 
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("deve ser um texto de preferencia")

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, new_preco):
        if new_preco >= 0 :
            self.__preco = new_preco
        else:
            print("naum pode ser negativos apenas numeros racionais /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

    def amostrar(self):
        return self.nome, self.preco
    
    def desconto(self):
        preco_descontado = self.preco * (1 - 0.15)
        return preco_descontado
    
    #VAMOS TESTAR KRL

object1 = Produto("BANANA", 5.00)
print(object1.amostrar())


object1.preco = -2.50 
print(f" não vai funcionar, aqui o preço R$ {object1.preco:.2f}")

object1.preco = 4.50
print(f"Preço pós alteração R$ {object1.preco:.2f}")
print(f"Preço pós descontasso R$ {object1.desconto():.2f}\n")
