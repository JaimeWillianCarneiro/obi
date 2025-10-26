tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
eh_valido = True
n = int(input())
for navio in range(n):
    d, l, r, c = list(map(int, input().split()))
    posicoe_para_marcar = []
    if eh_valido:
        for i in range(l):
                #  ta na horizontal
                if d==0:
                    linha_atual, coluna_atual = r,c + i
                else: 
                    linha_atual, coluna_atual= r+i, c
                if linha_atual >10 or coluna_atual>10:
                    # print("caso 1")
                    # print("N")
                    eh_valido = False
                    break
                if tabuleiro[linha_atual-1][coluna_atual-1]==1:
                    # print("caso 2")
                    # print("N")
                    eh_valido = False
                    break
                
                posicoe_para_marcar.append((linha_atual-1, coluna_atual-1))
        for x, y in posicoe_para_marcar:
            tabuleiro[x][y] = 1
    
if eh_valido:
    print("Y")
else:
    print("N")
             
        