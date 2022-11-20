from datetime import date as dt
data = int(input('Digite seu ano de nascimento: '))
ano = int(dt.today().strftime("%Y"))
edade = ano - int(data)
if  edade <= 9:
    print(f'Têm {edade} anos, categoria Mirim.')
elif 10 <= edade <= 14:
    print(f'Têm {edade} anos, categoria Infantil.')
elif 15 <= edade <= 19:
    print(f'Têm {edade} anos, categoria Junior.')
elif edade == 20:
    print(f'Têm {edade} anos, categoria Sênior.')
else:
    print('A sua categoria é Master.')