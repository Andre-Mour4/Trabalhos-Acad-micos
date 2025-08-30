horas_trabalhadas = float(input("Digite o numero de horas trabalhadas na semana: "))

if horas_trabalhadas <= 40:
    salario = horas_trabalhadas * 15
else:
    salario = 600 + horas_trabalhadas * 21

print("O salario semanal é: R$" , salario)
