from moeda import aumentar, diminuir , dobro, metade, moeda

salario = 1212
print(f'Seu salario é {moeda(salario)} e com o aumento é {moeda(aumentar(salario, 300))}.')
print(f'Seu salario é {moeda(salario)} e com a diminução é {moeda(diminuir(salario, 300))}.')
print(f'Seu salario é {moeda(salario)} e o dobro é {moeda(dobro(salario))}.')
print(f'Seu salario é {moeda(salario)} e a metade é {moeda(metade(salario))}.')
