tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Atlético-MG',
          'São Paulo', 'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará',
          'Atlético-GO', 'Cuiabá', 'Avaí', 'Juventude')
print('=-'*60)
print('A -> Primeiros cinco na tabela do brasileirao')
print(tabela[0:5])
print('=-'*60)
print('B -> Últimos quatro na tabela do brasileirao')
print(tabela[-4:20])
print('=-'*60)
print('C -> Times com organização alfabética')
print(sorted(tabela))
print('=-'*60)
print('D -> Posiçao do time Fortaleza')
print( tabela.index('Fortaleza') + 1)
print('=-'*60)