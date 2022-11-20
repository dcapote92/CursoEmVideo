l = []
while True:
    n = int(input('Digite um número: '))
    if l.__contains__(n):
        print(f'Valor {n} já existe, não vou adicionar.')
    else:
        l.append(n)
    c = input('Deseja continuar: [S/N] ')
    if c in 'Nn':
        break
print(f'Ordem normal {l}')
l.sort()
print(f'Ordem crescente {l}')
