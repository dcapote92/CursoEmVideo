a = int(input('Digite um ano: '))
secular = str(a)[len(str(a)) - 1 ] == '0' and str(a)[len(str(a)) - 2 ] == '0'
if not secular:
    if a % 4 == 0:
        print('È bissexto.')
    else:
        print('Não é bissexto.')
if secular:
    if a % 400 == 0 and a % 4 == 0:
        print('È bissexto.')
    else:
        print('Não é bissexto.')