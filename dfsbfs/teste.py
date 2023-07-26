def dfs_caminho(grafo, inicio, destino, visitados=None):
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

# Exemplo de uso:
grafo = [
    {2, 3},       # Vértice 1
    {1, 4},       # Vértice 2
    {1, 4},       # Vértice 3
    {2, 3, 5},    # Vértice 4
    {4},          # Vértice 5
]

inicio = 1
destino = 5

caminho = dfs_caminho(grafo, inicio, destino)

if caminho:
    print(f"O caminho entre {inicio} e {destino} é: {caminho}")
else:
    print(f"Não há caminho entre {inicio} e {destino}")
