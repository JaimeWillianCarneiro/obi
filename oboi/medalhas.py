a, v = map(int, input().split())


tamanhoAzuis = [int(i) for i in input().split()]

tamanhoVermelho= [int(i) for i in input().split()]


tamanhos = tamanhoAzuis+ tamanhoVermelho
tamanhos = sorted(tamanhos)
tamanhoAzuis= sorted(tamanhoAzuis)
tamanhoVermelho = sorted(tamanhoVermelho)


v -=1
a-=1 

t = a+v +1
descartes = 0 

while True:

    
    if (tamanhos[t] == tamanhoAzuis[a] and tamanhos[t-1] == tamanhoVermelho[v])  or (tamanhos[t-1] == tamanhoAzuis[a] and tamanhos[t] == tamanhoVermelho[v]):
        break
    else:
     
        
        descartes+=1
        if tamanhos[t] ==tamanhoVermelho[v]:
            v-=1
           
            
        elif tamanhos[t] ==tamanhoAzuis[a]:
            a-=1
        t-=1
   

print(descartes)


