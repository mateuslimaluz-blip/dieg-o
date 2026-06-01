"""Crie uma classe mãe Veiculo com atributos marca e ano, e um método informacoes() que imprime os dois.
Crie duas classes lhas: Carro (com atributo portas) e Moto (com atributo cilindradas). Use super() em
ambas. Crie um objeto de cada e teste."""
class veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def informacoes(self):
        print(f"marca {self.marca} ano {self.ano}.")

class Francesco_Bernoli(veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas
    
class Moto(veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

my_car = Francesco_Bernoli("não sei a marca", 1945, 0)
my_moto = Moto("mitsubish", 1946, "oq é isso?")

my_car.informacoes()
my_moto.informacoes()