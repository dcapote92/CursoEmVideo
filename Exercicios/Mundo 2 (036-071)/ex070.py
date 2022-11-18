total = 0
prod_acima_mil = 0
mais_barato =''
barato = 1000
while True:
    n = input('Digite o nome do produto: ')
    p = float(input('Digite o preço do produto: '))
    total += p
    if p > 1000:
        prod_acima_mil += 1
    elif p < barato:
        barato = p
        mais_barato = n
    o = input('Deseja continuar: [S/N] ')
    if o in 'Nn':
        break
print(f'Total gasto na compra {total}.\n{prod_acima_mil} produtos custam acima de R$1000.\nO produto mais barato é {mais_barato}.')