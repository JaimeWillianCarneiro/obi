N = int(input())
valor = N
S_ordenada_dec  = [100, 50, 25, 10, 5,1]
quantidade_total  =0

for moeda in S_ordenada_dec:
    if N >= moeda:
        quantidade= valor//moeda
        quantidade_total += quantidade
        valor%=moeda


print(quantidade_total)
    

