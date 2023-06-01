n = int(input())
m = int(input())
s = int(input())
maiorValor = None


for i in range(m, n+1, -1):
    i = str(i)
    soma = 0
    for k in i:
        soma+=int(k)
    if soma==s:
        maiorValor = i
        break

if maiorValor==None:
    print(-1)
else: print(maiorValor)