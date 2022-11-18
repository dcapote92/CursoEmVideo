n = int(input('Digite um número: '))
print(f'{n}!=', end='')
final = 1
while n != 1:
    final *= n
    print(f'{n}x', end='')
    n -= 1
print(f'1=',final)
