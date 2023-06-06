m,n = map(int, input().split())



matriz = []




for i in range(m):
    linha = list(map(int, input().split()))
    matriz.append(linha)



p = int(input())

vendidas = 0

for x in range(p):
    i, j = map(int, input().split())
    if matriz[i-1][j-1]  > 0:
        vendidas +=1
        matriz[i-1][j-1] -=1
     



print(vendidas)
# print(matriz)