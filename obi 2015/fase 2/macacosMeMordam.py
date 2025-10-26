quantidade_arvores = int(input())
arvores = []

for idx in range(quantidade_arvores):
    x, h = list(map(int, input().split()))
    arvores.append((x, h))
    


arvores.sort()
print(arvores)