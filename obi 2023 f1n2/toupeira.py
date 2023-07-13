#  necessario
s, t = map(int, input().split())


possiveis = 0 

 

tuneis = [[] for i in range(s)]








for _ in range(t):
    x, y = map(int, input().split())
    
    tuneis[x-1].append(y)
    tuneis[y-1].append(x)

# muitos fors





p = int(input())

possiveis = 0 



for _ in range(p):
    caminho = 1
    
    sugestao1 = list(map(int, input().split()))
    tam = sugestao1[0]
    sugestao = sugestao1[1:]


    
    for x in range(tam-1):
        
        if sugestao[x]  in tuneis[sugestao[x+1]-1]:
            caminho +=1
        else:
            break 


    if caminho == tam:
         possiveis +=1




print(possiveis)










