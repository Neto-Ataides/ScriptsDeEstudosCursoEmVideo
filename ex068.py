from random import randint

print('=-=' * 10)
print('Vamos Jogar Par ou Ímpar')
print('=-=' * 10)
v = 0
while True:
    jogador = int(input('Dê um palpite: '))
    computador = randint(0, 10)
    total = jogador + computador
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if opção == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1
        else:
             print('Você perdeu!!!')
             break
    elif opção == 'I':
        if total % 2 == 1:
           print('Você venceu!!!')
           v += 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente? ')
print(f'Game Over! Você venceu {v} vezes.')
    