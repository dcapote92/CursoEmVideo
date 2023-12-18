soma = 0
cont = 0
maior = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    if maior < n:
        maior = n
    if menor == 0:
        menor = n
    elif n < menor:
        menor = n
    continuar = input('Deseja continuar? S/N: ').upper()
    cont += 1
print(f'A média entre todos os valores é {round(soma/cont,2)}, o maoir valor é {maior} e o menor {menor}.')
