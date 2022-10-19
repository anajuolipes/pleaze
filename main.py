# este script armazena nomes e os divide em grupos

import random
import time
import utils

nomes = []
utils.nomes = nomes

while True:
    x = input("Insira o nome:\n")
    x = str(x)

    if x == "ok":
        break
    else:
        nomes.append(x)

print("Esses são todos os nomes na lista:\n" , nomes)
print("Deseja dividir os" , len(nomes) , "alunos em grupos de quantos?\n")
gruposde = input()
gruposde = int(gruposde)
qualgrupo = 1

while True:
    utils.qualgrupo = qualgrupo

    if qualgrupo * gruposde != len(nomes):
        utils.escolher(gruposde)
        qualgrupo += 1

    if len(nomes) == 1:
        print(nomes,"ficou sobrando")
        break







