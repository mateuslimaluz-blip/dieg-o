''' Crie uma classe mãe Animal com o atributo nome e um método comer() que imprime “[nome] está comendo”.
Crie uma classe lha Cachorro que herda de Animal e adiciona um método latir(). Crie um objeto Cachorro
e teste os dois métodos.'''
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"o {self.nome} está comendo")
              
class cachoro(Animal):
    def __init__ (self, raca, nome):
        super().__init__(nome)
        self.raca = raca

    def latir(self):
        print(f"o {self.nome} is latindo now!")

my_dog = cachoro("caramelo", "bob")
my_dog.comer()
my_dog.latir()