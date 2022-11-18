a = int(input('Digite o comprimento um: '))
b = int(input('Digite o comprimento dois: '))
c = int(input('Digite o comprimento tres: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Pode formar um triângulo com essas retas')
else:
    print('Não pode formar um triângulo com essas retas, não cumple com a regra de existencia.')
