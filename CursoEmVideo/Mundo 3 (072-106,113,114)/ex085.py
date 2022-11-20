lista = [[], []]
for v in range(7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'Pares {sorted(lista[0])}\nImpares {sorted(lista[1])}')


