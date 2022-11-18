peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em m: '))
IMC = peso / pow(altura, 2)
round(IMC, 2)
if IMC < 18.5:
    print(f'O seu IMC é {round(IMC, 2)}, você é abaixo do peso.')
elif 18.5 <= IMC <= 25:
    print(f'O seu IMC é {round(IMC, 2)}, você tem um peso ideal.')
elif 26 <= IMC <= 30:
    print(f'O seu IMC é {round(IMC, 2)}, você tem sobrepeso.')
elif 31 <= IMC <= 40:
    print(f'O seu IMC é {round(IMC, 2)}, você tem obesidad.')
else:
    print(f'O seu IMC é {round(IMC, 2)}, você tem obesidad mórbida.')