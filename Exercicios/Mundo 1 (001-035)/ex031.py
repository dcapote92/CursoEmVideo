km = int(input('Digite a distância do seu viagem em Km: '))
vc = 0.50 #Custo por Km de viagem curto
vl = 0.45 #Custo por Km de viagem longo
print(f'O custo do seu viagem é R${vc * km}' if km <= 200 else f'O custo de seu viagem é R${(200 * vc) + (km - 200) * vl}')