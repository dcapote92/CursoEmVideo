pre_normal = float(input('Digite opreço do produto: '))
pre_final = 0
print('*'*60)
print('1. Dinheiro/Cheque  2. Cartão  3. 2x no cartão  4. 3x ou mais')
print('*'*60)
cond_pagamento = input('Escolha a forma de pagamento(Digite o número): ')
if cond_pagamento == '1' :
    pre_final = pre_normal - (pre_normal * 0.1)
elif cond_pagamento == '2':
    pre_final = pre_normal - (pre_normal * 0.05)
elif cond_pagamento == '3':
    pre_final = pre_normal
elif cond_pagamento == '4':
    pre_final = pre_normal + (pre_normal * 0.2)
print(f'O preço final do produto é {pre_final}')