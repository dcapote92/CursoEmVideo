def maior(* valores):
    maior = 0
    for n in valores:
        if n > maior:
            maior = n
    print(valores)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior é {maior}')

maior(1,6,5,7,45,34,6,4)