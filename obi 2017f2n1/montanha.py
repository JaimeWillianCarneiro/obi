tamanhoDaSequencia = int(input())
n = tamanhoDaSequencia
sequencia = list(map(int, input().split()))
pico =1


for i in range(1,n-1):
    if  sequencia[i-1] > sequencia[i] < sequencia[i+1]:
        pico +=1
        break

if pico==2:
    print("S")


else: print("N")