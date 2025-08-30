contador = 0
numero = 1
while contador < 3:
   soma = 0
   for i in range(1, numero):
       if numero % i == 0:
           soma += i
   if soma == numero:
       print(numero, "é um número perfeito")
       contador += 1
   numero += 1