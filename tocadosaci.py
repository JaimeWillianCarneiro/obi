n, m = map(int, input().split())

mapa = [[0 for _ in range(m)] for _ in range(n)]

iniX = 0
iniY= 0
xF = 0 
yF = 0 


for i in range(n):
    linha= list(map(int, input().split()))
    

    for j in range(m):
        if linha[j]==2:
            mapa[i][j] = 2
            iniX, iniY= i, j
        elif linha[j]  ==3:
            xF, yF= i, j
        elif linha[j]==1:
            mapa[i][j] = 1
        


mapa.append([0 for _ in range(m + 1)])


x, y = iniX, iniY

passos = 1



while True:
                                   # segue Hermione
    
    if mapa[iniX+1][iniY]==1 and x < m:
        print(iniX+1, iniY)
        
        mapa[iniX][iniY]= -1
        iniX,iniY=iniX+1,iniY
        passos+=1
        
    elif mapa[iniX-1][iniY]==1 and iniX >= 0 :
        print(iniX-1, iniY)
        mapa[iniX][iniY]= -1

        iniX,iniY=iniX-1,iniY
        passos+=1
        
    elif mapa[iniX][iniY+1]==1 and y+1 <m :
        print(iniX, iniY+1)
        mapa[iniX][iniY]= -1


        iniX,iniY=iniX,iniY+1
        passos+=1

    elif mapa[iniX][iniY-1]==1 and iniY >=0:
        print(iniX, iniY-1)
        mapa[iniX][iniY]= -1

        iniX,iniY=iniX,iniY-1
        passos+=1
        
    elif mapa[iniX][iniY-1]==3 or mapa[iniX][iniY+1]==3 or mapa[iniX-1][iniY]==3 or  mapa[iniX+1][iniY]==3:
        break
    else:
        passos = 1
        iniX,iniY= x, y  
       
        
passos+=1

print(passos)