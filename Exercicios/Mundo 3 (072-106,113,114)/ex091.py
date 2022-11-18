from random import randint as ri
from operator import itemgetter
import time
jogadores = {}
for j in range(0, 4):
    jogadores['Jogador '+str(j+1)] = int(ri(1,6))
print(jogadores)

ranking = []
for k, v in jogadores.items():
    print(f'{k} tirou {v}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    time.sleep(1)



