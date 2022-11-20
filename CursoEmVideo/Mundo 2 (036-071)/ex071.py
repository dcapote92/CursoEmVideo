import time

b50 = 0
b20 = 0
b10 = 0
b1 = 0
while True:
    v = int(input('Valor a ser sacado R$'))
    if v % 50 == 0:
        b50 = v // 50
    elif v % 50 != 0:
        b50 = v // 50
        v = v % 50
        if v % 20 == 0:
            b20 = v // 20
        elif v % 20 != 0:
            b20 = v // 20
            v = v % 20
            if v % 10 == 0:
                b10 = v // 10
            elif v % 10 != 0:
                b10 = v // 10
                v = v % 10
                if v < 10:
                    b1 = v
    print('Contando seu dinheiro...')
    time.sleep(3)
    print(f'Vai receber: \n{b50} cédulas de R$50. \n{b20} cédulas de R$20.\n{b10} cédulas de R$10.\n{b1} cédulas de R$1.')
    o = input('Deseja continuar: [S/N]')
    if o in 'nN':
        break
print('Obrigado por usar nossos serviços, volte sempre.')