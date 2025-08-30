salario = float(input("Digite o salário atual: "))
tempo_servico = int(input("Digite seu tempo de serviço em anos: "))
if tempo_servico <=1:
    aumento = salario * 0.10
else:
    aumento = salario * 0.20

salario_novo = salario + aumento
print("Salário reajustado: R$" , salario_novo)