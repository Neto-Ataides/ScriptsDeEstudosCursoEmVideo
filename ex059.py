n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opção = 0
while opção != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    print('\n')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        def add(n1,n2):
            return n1 + n2
        print(f'A soma entre {n1} + {n2} é {add(n1,n2)}')
    elif opção == 2:
        def multiply(n1,n2):
            return n1 * n2
        print(f'O produto de {n1} * {n2} é {multiply(n1,n2)}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente. ')
    print('=-='*10)
print('Fim do program! Volte sempre!')
