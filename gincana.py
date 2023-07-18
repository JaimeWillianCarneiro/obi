# n, m = map(int, input().split())


# listaDeAmizades = [ [int(i) for i in input().split()] for k in range(m)]


#  Como fazer infinito em python



infinito =  float('inf')
print(infinito)
# print(listaDeAmizades)


def dfs(graph, start):
    visited = set()  # Conjunto para armazenar os nós visitados
    
    stack = [start]  # Pilha para armazenar os nós a serem explorados

    while stack:
        vertex = stack.pop()  # Remove o último nó da pilha
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph[vertex]  # Obtém os vizinhos do nó atual
            stack.extend(neighbors - visited)  # Adiciona os vizinhos não visitados à pilha

    return visited

def dfs(x, lista, componente):
    # Percorremos por todos os vizinhos
    for v in lista[x]:
        if componente[v] == -1:  # Checamos se v ainda não foi visitado
            componente[v] = componente[x]
            dfs(v, lista, componente)
