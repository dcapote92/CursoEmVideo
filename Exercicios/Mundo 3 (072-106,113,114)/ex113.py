def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except Exception as erro:
            print(f'\033[0;31mErro {erro.__class__}: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except Exception as erro:
            print(f'\033[0;31mErro {erro.__class__}: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num
num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O valores digitados foram {num1} e {num2}')
