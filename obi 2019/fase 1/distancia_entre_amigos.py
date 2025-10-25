n = int(input())
andaresDeCadaPredio = list(map(int, input().split()))

max_distancia_total = 0
max_valor_passado = andaresDeCadaPredio[0]-0

# A[j] + A[i] + j-1 = (A[j] + j) + (A[i]-i) 
for j in range(1, n):
    #  a distancia maxima de sair desse predio é fixa
    
    dist_atual = andaresDeCadaPredio[j] + j + max_valor_passado
    max_distancia_total = max(max_distancia_total, dist_atual)
    max_valor_passado = max(max_valor_passado, andaresDeCadaPredio[j] - j)
    

print(max_distancia_total)

        