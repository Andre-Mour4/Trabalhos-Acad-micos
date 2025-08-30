valor_salario = float(input("Digite seu salário: "))
financiamento = float(input("Digite o financiamento desejado: "))

if financiamento <= 5 * valor_salario:
    print("Financiamento concedido")
else:
    print("Financiamento negado ")