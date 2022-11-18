som = 0
for n in range(6):
    num = int(input(f'Digite o {n+1} número:'))
    if num % 2 == 0:
        som += num
print(som)