n = float(input("digite um numero: "))
soma = 0
divisor = 0
while n >= 0:
    divisor += 1
    soma += n
    media_aritmetica = soma/divisor
    n = float(input("digite um numero: "))
print(f"media aritmetica: {media_aritmetica}")