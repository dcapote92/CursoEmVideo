soma = 0
cont = 0
contmulher = 0
maior = ''
idade_maior = 0
for p in range(4):
    cont += 1
    nome = input(f'Digite o nome [{cont}]: ')
    idade = int(input(f'Digite a idade [{cont}]: '))
    sexo = input(f'Digite o sexo (F/M)[{cont}]: ')
    soma += idade
    if idade > idade_maior and sexo == 'm' or sexo == 'M':
        maior = nome
    elif idade < 20 and sexo == 'f' or sexo == 'F':
        contmulher += 1
print(f'A media  de idades é {soma//cont}, o homen mais velho é {maior} e têm {contmulher} mulheres menores de 20 anos.')