lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([nome, [nota1, nota2], (nota1 + nota2)/2])
    c = input('Quer continuar? [S/N] ')
    if c in 'Nn':
        break
    elif c not in 'SsNn':
        print('Carater não valido. Tente novamente.')
        c = input('Quer continuar? [S/N] ')
        if c in 'Nn':
            break
print('+' * 30)
print('\tNo.\tNome\tMedia')
print('+' * 30)
for a in lista:
    print(f'\t{lista.index(a) + 1}\t{a[0]:^5}\t{a[2]:^5}')
while True:
    a = int(input(f'Digite o número da lista para o aluno que você quer olhar seus notas [número fora da lista interrompe]: '))
    if a < 1 or a > len(lista):
        break
    print(f'Notas de {lista[a-1][0]}: {lista[a-1][1][0]} e {lista[a-1][1][1]}')
