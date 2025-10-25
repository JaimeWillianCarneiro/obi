n = int(input())
entrada = list(map(int, input().split()))
esquerda = 0
soma_esquerda = entrada[esquerda]

direita = n-1
soma_direita = entrada[direita]
operacoes = 0

while esquerda < direita:
    if soma_esquerda == soma_direita:
        esquerda+=1
        direita-=1
        soma_direita = entrada[direita]
        soma_esquerda = entrada[esquerda]
    elif soma_esquerda <soma_direita:
        esquerda +=1
        soma_esquerda+=entrada[esquerda]
        operacoes +=1
    else:
        direita-=1
        soma_direita += entrada[direita]
        operacoes+=1
        

print(operacoes)
