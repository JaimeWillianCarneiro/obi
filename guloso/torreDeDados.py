n = int(input())

dados= []


for _ in range(n):
    entrada_linha = list(map(int, input().split()))
    
    dados.append(entrada_linha)


primeiro_dado = dados[0]

# A, B, C, D, E, F
# A <-> F
#  B<-> D
#  C<> E
face_oposta= {0: 5, 1:3, 2:4,5:0, 3:1, 4:2  }


def ver_maximo_sem_indices(baixo, cima):
    maximo = 0
    
    for face in range(1, 7):
        if face not in [baixo, cima]:
            maximo = max(face, maximo)
    
    return maximo
soma_maxima =0


for baixo_idx in range(6):
    soma_estado_atual = 0
    face_baixo = primeiro_dado[baixo_idx]
    face_cima = primeiro_dado[face_oposta[baixo_idx]]
    
    # print(f"face de baixo inicial: {}")
    # print(face_baixo, face_cima)
    for dado_idx in range(n):
        if dado_idx==0:
            soma_estado_atual+= ver_maximo_sem_indices(face_baixo, face_cima)
        else:
            face_baixo = face_cima
            face_baixo_idx = dados[dado_idx].index(face_baixo)
            face_cima = dados[dado_idx][face_oposta[face_baixo_idx]]
            soma_estado_atual+=ver_maximo_sem_indices(face_baixo, face_cima)
    
    
    soma_maxima = max(soma_maxima, soma_estado_atual)

print(soma_maxima)

            
            