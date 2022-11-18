jogadores = list()
while True:
    jogador = dict()
    jogador['nome'] = input('Digite seu nome: ')
    partidas = int(input('Quantos partidos jogou?: '))
    gols = []
    for p in range(0, partidas):
        gols.append(int(input(f'\tQuantos gols na partida {p + 1} ?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    aproveitamiento = float((jogador['total'] * 100) / partidas)
    jogador['aproveitamento'] = round(aproveitamiento, 2)
    jogadores.append(jogador.copy())
    c = input('Quer continuar?: [S/N] ')
    if c in 'Nn':
        break
print(jogadores)
print('Jogador\t Partidas \t Gols \tAproveitamento')
for j in jogadores:
    print(f'{j["nome"]:-<10} {len(j["gols"]):-<10} {j["total"]:-<10} {j["aproveitamento"]}%')