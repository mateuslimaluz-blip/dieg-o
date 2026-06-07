'''Crie uma classe Carro com os atributos marca, modelo e velocidade (inicia em 0). Crie os métodos
acelerar() que soma 10 à velocidade e frear() que subtrai 10 (mínimo 0). Crie um objeto, acelere 3 vezes,
freie 1 vez e imprima a velocidade final.'''
class carlinhosF1:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
                #sou muito burro ia colocar um property pra settar a velocidade em 0

    def acelera_bichão(self):
         self.velocidade += 10
    
    def freia_catapimbas(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
    
carlos = carlinhosF1("Peugeot", "2011")
carlos.acelera_bichão()
carlos.acelera_bichão()
carlos.acelera_bichão()
carlos.acelera_bichão()

carlos.freia_catapimbas()
print(f"velocidade : {carlos.velocidade}")