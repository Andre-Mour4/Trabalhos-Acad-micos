soma_precos_antigos = 0
soma_precos_novos = 0
quantidade = 0
codigo = 0
while codigo >= 0:
   codigo = int(input("Digite o código do produto: "))
   if codigo >= 0:
       preco_antigo = float(input("Digite o preço do produto: "))
       soma_precos_antigos += preco_antigo
       quantidade += 1
       preco_novo = preco_antigo * 1.2
       soma_precos_novos += preco_novo
       print("Código:", codigo)
       print("Preço novo:", preco_novo)

if quantidade > 0:
   media_precos_antigos = soma_precos_antigos / quantidade
   media_precos_novos = soma_precos_novos / quantidade
   print("Média dos preços antigos:", media_precos_antigos)
   print("Média dos preços novos:", media_precos_novos)
else:
   print("Nenhum produto foi cadastrado.")
