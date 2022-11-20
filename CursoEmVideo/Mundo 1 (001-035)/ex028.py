import random
n = random.randint(0, 5)
a = int(input('Tente adivinar um numero entre 0 e 5: '))
print('Parabens, você adivinou!' if a == n else 'Tente novamente, esse não é o numero.')
