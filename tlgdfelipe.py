n, m = map(int, input().split())


interacoes = [list(map(int, input().split())) for _ in range(m)]



pontes = [ set() for _ in range(n+1)]


for tipo, a, b in interacoes:
    if tipo==0:
        if a in pontes[b]:
            print(1)
        else:
            print(0)
    else:
        pontes[a].add(b)
        pontes[b].add(a)