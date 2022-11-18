import random

mao = ['Pedra', 'Papel', 'Tesoura']
mao_jogador = int(input('Vamos jogar Jokenpô?\nEscolhe a tua mão\n"1.Pedra  2.Papel  3.Tesoura"\nSua opção:')) - 1
mao_computador = random.randint(0,2)
if mao[mao_jogador] == 'Pedra' and mao[mao_computador] == 'Tesoura':
    print(f'Parabens! Você Ganhou.\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Pedra' and mao[mao_computador] == 'Papel':
    print(f'Kkkk ganho eu!\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Papel' and mao[mao_computador] == 'Pedra':
    print(f'Parabens! Você Ganhou.\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Papel' and mao[mao_computador] == 'Tesoura':
    print(f'Kkkk ganho eu!\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Tesoura' and mao[mao_computador] == 'Papel':
    print(f'Parabens! Você Ganhou.\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Tesoura' and mao[mao_computador] == 'Pedra':
    print(f'Kkkk ganho eu!\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Pedra' and mao[mao_computador] == 'Pedra':
    print(f'Opa, empate, tentemos novamente!\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Papel' and mao[mao_computador] == 'Papel':
    print(f'Opa, empate, tentemos novamente!\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')
elif mao[mao_jogador] == 'Tesoura' and mao[mao_computador] == 'Tesoura':
    print(f'Opa, empate, tentemos novamente!\nMão computador: {mao[mao_computador]}\nMão jogador: {mao[mao_jogador]}')

