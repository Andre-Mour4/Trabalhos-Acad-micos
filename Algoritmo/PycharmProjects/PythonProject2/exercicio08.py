ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

print("Você tem " , idade , "anos")

if idade <= 3:
    print("bebê")
else:
    if idade <= 11:
        print("criança")
    else:
        if idade <= 17:
            print("adolescente")
        else:
            if idade <= 64:
                print("adulto")
            else:
                print("idoso")


