soma = 0
for n in range(500):
    if n % 2 == 1 and n % 3 == 0:
        soma += n
print(soma)