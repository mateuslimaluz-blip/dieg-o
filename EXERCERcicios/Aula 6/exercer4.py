'''Crie uma classe mãe Pagamento com método processar(valor). Crie três lhas:
• Dinheiro – aplica 5% de desconto
• Cartao – aplica 2% de juros
• Pix – valor sem alteração
Cada uma sobrescreve processar(valor) retornando o valor nal. Crie uma lista com os três tipos e mostre
o resultado de um pagamento de R$ 100,00 em cada forma.'''
class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def processar_pagamento(self):
        return 0
    
class dinheiro(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar_pagamento(self):
        return self.valor * 0.95
    
class cartao(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar_pagamento(self):
        return self.valor * 1.02
    
class Pix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
    
    def processar_pagamento(self):
        return self.valor
    
Pagar = [
    dinheiro(100),
    cartao(100),
    Pix(100),
]

for p in Pagar:
    tipo = p.__class__.__name__
    valor_final = p.processar_pagamento()
    print(f"Forma : {tipo} Valor Original : {p.valor} Valor Após : {valor_final: .2f}")