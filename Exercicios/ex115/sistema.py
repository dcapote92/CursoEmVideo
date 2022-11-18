from ex115.lib.interface import *
from ex115.lib.arquivo import  *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Listar pessoas no arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar pessoas no arquivo
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mErro! Digite uma opção válida!\033[m')
    sleep(2)