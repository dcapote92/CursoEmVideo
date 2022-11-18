import datetime as dt
d = int(input('Qual é sua data de nascimento?(digite o ano): '))
date = int(dt.date.today().strftime("%Y"))
data = date - d
if data == 18:
    print(f'Você tem {data} anos, vai se alistar ao serviço militar agora.')
elif data < 18:
    print(f'Você tem {data} anos, ainda vai se alistar.')
else:
    print(f'Você tem {data} anos, passou do tempo.')