preco_kw = 0.12
icms = 0.18
quilowatts_consumidos = int(input("Digite o número de quilowatts consumidos: "))
valor_total = (quilowatts_consumidos * preco_kw) * (1 + icms)
print("O valor total a ser pago é: R$", valor_total)