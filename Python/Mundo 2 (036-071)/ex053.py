frase = input('Digite uma frase qualquer: ').strip().upper().split()
junto = ''.join(frase)
inverso = ''
for l in range(len(junto) -1, -1, -1):
    inverso += junto[l]
if inverso == junto:
    print(f'A frase é um palindromo.\n{junto}\n{inverso}')
else:
    print(f'A frase não é um palindromo.\n{junto}\n{inverso}')