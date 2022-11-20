# Comprovar que una expressão é válida com uso de parentessis
ex = input('Digite uma expressão matemática: ')
l = []
for simb in ex:
    if simb == '(':
        l.append('(')
    elif simb == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')