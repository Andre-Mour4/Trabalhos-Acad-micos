numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

if soma < 8:
    media = (numero1 + numero2) / 2
    print("A média dos numero é: " , media)
else:
    if soma == 8:
        produto = numero1 * numero2
        print("Seu produto é: " , produto)
    else:
        if numero1 > numero2:
            divisao = numero1 / numero2
        else:
            divisao = numero2 / numero1
        print("A divisão do maior pelo menor é: " , divisao)