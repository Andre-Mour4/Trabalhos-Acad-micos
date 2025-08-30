nota = int(input("Digite uma nota: "))
if nota < 0 or nota > 100:
    print("Nota invalida")
else:
    if nota >= 60:
        print("Aprovado")
    else:
        print("Reprovado")