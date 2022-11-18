pessoas = []
while True:
    pessoa = []
    nome = input('Digite nome: ')
    peso = float(input('Digite peso em kg: '))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa)
    c = input('Quer acrecentar pessoa?: ')
    if c not in 'SsNn':
        print('Só são aceitos os valores S ou N. Tente novamente.')
        c = input('Quer acrecentar pessoa?: ')
        if c in 'Nn':
            break
    elif c in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
men = 0
mai = 0
for p in pessoas:
    if men == 0 and mai == 0:
        mai = men = p
    else:
        if p[1] > mai[1]:
            mai = p
        elif p[1] < men[1]:
            men = p
list_maior = []
list_menor = []
for p in pessoas:
    if p[1] == mai[1]:
        list_maior.append(p[0])
    elif p[1] == men[1]:
        list_menor.append(p[0])

print(f'As pessoas mais pesadas foram {list_maior} com {mai[1]} kg.\nAs pessoas mais leves foram {list_menor} com {men[1]} kg.')
