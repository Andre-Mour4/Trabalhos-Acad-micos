intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
valor = int(input("digite seu valor: "))
while valor >= 0 and valor <= 100:
    if valor >= 0 and valor <= 25:
        intervalo1 += 1
    if valor >= 26 and valor <= 50:
        intervalo2 += 1
    if valor >= 51 and valor <= 75:
        intervalo3 += 1
    if valor >= 76 and valor <= 100:
        intervalo4 += 1
    valor = int(input("digite seu valor: "))
print(f"intervalo 0/25: {intervalo1}")
print(f"intervalo 26/50: {intervalo2}")
print(f"intervalo 51/75: {intervalo3}")
print(f"intervalo 76/100: {intervalo4}")