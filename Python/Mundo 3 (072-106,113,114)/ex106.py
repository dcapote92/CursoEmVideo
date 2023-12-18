def interact(c):
    print('\033[0:33:40m')
    print(f'{help(c)}')

def lin():
    print('~' * 100)



code = ''
while True:
    code = input('\033[mFunção ou Biblioteca >>> ')
    if code == 'fim':
        break
    else:
        lin()
        interact(code)
        lin()
