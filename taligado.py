n, m = [int(i) for i in input().split()]

adj = [[False for _ in range(n + 1)] for _ in range(n + 1)]


for _ in range(m):
    i = [int(i) for i in input().split()]
    
    if i[0] == 0:
        print(1 if adj[i[1]][i[2]] else 0)
    else:
        adj[i[1]][i[2]] = True
        adj[i[2]][i[1]] = True

