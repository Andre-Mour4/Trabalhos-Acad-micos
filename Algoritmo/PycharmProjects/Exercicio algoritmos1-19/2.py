# 2.	Escreva um algoritmo que leia 20 valores
# e encontre o maior e o menor deles. Mostre o
# resultado.

for i in range(5):
    numero = int(input(f"Digite o numero {i+1}: "))
    if i == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"Maior = {maior}")
print(f"Menor = {menor}")