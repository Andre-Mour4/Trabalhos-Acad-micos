salariobruto = int(input("Digite seu salario bruto: "))
quantidadehorasextra = int(input("Digite o quantidade de horas extras: "))
valorhoraextra = int(input("Digite o valor da hora extra: "))
horaextra = quantidadehorasextra * valorhoraextra
salarionovo = horaextra + salariobruto
Desconto = salarionovo * 8/100
salarioliquido = salarionovo - Desconto
print("Salario Liquido é: " , salarioliquido,)




