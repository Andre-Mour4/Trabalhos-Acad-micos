numero1 = float(input("Digite seu primeiro número: "))
numero2 = float(input("Digite seu segundo número: "))
numero3 = float(input("Digite seu terceiro número: "))
numero4 = float(input("Digite seu quarto número: "))

menor = numero1

if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

if numero4 < menor:
    menor = numero4

print("O menor numero é: " , menor)