def bfs(graph, start):
    # Inicializar a fila com o nó inicial e marcar como visitado
    queue = [start]
    visited = set([start])
    
    while queue:
        # Retira o primeiro nó da fila
        current_node = queue.pop(0)
        print("Visitando o nó:", current_node)
        
        # Explora os vizinhos do nó atual
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Adiciona vizinhos não visitados à fila e marca como visitado
                queue.append(neighbor)
                visited.add(neighbor)

# Exemplo de um grafo representado por um dicionário de listas de adjacências
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Chamar a função BFS com o nó inicial 'A'
bfs(graph, 'A')



