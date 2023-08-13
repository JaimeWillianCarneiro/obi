n, m = map(int, input().split())

mapa = [[0 for _ in range(m)] for _ in range(n)]



for i in range(n):
    linha= list(map(int, input().split()))
    

    for j in range(m):
        if linha[j]==2:
            mapa[i][j] = 2
            iniX, iniY= i, j
        elif linha[j]==3:
            mapa[i][j] = 3
        elif linha[j]==1:
            mapa[i][j] = 1
        

x = 0 
y = 0 

# mapa.append([0 for _ in range(m + 1)])


x, y = iniX, iniY

passos = 1


ok = False
while not ok:
                              
    
    if  x + 1< n  and mapa[x+ 1][y]==1:
        # print(iniX+1, iniY)
        
        mapa[x][y]= -1
        x+=1
        passos+=1
        
    elif mapa[x-1][y]==1 and x >= 1 :
        # print(iniX-1, iniY)
   
        mapa[x][y]= -1

        x-=1
        passos+=1
        
    

    elif mapa[x][y-1]==1 and y >=1:
     
        mapa[x][y]= -1

        y-=1
        passos+=1


    elif mapa[x][y+1]==1 and y+1 <m :
       
        mapa[x][y]= -1


        y+=1
        passos+=1
        
    elif (x + 1< n  and mapa[x+ 1][y]==3) or( mapa[x-1][y]==3 and x >= 1) or (mapa[x][y-1]==3 and y >=1) or(mapa[x][y+1]==3 and y+1 <m):
        ok = True
      
    else:
        x, y = iniX, iniY
        passos = 1

        
        
        
       
        
passos+=1

print(passos)
