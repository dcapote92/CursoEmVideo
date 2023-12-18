n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero inteiro:'))
n3 = int(input('Digite mais um numero inteiro:'))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'O maior é {n1} e o menor é {n3}')
    else:
        print(f'O maior é {n1} e o menor é {n2}')
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'O maior é {n2} e o menor é {n3}')
    else:
        print(f'O maior é {n2} e o menor é {n1}')
if n3 > n1 and n3 > n2:
    if n1 > n2:
        print(f'O maior é {n3} e o menor é {n2}')
    else:
        print(f'O maior é {n3} e o menor é {n1}')

