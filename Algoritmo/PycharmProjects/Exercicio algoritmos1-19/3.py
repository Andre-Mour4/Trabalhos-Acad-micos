#3.	Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial de N (N!).
numero = int(input("digite seu numero: "))
if numero < 0:
    print("numero invalido")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"fatorial= {fatorial}")