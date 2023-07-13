n, r = [int(i) for i in input().split()]

adj = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(r):
    x, y = [int(i)-1 for i in input().split()]
    
    adj[x][y] = 1
    adj[y][x] = 1

total = 0

for l in adj:
    total += sum(l)

print((n*n-n-total)/2)
