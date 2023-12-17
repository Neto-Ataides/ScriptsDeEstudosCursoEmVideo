while True:
    num = int(input('Informe um número para ver sua tabuada: '))
    print('-' * 30)
    for c in range(1, 11):
        mult = num * c
        print(f'{num} X {c} = {mult}')
    print('-' * 30)
    if num < 0:
        break
print('Fim!!!')
