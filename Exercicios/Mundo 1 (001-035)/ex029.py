km = int(input('Digite a velocidade que você traz no seu carro: '))
l = 80 #límite de velocidade
m = 7 #Custo por km acima de 80
print(f'Você será multado com um valor de R${(km-l)*m},00 por ultrapassar os {l}km/h' if km > l else 'Obrigado.')