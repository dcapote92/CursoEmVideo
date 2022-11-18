num = int(input('Digite um número: '))
tot = 0
for n in range(1, num+1):
    if num % n == 0:
        print('\033[33m', end=' ') # Se é divisível pelo contador(n) fica amarelo.
        tot += 1
    else:
        print('\033[31m', end=' ')# Senão fica vermelho.
    print(f'{n}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')