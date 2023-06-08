numeroDemedicoes = int(input())
somaDesejada = int(input())
n = numeroDemedicoes
medicoes = list(map(int, input().split()))
intervalosDesejados = 0
for i in range(n):
    soma = medicoes[i]
    if medicoes[i]== somaDesejada:
        intervalosDesejados+=1

    if soma<=somaDesejada:
        for k in range(i+1, n):
            soma+= medicoes[k]
            if soma== somaDesejada:
                intervalosDesejados+=1
            elif soma>somaDesejada:
                break
print(intervalosDesejados)

