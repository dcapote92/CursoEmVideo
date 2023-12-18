def notas(* nota, sit=False):
    """
    :param nota: recebe várias notas
    :return: um dicionário
    """
    aluno = dict()
    aluno['notas'] = len(nota)
    aluno['maior'] = 0
    aluno['menor'] = 0
    aluno['media'] = 0
    soma = 0
    for n in nota:
        if aluno['maior'] == 0 and aluno['menor'] == 0:
            aluno['maior'] = aluno['menor'] = n
        else:
            if n > aluno['maior']:
                aluno['maior'] = n
            elif n < aluno['menor']:
                aluno['menor'] = n
        soma += n
    aluno['media'] = soma / aluno['notas']
    if sit == True:
        if aluno['media'] < 6:
            aluno['situação'] = 'Suspenso'
        else:
            aluno['situação'] = 'Aprovado'
    return aluno

print(notas(5,6,4,6,8,9,7,4,3,6,5,sit=True))

