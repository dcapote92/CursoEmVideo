print('Comprimentos de retas que podem formar um triângulo')
a = int(input('Digite o comprimento A: '))
b = int(input('Digite o comprimento B: '))
c = int(input('Digite o comprimento C: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Pode formar um triângulo com essas retas.')
    if a == b or a == c or b == c:
        print('O seu triângulo é isôsceles.')
    elif a == b and a == c and b == c:
        print('O se triângulo e equilátero')
    else:
        print('O seu triângulo é escaleno.')
else:
    print('Não pode formar um triângulo com essas retas, não cumple com a regra de existencia.')
