s, t, p = [int(i) for i in input().split()]
alturas = [int(i) for i in input().split()]
adj = [[False for _ in range(s)] for _ in range(s)]

print(alturas)

for _ in range(t):
    i, j = [int(i)-1 for i in input().split()]
    # print(adj[i])
    if alturas[i] > alturas[j]: 
        adj[i][j] = True
    elif alturas[j] > alturas[i]:
        adj[j][i] = True
        
    # print(adj[i])
        

for x in range(adj[p-1]):
    if x:
        


