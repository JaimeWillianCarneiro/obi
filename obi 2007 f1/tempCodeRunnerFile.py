n = int(input())
tabela =[]

soma_ideal = 0
soma_colunas = [0 for _ in range(n)]
soma_diagonais = [0, 0]
soma_linhas = [0 for _ in range(n)] #acho que não precisa
eh_magico = True

for linha in range(n):
    linha_entrada = list(map(int, input().split()))
    
    soma_linha = 0 
    tabela
    if eh_magico:
        if linha == 0:
            # primeira linha 
            for elem_idx in range(n):
                if elem_idx ==0:
                    soma_diagonais[0] +=linha_entrada[0]
                if elem_idx ==(n-1):
                    soma_diagonais[1] +=linha_entrada[n-1]
                soma_linha+=linha_entrada[elem_idx]
                
                soma_colunas[elem_idx]+=linha_entrada[elem_idx]
                if elem_idx==0:
                    soma_colunas[0]+=linha_entrada[elem_idx]
                if elem_idx==(n-1):
                    soma_colunas[1]+=linha_entrada[elem_idx]
                    
            soma_ideal = soma_linha
        else:
            for elem_idx in range(n):
                soma_linha+= linha_entrada[elem_idx]
                if soma_linha> soma_ideal:
                    eh_magico  =False
                    break
                    
                soma_colunas[elem_idx]+=linha_entrada[elem_idx]
                if elem_idx==linha:
                    # somando na diagonal principal
                    soma_diagonais[0]+=linha_entrada[elem_idx]
                    if soma_diagonais[0] >soma_ideal:
                        eh_magico=False
                        break
                    
                    
                
                if elem_idx + linha ==(n-1):
                    # somando na diagonal secundária
                    soma_diagonais[1]+=linha_entrada[elem_idx]
                    if soma_diagonais[1] >soma_ideal:
                        eh_magico=False
                        break
            
            if soma_linha != soma_ideal:
                eh_magico =False

if soma_diagonais[0] != soma_diagonais[1] or soma_ideal !=soma_diagonais[0]:
    eh_magico =False
for soma in soma_colunas:
    if soma!=soma_ideal:
        eh_magico = False
    
                



if eh_magico:
    print(soma_ideal)
else:
    print(-1)
        
            
            
        
        




