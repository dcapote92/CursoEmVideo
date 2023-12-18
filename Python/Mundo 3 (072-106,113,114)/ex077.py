tupla = ('Pera', 'Guayaba', 'Mango', 'Chirimoya')
for p in tupla:
    print(f'Para a palavra {p}, as suas vogais são ', end='')
    if p.__contains__('a'):
        print('a', end=' ')
    if p.__contains__('e'):
        print('e', end=' ')
    if p.__contains__('i'):
        print('i', end=' ')
    if p.__contains__('o'):
        print('o', end=' ')
    if p.__contains__('u'):
        print('u', end=' ')
    print()