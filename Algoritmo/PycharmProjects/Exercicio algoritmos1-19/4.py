# 4.	A prefeitura de uma cidade fez uma
# pesquisa entre seus habitantes, coletando
# dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a.	média do salário da população;
# b.	média do número de filhos;
# c.	maior salário;
# d.	percentual de pessoas com salário
# até R$100,00;
# O final da leitura de dados se dará com a
# entrada de um salário negativo.

soma_salario = 0.0
soma_filhos = 0
quantidade_pessoas = 0
quantidade_pessoas_salario_baixo = 0
salario = float(input("Digite um salario: "))
maior_salario = salario
while salario >= 0:
    quantidade_filhos = int(input("Digite a quantidade de filhos: "))
    soma_salario = soma_salario + salario
    quantidade_pessoas = quantidade_pessoas + 1
    soma_filhos = soma_filhos + quantidade_filhos
    if salario > maior_salario:
        maior_salario = salario
    if salario <= 100:
        quantidade_pessoas_salario_baixo = quantidade_pessoas_salario_baixo + 1
    salario = float(input("Digite um salario: "))

if quantidade_pessoas > 0:
    media_salarios = soma_salario / quantidade_pessoas
    print(f"Média salarial = {media_salarios:5.2f}")
    media_filhos = soma_filhos / quantidade_pessoas
    print(f"Média de filhos = {media_filhos:5.2f}")
    print(f"Maior salario = {maior_salario}")
    percentual_salario_baixo = (quantidade_pessoas_salario_baixo / quantidade_pessoas) * 100
    print(f"Percentual salario baixo = {percentual_salario_baixo:5.2f} %")