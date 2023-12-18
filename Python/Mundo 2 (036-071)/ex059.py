sair = False
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
while sair != True:
    op = input('Escolha uma opção:\n[1]Somar\t[2]Multiplicar\t[3]Maior\t[4]Novos números\t[5]Sair do programa\n:')
    if op == '1':
        print(f'A soma de {n1} e {n2} é {n1 + n2}')
    elif op == '2':
        print(f'A multiplicação de {n1} e {n2} é {n1 * n2}')
    elif op == '3':
        print(f'O maior é {n1}'if n1 > n2 else f'O maior é {n2}')
    elif op == '4':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite mais um valor: '))
    elif op == '5':
        print('Tchau!')
        sair = True
