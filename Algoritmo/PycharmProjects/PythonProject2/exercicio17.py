codigo = int(input("Digite o código de disco: "))

if codigo == 1:
    tipo = "CD-ROM (700MB)"
else:
    if codigo == 2:
        tipo = "DVD-ROM (4.7GB)"
    else:
        if codigo == 3:
            tipo = "DVD-9 (8.54 GB)"
        else:
            if codigo == 4:
                tipo = "Blu-Ray (25 GB)"
            else:
                tipo = "Código inválido"

print("Tipo de unidade:", tipo)
