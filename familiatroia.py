







def dfs(x):
    # Percorremos por todos os vizinhos
    for v in lista[x]:
        if componente[v] == -1:  # Checamos se v ainda não foi visitado
            componente[v] = componente[x]
            dfs(v)






n, m = map(int, input().split())

MAXN = 2*m
componente = [-1] * (MAXN)
lista = [[] for _ in range(MAXN)]

for i in range(m):
    a, b = map(int, input().split())
        # adicionamos cada um a lista do outro
    lista[a].append(b)
    lista[b].append(a)



numero_componentes = 0
for i in range(1, n + 1):
    if componente[i] == -1:  # i ainda não tem componente
            # começaremos uma dfs a partir de i
            # assim, i será o começo de uma nova componente
        numero_componentes += 1
        componente[i] = numero_componentes
        dfs(i)

print(numero_componentes)  # por fim, imprimimos a resposta



