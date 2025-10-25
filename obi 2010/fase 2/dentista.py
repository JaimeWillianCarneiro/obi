consultadasMarcadsa = int(input())
n = consultadasMarcadsa
start  =[]
end  =[]
for tarefa in range(n):
    ini, fim = list(map(int, input().split()))
    start.append(ini)
    end.append(fim)
def agendamento_de_tarefa(start: list, end: list):
    tarefas_a_serem_alocadas =[]
    n_tarefas_alocadas  =0
    n_tarefas = len(start)
    #  Agrupando as tarefas
    tarefas_ordenada = []
    for idx in range(n_tarefas):
        tarefa = ( start[idx], end[idx])
        tarefas_ordenada.append(tarefa)
    tarefas_ordenada.sort(key= lambda item: item[1])
    
    
    tarefas_a_serem_alocadas.append(tarefas_ordenada[0])  
    n_tarefas_alocadas+=1
    
    for tar_idx in range(1, len(tarefas_ordenada)):
        if tarefas_ordenada[tar_idx][0]>=tarefas_a_serem_alocadas[-1][1]:
            tarefas_a_serem_alocadas.append(tarefas_ordenada[tar_idx])
            n_tarefas_alocadas+=1

    
    return n_tarefas_alocadas


print(agendamento_de_tarefa(start, end))
        
