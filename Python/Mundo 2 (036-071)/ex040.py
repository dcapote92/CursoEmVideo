n1 = int(input('Digite uma nota: '))
n2 = int(input('Digite mais uma nota: '))
m = (n1 + n2) / 2
if m < 5.0 :
    print(f'{m} Reprovado')
elif 5.0 < m < 6.9:
    print(f'{m} Recuperação')
else:
    print(f'{m} Aprovado')