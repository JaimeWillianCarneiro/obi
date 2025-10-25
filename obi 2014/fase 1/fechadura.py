n, m = list(map(int, input().split()))
entrada = list(map(int, input().split()))
n_total_movimentos = 0
for idx in range(len(entrada)-1):
    if entrada[idx] != m:
        n_movimentos =m-entrada[idx] 
        entrada[idx]+=n_movimentos
        entrada[idx+1]+=n_movimentos
        n_total_movimentos+=abs(n_movimentos)

print(n_total_movimentos)

        
    
    
    
