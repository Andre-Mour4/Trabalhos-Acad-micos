# 1.	Escrever um algoritmo que lê 10 valores
# e conte quantos destes valores são
# negativos, escrevendo esta informação

negativos = 0
for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    if valor < 0:
        negativos = negativos + 1
print(f"Quantidade de negativos = {negativos}")