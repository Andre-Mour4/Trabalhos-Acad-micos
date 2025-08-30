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
 /|\\ |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\ |
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
for i in range(27):
    print()

progresso = []
chute = []
erros = 0
erros_max = 6
andamento = True

for i in range(len(palavra)):
    progresso.append('_')

while erros < erros_max and andamento == True:
    print(bonecos[erros])
    print("Progresso: ", progresso)
    print("Letras Chutadas: ", chute)
    print()
    letra = input("Digite uma letra: ")
    print()

    chute.append(letra)

    acertou = False

    for i in range(len(palavra)):
        if palavra[i] == letra:
            progresso[i] = letra
            acertou = True

    if acertou == False:
        erros = erros + 1
        print("Letra errada! Burro! Tentativas Restantes: ", erros_max - erros)
        print()

    completo = True
    for i in progresso:
        if i == '_':
            completo = False

    if completo == True:
        andamento = False

if erros == erros_max:
    print("Você Perdeu! Tu é Burro msm! A palavra era: ", palavra)
else:
    print("Parabéns! Você não é burro!")
    print("Palavra correta: ", progresso)