from time import sleep
def contador(i, f, p):
    cont = i
    if i < f:
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.2)
            cont += p
        print('.')
    elif i > f:
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.2)
            cont -= p
        print('.')


contador(1, 15, 1)
contador(15, 1, 1)
print('Agora você vai definir os seus números.')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)