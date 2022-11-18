from datetime import date as dt

maior = 0
for p in range(7):
    ano = int(input('Digite o ano de nascimento da pessoa: '))
    if int(dt.today().strftime("%Y")) - ano >= 21:
        maior += 1
print(f'{7 - maior} ainda no atingiram a maioridade y {maior} já são maiores.')