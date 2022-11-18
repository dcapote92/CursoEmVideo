import random
n = int(12)
a = int(11)
c = 0
while a != n:
    n = random.randint(0, 10)
    a = int(input('Tente adivinar um numero entre 0 e 10: '))
    print(n)
    if a == n:
        print('Parabens, você ganhou!')
    else:
        print('Tente novamente, ganhe eu.')
        c += 1
print(f'Você precisou {c} palpites para ganhar.')


