maior = 0
menor = 0
for p in range(5):
    k = float(input(f'Digite o peso em kg da pessoa [{p+1}]: '))
    if p == 1:
        maior = k
        menor = k
    else:
        if k > maior:
            maior = k
        elif k < menor:
            menor = k
print(f'O maior peso foi {maior} kg y o menor {menor} kg.')