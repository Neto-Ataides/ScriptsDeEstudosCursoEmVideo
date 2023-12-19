listanum = []
while True:
    n = int(input('Informe os valores a serem adicionados:  '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!!! ')
    else:
        print('Valor duplicado! \n Não vou adcionar...')
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
listanum.sort()
print(f"Você digitou os valores {listanum}")
