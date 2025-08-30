mes = int(input("Digite o número do mês: "))

if mes == 1:
    nome_mes = "Janeiro"
else:
    if mes == 2:
        nome_mes = "Fevereiro"
    else:
        if mes == 3:
            nome_mes = "Março"
        else:
            if mes == 4:
                nome_mes = "Abril"
            else:
                if mes == 5:
                    nome_mes = "Maio"
                else:
                    if mes == 6:
                        nome_mes = "Junho"
                    else:
                        if mes == 7:
                            nome_mes = "Julho"
                        else:
                            if mes == 8:
                                nome_mes = "Agosto"
                            else:
                                if mes == 9:
                                    nome_mes = "Setembro"
                                else:
                                    if mes == 10:
                                        nome_mes = "Outubro"
                                    else:
                                        if mes == 11:
                                            nome_mes = "Novembro"
                                        else:
                                            if mes == 12:
                                                nome_mes = "Dezembro"
                                            else:
                                                nome_mes = "Mês inválido"

print(nome_mes)