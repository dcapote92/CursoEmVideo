a1 = int(input('Digite um número:'))
a2 = int(input('Digite um número:'))
a3 = int(input('Digite um número:'))
a4 = int(input('Digite um número:'))
tupla = (a1, a2, a3, a4)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 foi digitado pela primeira vez na posição {tupla.index(3)}')
for n in tupla:
    if n % 2 == 0:
        print(f'Valor par {n}')
