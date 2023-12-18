def factorial(num, show):
    """
    :param num: O número a ser calculado
    :param show: Mostrar ou não a conta
    :return: O valor do fatorial de num
    """
    fact = 1
    for n in range(1, num):
        fact *= n+1
        if show == True:
            print(f'{n} * {n+1} = {fact}')
    return fact
print(factorial(7, False))