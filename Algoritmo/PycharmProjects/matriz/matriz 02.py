def soma_total(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma = soma + matriz[i][j]
    return soma

def soma_diagonal(matriz_6x6):
    soma = 0
    for i in range(len(matriz_6x6)):
        soma = soma + matriz_6x6[i][i]
    return soma

def soma_diagonal_sec(matriz_6x6):
    soma = 0
    for i in range(len(matriz_6x6)):
        j = len(matriz_6x6) - 1 - i
        soma = soma + matriz_6x6[i][j]
    return soma

def soma_7x6(matriz_7x6):
    soma = 0
    for i in range(len(matriz_7x6)):
        soma = soma + matriz_7x6[i][2]
    for j in range(len(matriz_7x6[0])):
        soma = soma + matriz_7x6[4][j]
    soma = soma - matriz_7x6[4][2]
    return soma




matriz_5x5 = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
         ]
matriz_6x6 = [
    [ 1,  2,  3,  4,  5,  6],
    [ 7,  8,  9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
             ]

matriz_7x6 = [
    [ 1,  2,  3,  4,  5,  6],
    [ 7,  8,  9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42]
         ]
# O 27 esta em ambas as contas, precisa subtrair por ele para dar o resultado


print("Soma total matriz 5x5 : ", soma_total(matriz_5x5))
print("Soma diagonal 6x6: ", soma_diagonal(matriz_6x6))
print("Soma diagonal Sec 6x6: ", soma_diagonal_sec(matriz_6x6))
print("Soma da linha 5 e coluna 3:", soma_7x6(matriz_7x6))