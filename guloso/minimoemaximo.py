somaDosDigitos = int(input())
s = somaDosDigitos
a = int(input())
b = int(input())

numerosDesejados = []

for i in range(a, b +1):
    i = str(i)
    soma=0
    for k in i:
        k = int(k)
        soma+=k
        if soma>somaDosDigitos:
            break
    if soma== somaDosDigitos:
        numerosDesejados.append(i)

numerosDesejados.sort()
print(numerosDesejados[0])
print(numerosDesejados[len(numerosDesejados)-1])