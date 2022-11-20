s = float(input('Digite o seu salario: '))
print(f'Seu novo salario será R${s + s * 0.1}' if s > 1250 else f'Seu novo salario será R${s + s * 0.15}')
