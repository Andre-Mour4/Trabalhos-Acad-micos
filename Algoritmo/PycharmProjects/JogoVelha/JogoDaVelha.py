import random


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)
    print()


def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def numero_dif(mensagem):
    certo = False
    while certo == False:
        numero = input(mensagem)
        if len(numero) == 1:
            if numero == "0":
                certo = True
            if numero == "1":
                certo = True
            if numero == "2":
                certo = True
        if certo == False:
            print("Digite apenas 0, 1, 2 ")
    return int(numero)

def encontrar_jogada(tabuleiro, jogador):
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = jogador
                venceu = verificar_vitoria(tabuleiro, jogador)
                tabuleiro[i][j] = 0
                if venceu == True:
                    return i * 3 + j
            j = j + 1
        i = i + 1
    return -1

def jogada_maquina(tabuleiro):
    posicao = encontrar_jogada(tabuleiro, 2)
    if posicao == -1:
        posicao = encontrar_jogada(tabuleiro, 1)

    if posicao == -1:
        posicoes_vazias = []
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if tabuleiro[i][j] == 0:
                    posicoes_vazias.append(i * 3 + j)
                j = j + 1
            i = i + 1
        posicao = posicoes_vazias[random.randint(0, len(posicoes_vazias) - 1)]

    linha = posicao // 3
    coluna = posicao % 3
    return linha, coluna

def jogar():
    tabuleiro = [

        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]

                ]

    rodadas = 0
    mostrar_tabuleiro(tabuleiro)

    acabou = False

    while rodadas < 9 and acabou == False:
        jogada_valida = False

        while jogada_valida == False:

            linha = numero_dif("Digite a linha (0 a 2): ")
            coluna = numero_dif("Digite a coluna (0 a 2): ")

            if tabuleiro[linha][coluna] == 0:
                tabuleiro[linha][coluna] = 1
                rodadas = rodadas + 1
                mostrar_tabuleiro(tabuleiro)
                jogada_valida = True

                if verificar_vitoria(tabuleiro, 1) == True:
                    print("Você venceu!")
                    acabou = True
            else:
                print("Espaço ocupado! Tente novamente.")

        if rodadas < 9 and acabou == False:
            print("Vez da máquina...")
            print()
            lin, col = jogada_maquina(tabuleiro)
            tabuleiro[lin][col] = 2
            rodadas = rodadas + 1
            mostrar_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro, 2) == True:
                print("A máquina venceu!")
                acabou = True

    if acabou == False:
        print("Empate!")

jogar()
