from random import randint as ri
numeros = list()


def sorteia():
    for i in range(5):
        numeros.append(ri(1,100))


def somaPar():
    soma = 0
    for e in numeros:
        if e % 2 == 0:
            soma += e
    print(f'Soma dos números pares {soma}')

sorteia()
print(numeros)
somaPar()
