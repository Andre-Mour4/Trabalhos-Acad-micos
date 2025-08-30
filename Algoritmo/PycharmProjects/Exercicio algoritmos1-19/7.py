candidato1 = 1
candidato2 = 2
candidato3 = 3
candidato4 = 4
voto_nulo = 5
voto_em_branco = 6
votocandidato1 = 0
votocandidato2 = 0
votocandidato3 = 0
votocandidato4 = 0
total_nulos = 0
total_brancos = 0
for i in range(20):
    voto = int(input(f"digite o voto{i+1}: "))
    if voto < 1 and voto >6:
        print("voto invalido")
    else:
        if voto == 1:
            votocandidato1 += 1
        if voto == 2:
            votocandidato2 += 1
        if voto == 3:
            votocandidato3 += 1
        if voto == 4:
            votocandidato4 += 1
        if voto == 5:
            total_nulos += 1
        if voto == 6:
            total_brancos += 1
print(f"votos candidato1: {votocandidato1}")
print(f"votos candidato2: {votocandidato2}")
print(f"votos candidato3: {votocandidato3}")
print(f"votos candidato4: {votocandidato4}")
print(f"votos nulos: {total_nulos}")
print(f"votos em branco: {total_brancos}")