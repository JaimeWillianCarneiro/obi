e, d = map(int, input().split())


esquerda = [int(i) for i in input().split()]
direita = [int(i) for i in input().split()]


l = e -1
r = 0


anilhas = 0 
somaEsquerda = esquerda[-1]
somaDireita = direita[0]

ok = False

while not ok:
    if somaEsquerda== somaDireita:
    

        anilhas = l+1 + (d-(r+1))-1
        ok = True
    else:
    
        if esquerda[l] < direita[r]:
            l-=1
            somaEsquerda+= esquerda[l]
            
        else:
            r+=1
            somaDireita+= direita[r]
            


print(anilhas)


"""
3 3
1 7 1
8 4 1
"""
            

