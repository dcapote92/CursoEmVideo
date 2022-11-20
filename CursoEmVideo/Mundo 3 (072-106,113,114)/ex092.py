from datetime import datetime
dados = {}
dados['nome'] = input('Digite seu nome: ')
nascimento = int(input('Digite seu ano denascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Digite sua carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('*'*30)
print(dados)