consultadasMarcadsa = int(input())
n = consultadasMarcadsa
consultasPossiveis = 0
inicioAtend = None
fimAtend = None
for i in range(n):
    x,y = map(int, input().split())
    if inicioAtend== None and fimAtend==None:
        inicioAtend=x
        fimAtend = y
        consultasPossiveis+=1
    elif x>=fimAtend:
        fimAtend = y
        consultasPossiveis+=1


print(consultasPossiveis)
