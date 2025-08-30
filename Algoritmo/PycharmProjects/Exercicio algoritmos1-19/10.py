n = int(input("digite o valor de n: "))
fatorial = 1
for i in range(1,n + 1):
    for j in range(1):
        fatorial *= i
    print(f"{i},{i}!={fatorial}")