from datetime import datetime as dt
ano_atual = dt.now().year
def voto(ano):
    voto = ''
    if ano_atual - ano < 18:
        voto = 'Não vota'
    elif 18 < ano_atual - ano < 65:
        voto = 'Voto obrigatorio'
    else:
        voto = 'Voto opcional'
    return voto


a = int(input('Digite seu ano de nascimento: '))
print(voto(a))