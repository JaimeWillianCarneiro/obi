# Recebendo as entradas
e, d = map(int, input().split())

esquerda = [int(i) for i in input().split()]
direita = [int(i) for i in input().split()]

l = 0 # ponteiro representando a anilha da extremidade esquerda
r = d-1 # ponteiro representando a anilha da extremidade direita

anilhasRetiradas = 0
somaEsquerda = sum(esquerda)  # Alteração 1: Calcular a soma inicial do lado esquerdo
somaDireita = sum(direita)    # Alteração 2: Calcular a soma inicial do lado direito

while True:

    # Se o lado direito e o esquerdo estiverem com o msm peso, encerramos a execução
    if somaEsquerda == somaDireita:
        
        # anilhas = l + d- (r+1) 
        break
    else:
     

        if somaEsquerda >somaDireita :  # Alteração 3: Correção da condição
            somaEsquerda -= esquerda[l]
            l += 1
            anilhasRetiradas +=1
            
        else:
   
            
            somaDireita -= direita[r]
            anilhasRetiradas+=1 
            
            r -= 1
        #else:
            # if len(direita) > len(esquerda):

print(anilhas)
