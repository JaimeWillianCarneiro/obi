import heapq

def dijkstra(grafo, origem, destino):

    # Como não sabemos inicialmente as distâncias, atribuimos todas como Infinitas 
    distancias = {vertice: float('inf') for vertice in grafo}



    distancias[origem] = 0
    prioridade = [(0, origem)]
    print(prioridade)
    while prioridade:


        atual_dist, atual_vertice = heapq.heappop(prioridade) #  Remove o elemento de menor distância (o primeiro elemento do heap) 
                                                                #da fila de prioridade e atribui o valor da distância e do
        print(prioridade)                                                                #  vértice a atual_dist e atual_vertice, respectivamente.
        
        if atual_dist > distancias[atual_vertice]:
            continue

        if atual_vertice == destino:
    
            return distancias[atual_vertice]

        for vizinho, peso in grafo[atual_vertice].items():
            distancia = atual_dist + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(prioridade, (distancia, vizinho))



    
    return float('inf')

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
