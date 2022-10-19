import random

def escolher(n):
    n = int(n)
    count = 0
    escolhidos = []

    while True:
        if n == len(escolhidos):
            break   

        else:
            escolhida = random.choice(nomes)
            escolhidos.append(escolhida)
            nomes.remove(escolhida)




    print( qualgrupo,"º grupo é:" ,escolhidos)