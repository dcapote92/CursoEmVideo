num = int(input('Digite um número enteiro: '))
cont = int(input('Digite a quantidade de termos que quer mostrar: '))
while cont != 0:
    print(num, end=' ')
    num += 5
    cont -= 1
if cont == 0:
    print('\nObrigado, tchau!')
