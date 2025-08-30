codigo = int(input("Digite seu código: "))

if codigo < 101 or codigo > 106:
    print("Código invalido")
else:
    if codigo == 101:
        cargo = "vendedor"
    else:
        if codigo == 102:
            cargo = "atendente"
        else:
            if codigo == 103:
                cargo = "auxiliar tecnico"
            else:
                if codigo == 104:
                    cargo = "assistente"
                else:
                    if codigo == 105:
                        cargo = "coordenador de grupo"
                    else:
                        cargo = "gerente"

    print("Seu cargo é " , cargo)