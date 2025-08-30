nota = int(input("Digite sua nota: "))

if nota < 0 or nota > 10:
    print("Nota invalida")
else:
    if nota >= 9:
        conceito = "A"
    else:
        if nota >= 7:
            conceito = "B"
        else:
            if nota >= 5:
                conceito = "C"
            else:
                conceito = "D"

    print("Seu conceito é: " , conceito)