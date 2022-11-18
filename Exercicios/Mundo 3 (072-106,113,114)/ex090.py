aluno = {}
aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a média: '))
if aluno['media'] <= 5.0:
    aluno['situação'] = 'suspenso'
else:
    aluno['situação'] = 'aprovado'
print('O aluno ',aluno['nome'],' com média ', aluno['media'],' é ',aluno['situação'])
