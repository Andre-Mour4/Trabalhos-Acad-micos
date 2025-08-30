numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
codigo = int(input("Digite o código de seleção: " ))

if codigo < 1 or codigo > 4:
    print("codigo invalido")
else:
    if codigo == 1:
        conta = numero1 + numero2
    else:
        if codigo == 2:
            conta = numero1 * numero2
        else:
            if codigo == 3:
                conta = numero1 / numero2

    print("O  reultado é: " , conta)