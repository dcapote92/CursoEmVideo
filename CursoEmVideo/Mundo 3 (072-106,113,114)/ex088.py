import time
from random import randint as ri
print('Mega Sena')
print('*' * 100)
mega = int(input('Quantos  jogos você quer que eu sorteie?: '))
megasena = []
for m in range(mega):
    jogo = []
    for j in range(6):
        jogo.append(ri(1, 60))
    megasena.append(jogo)

for m in range(mega):
    print(f'Jogo {m+1}: {megasena[m]}')
    time.sleep(1)
