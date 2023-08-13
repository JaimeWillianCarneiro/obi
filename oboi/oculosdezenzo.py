n,e, d = map(int, input().split())


graus= [list(map(int, input().split())) for _ in range(n)]
pontuacao = 100000
for oculos in graus:
    if (abs(oculos[0] - e) + abs(oculos[1]-d)) < pontuacao:
        pontuacao =  (abs(oculos[0] - e) + abs(oculos[1]-d))

    
print(pontuacao)
