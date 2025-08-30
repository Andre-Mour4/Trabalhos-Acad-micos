nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota na primeira prova (0 a 10): "))
nota2 = float(input("Digite sua nota na segunda prova (0 a 10): "))
trabalho = float(input("Digite sua nota do trabalho (0 a 10): "))
frequencia = int(input("Digite o numero de faltas nas aulas: "))

media = (nota1 * 3 + nota2 * 5 + trabalho * 2) / 10

print("Nome: " , nome)

if frequencia > 15:
    print("Reprovado")
else:
    if media >= 6.0:
        print("Aprovado")
    else:
        print("Você deverá fazer a prova final")

