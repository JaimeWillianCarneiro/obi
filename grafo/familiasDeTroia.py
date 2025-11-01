from collections import deque
MAXN = 50050


def dfs(x):
    # Percorremos por todos os vizinhos
    for v in lista[x]:
        if componente[v] == -1:  # Checamos se v ainda não foi visitado
            componente[v] = componente[x]
            dfs(v)






n, m = map(int, input().split())
adj = [[] for i in range(n+1)]
visitado = [False for i in range(n+1)]


def bfs(start, visitado):
    queue = deque([start])
    visitado[start] = True

    while queue: # enquanto a fila nao estiver vazia
        u = queue.popleft()

        for v in adj[u]:
            if visitado[v]==False:
                visitado[v] = 1
                queue.append(v)
    return visitado

componente = [-1] * (MAXN)


for i in range(m):
    a, b = map(int, input().split())
        # adicionamos cada um a lista do outro
    adj[a].append(b)
    adj[b].append(a)
    

num_componentes=0
for u in range(1, n+1):
    if visitado[u]==False:
        num_componentes +=1 
        visitado =bfs(u, visitado)    
print(num_componentes)

