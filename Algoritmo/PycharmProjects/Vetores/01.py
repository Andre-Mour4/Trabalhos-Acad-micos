valores = []
quantidade = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    valores.append(numero)
    if numero < 0:
        quantidade = quantidade + 1

print("Quantidade de número negativos:", quantidade)