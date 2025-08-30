par = 0
impar = 0
soma = 0
soma_pares = 0
divisor = 0
valor = int(input("digite seu valor: "))
while valor >= 0:
    soma += valor
    divisor += 1
    if valor < 0:
        print("valor invalido")
    else:
        if valor % 2 == 0:
            par += 1
            soma_pares += valor
        if valor % 2 != 0:
            impar += 1
    media_pares = soma_pares/par
    media_geral = soma/divisor
    valor = int(input("digite seu valor: "))
print(f"numeros pares: {par}")
print(f"numeros impares: {impar}")
print(f"media numeros pares: {media_pares}")
print(f"media geral dos valores: {media_geral}")