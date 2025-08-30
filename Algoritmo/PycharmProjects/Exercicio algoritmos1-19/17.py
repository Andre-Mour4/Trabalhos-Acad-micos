fora_intervalo = 0
dentro_intervalo = 0
for i in range(1,10+1):
    n = int(input(f"digite seu numero{i}: "))
    if n >= 10 and n <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1
print(f"fora do intervalo: {fora_intervalo}")
print(f"dentro do intervalo: {dentro_intervalo}")