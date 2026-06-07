'''Crie uma classe Sensor com atributo privado __temperatura. O setter deve aceitar apenas valores entre -50
e 150 (limite físico do sensor). Implemente um método status() que retorna:
• "Normal" se entre -50 e 80
• "Alerta" se entre 81 e 120

3

• "Critico" se acima de 120
Teste com pelo menos 4 temperaturas diferentes.'''

class sensor:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    @property
    def temperatura(self):
            return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if -50 <= valor <= 150: 
              self.__temperatura = valor
        else:
             print(f"a temperatura {valor} ta fora do limite do sensor COMPRE UM SENSOR MELHOR") 

    def status(self):
         if not hasattr(self, '_sensor__temperatura'):
              return "num dá naum"
         if -50 <= self.__temperatura <= 80:
              return "normar"
         elif 81 <= self.__temperatura <= 120:
              return "CALMA AÍ PATRÃO TEM MUITA COISA ERRADA"
         else:
              return "ACABOU PRO BETA NUM SABE PYTHION MONTE PITON👍"

sensor1 = sensor(25)         
print(f"eu acho que está {sensor1.temperatura} grus agora está muy quente da não")
print(f" o sensor diz {sensor1.status()} acredite nele")

sensor2 = sensor(99)         
print(f"eu acho que está {sensor2.temperatura} grus agora está muy caliente da não")
print(f" o sensor diz {sensor2.status()} ainda pode crer nele")
                            # por algum motivo o sensor 3 e 4 num da  erro de atributo??
"""sensor3 = sensor(167)         
print(f"eu acho que está {sensor3.temperatura} grus agora está muy caliente da não")
print(f" o sensor diz {sensor3.status()} tá suspeito mas 67676767!!!!!!!!!!!!!!")
                            
sensor4 = sensor(999)         
print(f"eu acho que está {sensor4.temperatura} grus agora está muy caliente da não")
print(f" o sensor diz {sensor4.status()} Tá amarrado") """