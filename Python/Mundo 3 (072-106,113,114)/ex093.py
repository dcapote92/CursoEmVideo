jogador = dict()
jogador['nome'] = input('Digite seu nome: ')
partidas = int(input('Quantos partidos jogou?: '))
gols = []
for p in range(0, partidas):
    gols.append(int(input(f'\tQuantos gols na partida {p+1} ?: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
aproveitamiento = float((jogador['total'] * 100)/partidas)
jogador['aproveitamento'] = round(aproveitamiento,2)
print(jogador)
for k, v in jogador.items():
    print(f'{k}: {v}')
print(f'Aproveitamento de {jogador["aproveitamento"]}% baseados em gols per partida.')