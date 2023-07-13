n, m = [int(i) for i in input().split()]

adj = [[False for _ in range(n)] for _ in range(n)]

res = []
for _ in range(m):
    i = [int(i) for i in input().split()]
    
    if i[0] == 0:
        if adj[i[1]-1][i[2]-1]: res.append(1)
        else: res.append(0)
    else:
        adj[i[1]-1][i[2]-1] = True
        adj[i[2]-1][i[1]-1] = True

for i in res: print(i)