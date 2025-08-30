valores = []
maior = 0

numero = int(input("Digite um número: "))
if numero < 0:
    print("Número invalido")
else:
    for i in range(9):
        numero = int(input("Digite um número: "))
        valores.append(numero)

        if i == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
    print("O maior valor é:", maior)
