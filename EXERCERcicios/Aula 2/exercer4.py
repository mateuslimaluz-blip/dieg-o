"""Crie uma tupla com 5 temperaturas (36.5, 37.2, 38.0, 36.8, 39.1). Percorra com for e imprima uma
mensagem para cada:
• Abaixo de 37.5 → "Normal"
• De 37.5 até 38.5 → "Febre moderada"
• Acima de 38.5 → "Febre alta"""
temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)
for temp in temperaturas:
    if temp < 37.5:
        print("normal")
    elif 37.5 <= temp <= 38.5:
        print("febre")
    else:
        print("eita o bicho pegou")