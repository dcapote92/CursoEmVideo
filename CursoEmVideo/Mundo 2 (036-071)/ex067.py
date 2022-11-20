while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for n in range(1,11):
        print(f'{num}*{n} = {n * num}')