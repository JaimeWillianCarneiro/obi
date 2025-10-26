
tamanho = int(input())
espacos_disponiveis_gb = [8*1024, 4*1024, 2*1024,1024, 512, 256, 128, 64, 32, 16, 8,4,2,  1]


quantidade_total = 0 


for equipamento in espacos_disponiveis_gb:
    if tamanho >=equipamento:
        quantidade = tamanho//equipamento
        quantidade_total+=quantidade
        tamanho %=equipamento


print(quantidade_total)