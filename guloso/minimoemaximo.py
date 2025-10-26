somaDosDigitos = int(input())
# s = somaDosDigitos
a = int(input())
b = int(input())

numerosDesejados = []
minimo = None
maximo = None
for i in range(a, b +1):
    i = str(i)
    soma=0
    for k in i:
        k = int(k)
        soma+=k
        if soma>somaDosDigitos:
            break
    if soma== somaDosDigitos:
        if not minimo:
            minimo = i
            maximo = i 
        else:
            maximo = i


print(minimo)
print(maximo)