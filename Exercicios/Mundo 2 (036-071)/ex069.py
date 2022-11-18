h = 0
m_menores = 0
maiores = 0
while True:
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo: [F/M] ')
    if i > 18:
        maiores += 1
    elif s in 'Mm':
        h += 1
    elif s in 'Ff' and i < 20:
        m_menores += 1
    o = input('Deseja continuar: [S/N] ')
    if o in 'Nn':
        break
print(f'Foram cadastrados:\n{maiores} pessoas maiores de 18 anos.\n{h} homens.\n{m_menores} mulheres menores de 20 anos.')