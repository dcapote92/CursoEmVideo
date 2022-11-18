import random
cont = 0
print('=-'*30,'\nVamos Jogar Par ou Impar\n','=-'*30)
while True:
    n = int(input('Diga um valor: '))
    v = input('Par ou Impar? [P/I] ')
    c = random.randint(1, 10)
    if (n + c) % 2 == 0 and v in 'Pp':
        print(f'Você ganhou! Seu valor {n}+{c} do computador é {n+c} deu par.')
        cont += 1
    elif (n + c) % 2 == 1 and v in 'Ii':
        print(f'Você ganhou! Seu valor {n}+{c} do computador é {n+c} deu impar.')
        cont += 1
    else:
        print(f'Game Over! Seu valor {n}+{c} do computador é {n+c}.', end= ' ')
        break
print(f'Você ganhou {cont} vezes.')