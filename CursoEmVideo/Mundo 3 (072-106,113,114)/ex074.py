from random import randint as ri

tupla = (ri(1,100), ri(1,100), ri(1,100), ri(1,100), ri(1,100))
print(tupla)
menor = tupla[0]
maior = tupla[0]
for n in tupla:
    if n < menor:
        menor = n
    elif n > maior:
        maior= n
print(f'O maior dos números gerados é {maior} e o menor {menor}')