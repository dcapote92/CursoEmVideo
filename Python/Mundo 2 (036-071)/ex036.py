custo = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salário: '))
anos = int(input('Em quantos anos vocẽ vai pagar?:'))

# CF = i / (1 - (1 / (1 + i)^n)) -> Coeficiente de financiamento
# i -> interesse ou taxa de juros
# n -> quantidade de mêses
i = float(0.03)
n = anos * 12
CF = i /(1 - (1 / pow((1 + i), n)))
if custo * CF > salario * 0.3:
    print('O seu empréstimo não pode ser, o seu salario é muito baixo.')
else:
    print('Empréstimo aprovado, parabens!')


