valorInicialDaDiaria = int(input())
aumentoDaDiaria = int(input())
diaDaChegada = int(input())
valorTotal = 0

if diaDaChegada<16:
    valorTotal = (32- diaDaChegada) *(valorInicialDaDiaria + (aumentoDaDiaria)*(diaDaChegada-1))
else:
    valorTotal = (32-diaDaChegada) *(valorInicialDaDiaria + (aumentoDaDiaria)*14)
print(valorTotal)

