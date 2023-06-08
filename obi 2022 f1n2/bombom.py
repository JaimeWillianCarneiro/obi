naipeDominante = None
somaLuana = 0
somaEdu = 0

for i in range(7):
    descricao = input()
    if i==0:
        naipeDominante= descricao[1]

    if i==1 or i==2 or i==3:
        if descricao[1]==naipeDominante:
            if descricao[0] ==  "A":
                somaLuana+=14
            elif descricao[0]== "J":
                somaLuana+=15
            elif descricao[0] == "Q":
                somaLuana+= 16
            else: somaLuana+=17
        else:
            if descricao[0] ==  "A":
                somaLuana+=10
            elif descricao[0]== "J":
                somaLuana+=11
            elif descricao[0] == "Q":
                somaLuana+= 12
            else: somaLuana+=13

    elif i>3:
        if descricao[1] == naipeDominante:
            if descricao[0] == "A":
                somaEdu += 14
            elif descricao[0] == "J":
                somaEdu += 15
            elif descricao[0] == "Q":
                somaEdu += 16
            else:
                somaEdu += 17
        else:
            if descricao[0] == "A":
                somaEdu += 10
            elif descricao[0] == "J":
                somaEdu += 11
            elif descricao[0] == "Q":
                somaEdu += 12
            else:
                somaEdu += 13

if somaLuana>somaEdu:
    print("Luana")
elif somaLuana<somaEdu:
    print("Edu")
else: print("empate")

