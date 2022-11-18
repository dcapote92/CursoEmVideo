l = []
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    c = input('Quer continuar?: ')
    if c in 'nN':
        break
print(f'[A] Foram digitados {len(l)} números.\n[B] Lista ordem decrescente {sorted(l, reverse = True)}.\n[C] Valor 5 digitado: ', 'Sim.' if l.count(5) > 0 else 'Não.')