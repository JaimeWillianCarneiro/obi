a, v = map(int, input().split())


tamanhoAzuis = [int(i) for i in input().split()]

tamanhoVermelho= [int(i) for i in input().split()]


tamanhos = tamanhoAzuis+ tamanhoVermelho
tamanhos = sorted(tamanhos)
tamanhoAzuis= sorted(tamanhoAzuis)
tamanhoVermelho = sorted(tamanhoVermelho)


descartes = 0 
while True:
    if (tamanhos[-1] == tamanhoAzuis[-1] and tamanhos[-2] == tamanhoVermelho[-1])  or (tamanhos[-2] == tamanhoAzuis[-1] and tamanhos[-1] == tamanhoVermelho[-1]):
        break
    else:
        if tamanhos[-1] ==tamanhoVermelho[-1]:
            tamanhoVermelho.remove(tamanhos[-1])
            tamanhos.pop(-1)
            descartes+=1
        elif tamanhos[-1] ==tamanhoAzuis[-1]:
            tamanhoAzuis.remove(tamanhos[-1])
            tamanhos.pop(-1)


print(descartes)

