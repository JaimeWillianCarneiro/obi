n, m = map(int, input().split())

estradas = [set() for _ in range(n+1)]


pinturas=  [ ]
cores = [0]*n
for i in range(n-1):
    u,v = map(int, input().split())
    estradas[u-1].add(v)
    estradas[v-1].add(u)





def dfs_caminho(grafo, inicio, destino, visitados=None):
    # Criar um set para 
    if visitados is None:
        visitados = set()
    
    visitados.add(inicio)
    
    if inicio == destino:
        return [inicio]
    
    for vizinho in grafo[inicio - 1]:
        if vizinho not in visitados:
            caminho = dfs_caminho(grafo, vizinho, destino, visitados)
            if caminho:
                return [inicio] + caminho
    
    return None

for _ in range(m):
    p,q ,c =map(int, input().split())
    # pintura = (p,q,c )
    # pinturas.append(pintura)

    caminho = dfs_caminho(estradas, p,q)
    for  i in caminho:
        cores[i-1] = c




print(*cores)


