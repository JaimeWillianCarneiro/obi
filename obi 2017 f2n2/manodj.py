def dijkstra(grafo, origem, destino):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    visitados = set()

    while True:
        # Encontrar o vértice não visitado com a menor distância
        vertice_atual = None
        menor_distancia = float('inf')
        for vertice, distancia in distancias.items():
            if vertice not in visitados and distancia < menor_distancia:
                vertice_atual = vertice
                menor_distancia = distancia

        if vertice_atual is None:
            break

        visitados.add(vertice_atual)

        # Atualizar as distâncias dos vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual].items():
            if vizinho not in visitados:
                distancia = distancias[vertice_atual] + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia

    return distancias[destino]

# Exemplo de uso:
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 8},
    'D': {'B': 10, 'C': 3, 'E': 7},
    'E': {'C': 8, 'D': 7}
}

# Encontre o menor caminho entre os vértices 'A' e 'D'
origem = 'A'
destino = 'D'
menor_caminho = dijkstra(grafo, origem, destino)

if menor_caminho != float('inf'):
    print(f"Menor caminho entre '{origem}' e '{destino}' é: {menor_caminho}")
else:
    print(f"Não há caminho entre '{origem}' e '{destino}' no grafo.")
