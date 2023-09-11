e, d = map(int, input().split())

esquerda = [int(i) for i in input().split()]
direita = [int(i) for i in input().split()]

l = 0
r = d-1

anilhas = 0
somaEsquerda = sum(esquerda)  # Alteração 1: Calcular a soma de esquerda
somaDireita = sum(direita)    # Alteração 2: Calcular a soma de direita

while True:


    if somaEsquerda == somaDireita:
        
        # anilhas = l + d- (r+1) 
        break
    else:
     

        if somaEsquerda >somaDireita :  # Alteração 3: Correção da condição
            somaEsquerda -= esquerda[l]
            l += 1
            anilhas +=1
            
        else:
   
            
            somaDireita -= direita[r]
            anilhas+=1 
            
            r -= 1
        #else:
            # if len(direita) > len(esquerda):

print(anilhas)
