v = int(input())

a = int(input())

f = int(input())

p = int(input())

maiorNumero = " nn vriou"

dividas = [ a, f, p]
dividas = sorted(dividas)

# print(sum(dividas[0:2]))
if sum(dividas) <=v:
    maiorNumero= 3



elif sum(dividas) > v:
    if v  < dividas[0]:
        maiorNumero = 0 
    elif   v< sum(dividas[0:2]) :
        maiorNumero= 1
    elif  v > sum(dividas[0:2]):


        maiorNumero =2

        



print(maiorNumero)


