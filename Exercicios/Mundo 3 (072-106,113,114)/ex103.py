def ficha(nome, gols):
    """
    :param nome: Nome do jogador
    :param gols: Quantos gols ele marcou
    :return: Ficha do jugador( nome e gols)
    """
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0

    jogador = {'nome': nome, 'gols': gols}
    return jogador

nome = input('Nome do Jogador: ')
gols = input('Número de gols: ')
jogador = ficha(nome, gols)
print(f'O jogador {jogador["nome"]} fez {jogador["gols"]} no campeonato.')