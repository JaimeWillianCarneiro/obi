def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def count_families(N, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = {i: False for i in range(1, N + 1)}
    num_families = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(graph, i, visited)
            num_families += 1

    return num_families

if __name__ == "__main__":
    N , M = map(int, input().split())

    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))

    num_families = count_families(N, edges)
    print(num_families)
