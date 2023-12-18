l = []
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    c = input('Quer continuar?: ')
    if c in 'nN':
        break
p = []
i = []
for n in l:
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
print(f'Lista completa {l}. \nLista de pares {p}.\nLista de impares {i}.')