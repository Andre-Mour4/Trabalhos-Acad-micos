n = int(input("digite um numero: "))
soma = 0
if n < 0:
    print("numero invalido: ")
else:
    for i in range(1, n + 1):
        soma += 1 / i
    print("Soma:", soma)