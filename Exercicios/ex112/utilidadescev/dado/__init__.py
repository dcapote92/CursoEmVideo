def leiaDinheiro(msg):
    flag = False
    while not flag:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m')
        else:
            flag = True
            return float(entrada)

def leiaInt(num):
    num = input('Digite um número: ')
    while not str(num).isdigit():
        print('\033[0:31:470mErro! Digite um número inteiro válido.')
        num = input('\033[mDigite um número: ')
    print('Número digitado:',num)
    pass
