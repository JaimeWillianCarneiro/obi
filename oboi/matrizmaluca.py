n, m , p = [int(i) for i in input().split()]


matriz = [[int(i) for i in input().split()] for _ in range(n)]
pontosEnzo = 0 
pontosLobo = 0 

for _  in range(p):
    pontos = 0 

    l, c = map(int, input().split()) 

    # adicionar  elementos da linha
    for i in range(m):
        pontos+=matriz[l-1][i]
        matriz[l-1][i] = 0 

    for j in range(n):
        pontos+= matriz[j][c-1]
        matriz[j][c-1] = 0 

    
    pontos-= matriz[l-1][c-1]

    if i%2==1:
        pontosEnzo+= pontos
    else:
        pontosLobo+=pontos


if pontosEnzo > pontosLobo:
    print("Enzo")
elif pontosEnzo < pontosLobo:
    print("Lobo")
else:
    print("Empate")
