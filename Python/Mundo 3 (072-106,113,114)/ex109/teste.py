from moeda import aumentar, diminuir , dobro, metade, moeda

salario = 1212
print(f'Seu salario é {moeda(salario)} e com o aumento é {aumentar(salario, 300, format=True)}.')
print(f'Seu salario é {moeda(salario)} e com a diminução é {diminuir(salario, 300, format=True)}.')
print(f'Seu salario é {moeda(salario)} e o dobro é {dobro(salario, format=True)}.')
print(f'Seu salario é {moeda(salario)} e a metade é {metade(salario, format=True)}.')
