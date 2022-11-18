num = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número do 1 ao 20: '))
pos = n - 1
while n < 1 or n > 20:
    n = int(input('Número fora do intervalo. Tente novamente: '))
print(f'Você escolhou {num[pos]}')

