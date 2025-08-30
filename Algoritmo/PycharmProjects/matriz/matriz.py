def soma_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][i]
    return soma

def soma_diagonal_sec(matriz):
    soma = 0
    for i in range(len(matriz)):
        j = len(matriz) - 1 - i
        soma = soma + matriz[i][j]
    return soma

def soma_linha(matriz):
    soma = 0
    for i in range(len(matriz[0])):
        soma = soma + matriz[0][i]
    return soma

def soma_coluna(matriz):
    colunas = len(matriz[2])
    for j in range(colunas):
        soma = 0
        for i in range(len(matriz)):
            soma = soma + matriz[i][j]
        return soma


def soma_total(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma = soma + matriz[i][j]
    return soma

matriz = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
         ]

print("soma diagonal ", soma_diagonal(matriz))
print()
print("soma diagnoal sec ", soma_diagonal_sec(matriz))
print()
print("soma linha ", soma_linha(matriz))
print()
print("soma coluna ", soma_coluna(matriz))
print()
print("soma total ", soma_total(matriz))