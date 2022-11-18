v = int(0)
soma = 0
cont = 0
while v != 999:
    v = int(input('Digite um número inteiro: '))
    if v != 999:
        soma += v
        cont += 1
print(f'Você digitou {cont} numeros e sua soma é {soma}')
