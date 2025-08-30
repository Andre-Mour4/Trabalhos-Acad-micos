import random


pedra = 0
papel = 1
tesoura = 2

jogador_vitorias = 0
computador_vitorias = 0
empates = 0
rodadas = 0

limite_partidas = int(input("Quantas partidas você quer jogar? "))

print("0 = pedra, 1 = papel, 2 = tesoura")

while rodadas < limite_partidas and jogador_vitorias < 3 and computador_vitorias < 3:
    partidas_restantes = limite_partidas - rodadas

    if jogador_vitorias + partidas_restantes < 3:
        rodadas = limite_partidas
    else:
        if computador_vitorias + partidas_restantes < 3:
            rodadas = limite_partidas
        else:
            computador = random.randint(0, 2)
            numero = int(input("Digite um número de 0 a 2: "))

            if numero < 0 or numero > 2:
                print("Valor inválido")
            else:
                if numero == computador:
                    print("Empate")
                    empates = empates + 1
                else:
                    if numero == 0 and computador == 2:
                        print("Você ganhou essa rodada!")
                        jogador_vitorias = jogador_vitorias + 1
                    else:
                        if numero == 1 and computador == 0:
                            print("Você ganhou essa rodada!")
                            jogador_vitorias = jogador_vitorias + 1
                        else:
                            if numero == 2 and computador == 1:
                                print("Você ganhou essa rodada!")
                                jogador_vitorias = jogador_vitorias + 1
                            else:
                                print("Você perdeu essa rodada!")
                                computador_vitorias = computador_vitorias + 1

                print("Computador escolheu:", computador)
                print("Placar: Você", jogador_vitorias, "x", computador_vitorias, "Computador")
                print("Empates:", empates)
                print()
                rodadas = rodadas + 1


print("=== FIM DE JOGO ===")
if jogador_vitorias > computador_vitorias:
    print("Parabéns! Você venceu o jogo!")
else:
    if computador_vitorias > jogador_vitorias:
        print("Você perdeu o jogo. Tente novamente!")
    else:
        print("O jogo terminou empatado!")
