n = int(input("Digite um valor N: "))
if n <0:
    print("valor invalido")
else:
    e = 1
    fatorial = 1
    for i in range(1, n + 1):
       fatorial *= i
       e += 1 / fatorial
    print("E =", e)