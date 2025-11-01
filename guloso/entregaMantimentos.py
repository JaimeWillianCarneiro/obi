n  = int(input())

pontos =[]


for i in range(n):
    x, y = map(int, input().split())
    ponto  = (x, y)
    pontos.append(ponto)
    
pontosOrdenadoX = sorted(pontos)
pontosOrdenadoY = sorted(pontos, key=lambda value: value[1] )
a = pontosOrdenadoX[n//2][0]
b = pontosOrdenadoY[n//2][1]

print(a, b)
