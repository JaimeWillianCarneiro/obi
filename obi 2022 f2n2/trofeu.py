pontuacoes = [int(input()) for i in range(5)]

diferentes = set(pontuacoes)

trofeus = 0 
placas = 0 
if len(diferentes)== len(pontuacoes):
    trofeus, placas = 1,1
elif len(diferentes)==1:
    trofeus, placas = 5,0
else:
    diferentes = list(diferentes)
    diferentes = sorted(diferentes)

    trofeus = pontuacoes.count(diferentes[-1])
    placas = pontuacoes.count(diferentes[-2])


print(trofeus, placas)