def aumentar(dinheiro = 0, aumento = 0, format= False):
    """
    :param dinheiro: quantidade inicial
    :param aumento: quantidade aumentada
    :return: quantidade final
    """
    dinheiro += aumento
    if format == True:
        return moeda(dinheiro)
    else:
        return dinheiro


def diminuir(dinheiro = 0, diminuente = 0, format= False):
    """
    :param dinheiro:quantidade inicial
    :param diminuente: quantidade a diminuir
    :return: quantidade final
    """
    dinheiro -= diminuente
    if format == True:
        return moeda(dinheiro)
    else:
        return dinheiro


def dobro(dinheiro = 0, format= False):
    """
    :param dinheiro:quantidade inicial
    :return: dobro da quantidade inicial
    """
    if format == True:
        return moeda(dinheiro * 2)
    else:
        return dinheiro * 2


def metade(dinheiro = 0, format= False):
    """
    :param dinheiro: quantidade inicial
    :return: metade da quantidade inicial
    """
    if format == True:
        return moeda(dinheiro / 2)
    else:
        return dinheiro / 2

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
