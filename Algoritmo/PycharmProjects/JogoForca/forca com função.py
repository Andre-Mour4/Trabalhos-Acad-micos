def limpar_tela():
    for i in range(27):
        print()

def mostrar_boneco(erros, bonecos):
    print(bonecos[erros])

def mostrar_progresso(progresso):
    print("Progresso: ", end="")
    for i in range(len(progresso)):
        print(progresso[i], end=" ")
    print()

def mostrar_chutes(chute):
    print("Letras Chutadas: ", chute)
    print()

def verificar_repetida(letra, chute):
    repetida = False
    for i in range(len(chute)):
        if chute[i] == letra:
            repetida = True
    return repetida

def atualizar_progresso(letra, palavra, progresso):
    acertou = False
    for i in range(len(palavra)):
        if palavra[i] == letra:
            progresso[i] = letra
            acertou = True
    return acertou

def verificar_completo(progresso):
    completo = True
    for i in progresso:
        if i == "_":
            completo = False
    return completo

def jogo_forca():
    bonecos = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========
"""
    ]

    palavra = input("Digite uma palavra: ")
    palavra = palavra.upper()

    limpar_tela()

    progresso = []
    chute = []
    erros = 0
    erros_max = 6
    andamento = True

    for i in range(len(palavra)):
        progresso.append("_")

    while erros < erros_max and andamento == True:
        mostrar_boneco(erros, bonecos)
        mostrar_progresso(progresso)
        mostrar_chutes(chute)

        letra = input("Digite uma letra: ")
        letra = letra.upper()
        print()

        valido = True

        if len(letra) != 1:
            print("Digite apenas UMA letra.")
            valido = False

        if verificar_repetida(letra, chute):
            print("Você já tentou essa letra.")
            valido = False

        if valido == True:
            chute.append(letra)

            acertou = atualizar_progresso(letra, palavra, progresso)

            if acertou == False:
                erros = erros + 1
                print("Letra errada! Tentativas Restantes: ", erros_max - erros)
                print()

            if verificar_completo(progresso):
                andamento = False

    mostrar_boneco(erros, bonecos)
    if erros == erros_max:
        print("Você Perdeu! A palavra era: ", palavra)
    else:
        print("Parabéns! Você acertou!")
        print("Palavra correta: ", progresso)


jogo_forca()