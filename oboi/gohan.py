n= int(input())

notas = [list(map(int, input().split())) for _ in range(n)]


notaH, notaP = 0, 0 

for nota in notas:
    notaP+= nota[0]
    notaH+=nota[1]



if notaH> notaP:
    print(":0 <- Gohan e Feijao")
elif notaH< notaP:
    print(":0 <-X- Gohan e Feijao")
else:
    print("impasse")