c = int(input())
lajotas =list(map(int, input().split()))

pulos = 0
ini = 0 
atual = ini
fim = c-1
eh_possivel = True
#  estrategia gulosa
while atual < fim:
    if atual <= (fim-2):
        
        if lajotas[atual+2] ==1:
            pulos +=1 
            atual+=2
        elif lajotas[atual+1]==1:
            pulos+=1
            atual +=1
        else:
            eh_possivel= False
            break
    else:
        if lajotas[atual+1] ==1:
            atual +=1
            pulos+=1
            break
        else:
            eh_possivel= False
            break
    

if eh_possivel:
    print(pulos)
else:
    print(-1)