numeroDeRodadas = int(input())
n = numeroDeRodadas
vitoriasD = 0
vitoriasX = 0

for i in range(n):
    d, x = map(int, input().split())
    if d ==0:
        if x==1:
            vitoriasD+=1
        elif x==2:
            vitoriasD+=1
        elif x==3:
            vitoriasX+=1
        elif x==4:
            vitoriasX+=1
    elif d==1:
        if x==2 or x==3:
            vitoriasD+=1
        else:
            vitoriasX+=1
    elif d==2:
        if x==3 or x==4:
            vitoriasD+=1
        else:
            vitoriasX+=1
    elif d==3:
        if x==0 or x==4:
            vitoriasD+=1
        else:
            vitoriasX+=1
    elif d==4:
        if x==0 or x==1:
            vitoriasD+=1
        else: vitoriasX+=1

if vitoriasD>vitoriasX:
    print("dario")
else: print("xerxes")