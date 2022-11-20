lista = list()
while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    sexo = input('Sexo [F/M]: ').upper()
    while sexo not in 'FfMm':
        sexo = input('Sexo não valido. Tente novamente.\nSexo [F/M]: ').upper()
    pessoa['sexo'] = sexo
    idade = int(input('Idade:'))
    while True:
        if idade <= 0:
            idade = int(input('Idade invalida. Tente novamente.\nIdade: '))
        elif idade > 120:
            idade = int(input('Idade invalida. Tente novamente.\nIdade: '))
        else:
            break
    pessoa['idade'] = idade
    lista.append(pessoa.copy())
    c = input('Quer continuar?: [S/N]')
    if c in 'Nn':
        break
cant_pessoas = len(lista)
soma_idades = 0
cont = 0
mulheres= list()
for p in lista:
    soma_idades += p['idade']
    cont += 1
    if p['sexo'] == 'F':
        mulheres.append(p.copy())
media_idades = soma_idades//cont
acima_media = list()
for p in lista:
    if p['idade'] > media_idades:
        acima_media.append(p.copy())
print(f'Pessoas cadastradas: {cant_pessoas}.\nMedia de idade: {media_idades}.\nMulheres: ')
for m in mulheres:
    print('\t',m['nome'])
print(f'Acima da media de idade: ')
for p in acima_media:
    print(f'\t{p["nome"]} - {p["sexo"]} - {p["idade"]}')

