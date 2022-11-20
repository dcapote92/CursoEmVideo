sexo = input('Digite seu sexo(F/M): ').upper()
while sexo not in 'FM':
    sexo = input(f'{sexo} não é um dato válido. Tente novamente:').upper()
print('Cadastrado corretamente.')

