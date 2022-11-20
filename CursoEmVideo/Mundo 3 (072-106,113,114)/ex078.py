l = []
maior = 0
menor = 0
for c in range(0, 5):
    l.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = l[c]
    else:
        if l[c] > maior:
            maior = l[c]
        elif l[c] < menor:
            menor = l[c]
print(f'\nO maior é {maior} nas posições ', end='')
for i, v in enumerate(l):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor é {menor} nas posições ', end='')
for i, v in enumerate(l):
    if v == menor:
        print(f'{i}...',end='')
