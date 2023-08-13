# 30/100
N = int(input())


vidas  = [int(i) for i in input().split()]

numeroVidas = 0

for i in range(N):
    soma = vidas[i]
    for j in range(i+1, N):
        soma+=vidas[j]
        if soma > numeroVidas:
            numeroVidas=  soma



print(numeroVidas)