produtos = ('Pão', 0.5, 'Arroz', 3.65, 'Açúcar', 3.55, 'Café', 4.69)
for n in produtos:
    if produtos.index(n) % 2 == 0:
        print(f'{produtos[produtos.index(n)]:.<30}', end=' ')
        print('R$ ', end='')
    else:
        print(float(produtos[produtos.index(n)]))
