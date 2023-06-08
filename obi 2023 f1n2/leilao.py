n  = int(input())
maiorLance  = 0 
Ganhador = None

for x in range(n):
    nome = input()
    lance = int(input())


    
    if lance > maiorLance:
        maiorLance = lance
        Ganhador = nome








print(Ganhador)
print(maiorLance)