k = int(input())
l = int(input())
fase = None
primeiroQuarto = list(range(1,5))
segundoQuarto = list(range(5,9))
terceiroQuarto = list(range(9,13))
quartoQuarto = list(range(13,17))
primeiraMetade = list(range(1, 9))
segundaMetade = list(range(9,17))
A =(k-1)%4
b = (l-1)%4

if min(k,l ) <= 8 and max(k, l)>8:
    fase = "final"

elif abs(k-l) == 1 and min(k,l )%2==1:
    fase = "oitavas"

elif abs(A-b)> 0:
    fase = "semifinais" 
else:
    fase = "quartas"

# elif (k in [1,2] and l in [3,4]) or  (l in [1,2] and k in [3,4]) :
#     fase = "quartas"
# elif ( k in [5, 6] and l in [7,8 ]) or  (l in [5, 6] and k in [7,8]):
#     fase = "quartas"

# elif (k in [9,10] and l in [11,12]) or  (l in [9,10] and k in [11,12]) :
#     fase = "quartas"
# elif ( k in [13, 14] and l in [15, 16 ]) or  (l in [ 13, 14] and k in [15, 16]):
#     fase = "quartas"

# elif (k in primeiroQuarto and l in segundoQuarto) or (l in primeiroQuarto and k in segundoQuarto):
#     fase = "semifinal"

# elif (k in terceiroQuarto and l in quartoQuarto) or (l in terceiroQuarto and k in quartoQuarto):
#     fase = "semifinal"
# elif (k in primeiraMetade and l in segundaMetade) or (l in primeiraMetade and k in primeiraMetade):
#     fase = "final"

print(fase)
