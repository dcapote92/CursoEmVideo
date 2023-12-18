num = int(input('Digite um número enteiro: '))
print('*' * 60 )
print('Agora vamos fazer converção numérica')
o = int(input('[1] para binário\n[2] para octal\n[3] para hexadecimal\nSua opção: '))
if o == 1:
    print(f'Seu número em Binário é {bin(num)[2:]}')#[2:] pula  o 0b
elif o == 2:
    print(f'Seu número em Octal é {oct(num)[2:]}')#[2:] pula  o 0o
elif o == 3:
    print(f'Seu número em Hexadecimal é {hex(num)[2:]}')#[2:] pula  o 0x
else:
    print('Opção inválida. Tente novamente;')
print('*' * 60)

