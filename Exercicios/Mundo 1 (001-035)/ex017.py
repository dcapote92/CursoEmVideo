from math import pow, sqrt
cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(cat_o, 2) + pow(cat_a, 2))
print(f'O comprimento da hipotenusa é {hipotenusa}')
