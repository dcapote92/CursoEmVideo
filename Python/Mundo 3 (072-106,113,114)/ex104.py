def leiaInt(num):
    num = input('Digite um número: ')
    while not str(num).isdigit():
        print('\033[0:31:470mErro! Digite um número inteiro válido.')
        num = input('\033[mDigite um número: ')
    print('Número digitado:',num)
    pass

leiaInt('a')