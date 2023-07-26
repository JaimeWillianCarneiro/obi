ordem = int(input())
n = ordem
linhas = []
for x in range(n):
    linha = list(map(int, input().split()))
    linhas.append(linha)

for i in range(1, n):
    for j in range(1, n):
        elem = linhas[i][j]
        vizinhas = [linhas[i - 1][j - 1], linhas[i - 1][j], linhas[i][j - 1]]
        if vizinhas.count(1) > vizinhas.count(0):
            linhas[i][j] = 0
        else:
            linhas[i][j] = 1
print(linhas[n-1][n-1])