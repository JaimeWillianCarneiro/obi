def bfs(graph, start, visited):
    queue = [start]
    visited.add(start)
    group = set([start])
    front = 0

    while front < len(queue):
        current_node = queue[front]
        front += 1

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                print(neighbor)
                visited.add(neighbor)
                queue.append(neighbor)
                group.add(neighbor)

    return group

def count_friend_groups(graph):
    visited = set()
    num_groups = 0

    for node in graph:
        print(node)
        if node not in visited:
            group = bfs(graph, node, visited)
            num_groups += 1
            print("Equipe", num_groups, ":", group)

    return num_groups

# Exemplo de um grafo não direcionado representado por um dicionário de listas de adjacências
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Dave'],
    'Charlie': ['Alice', 'Dave'],
    'Dave': ['Bob', 'Charlie'],
    'Eva': ['Frank'],
    'Frank': ['Eva']
}

num_teams = count_friend_groups(graph)
print("Total de equipes:", num_teams)
print(graph)