soma = 0
divisor = 0
negativos = 0
positivos = 0
while divisor < 10:
    valor = int(input(f"digite um valor: "))
    soma += valor
    divisor += 1
    if valor < 0:
        negativos += 1
    if valor >= 0:
        positivos += 1
    media_aritmetica = soma / divisor
print(f"media aritmetica: {media_aritmetica}")
print(f"valores negativos: {negativos}")
print(f"valores positivos: {positivos}")
percentual_valores_negativos = (negativos/divisor) * 100
percentual_valores_positivos = (positivos/divisor) * 100
print(f"percentual valores negativos: {percentual_valores_negativos}%")
print(f"percentual valores positivos: {percentual_valores_positivos}%")