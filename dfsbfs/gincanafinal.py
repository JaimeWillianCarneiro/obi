#  Solução Final gincana obi 2011
def bfs(grafo, inicio,visitados): 
     fila = [inicio] 
     visitados.add(inicio) 
     grupo = set([inicio]) 
     primeiroElemento = 0 
  
     while primeiroElemento < len(fila): 
         current_node = fila[primeiroElemento] 
         primeiroElemento += 1 
  
         for neighbor in grafo[current_node]: 
             if neighbor not in visitados: 
                 visitados.add(neighbor) 
                 fila.append(neighbor) 
                 grupo.add(neighbor) 
  
     return grupo 
  
def contar_grupos(grafo):
     visitados = set() 
     numerodegrupos = 0 
  
     for no in grafo: 
         if no not in visitados: 
             
             group = bfs(grafo, no, visitados) 
             numerodegrupos += 1 
             # print("Equipe", num_groups, ":", group) 
  
     return numerodegrupos 
  
  
  
  
 # Exemplo de um grafo não direcionado representado por um dicionário de listas de adjacências 


  
n,m = map(int, input().split()) 
  
  
 
grafo =  {i: [] for i in range(1, n+ 1)}
  
amizades =  [list(map(int, input().split())) for _ in range(m)] 
  
for i, j in amizades: 
     grafo[i].append(j) 
     grafo[j].append(i)
     

  
 # 
num_grupos = contar_grupos(grafo) 
print(num_grupos) 

