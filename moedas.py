valor = 43


moedas = [1,2, 3, 5, 10, 25]





memo =[ [-1 for _ in range(len(moedas)+1)] for i in range(valor+1)]



#  Solução topdown
def solve(x, i):
    print(x, i)
    if memo[x][i] != -1: # se ja foi resolvido
        return memo[x][i]
    if i>= len(moedas): #caso base: não temos moedas disponivel
        if x==0:
            return True
        else:
            return False
        
    # ans =0
    
    if moedas[i] > x:
        memo[x][i]=  solve(x, i+1)
    else:
        memo[x][i] =  solve(x-moedas[i], i+1)  or solve(x, i+1)

    return memo[x][i]


resposta  = solve(valor, 0)

print(resposta)
        