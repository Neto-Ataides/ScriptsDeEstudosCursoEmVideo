from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
v0 = 'Empate! '
v1 ='Vitória do Jogador! '
v2 ='Vitória do Computador! '
v4 = 'Jogada Inválida!'
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print(v0)
    elif jogador == 1:
        print(v1)
    elif jogador == 2:
        print(v2)
    else:
        print(v4)
        
elif computador == 1:
    if jogador == 0:
        print(v2)
    elif jogador == 1:
        print(v2)
    elif jogador == 2:
        print(v1)
    else:
        print(v4)
elif computador == 2:
    if jogador == 0:
        print(v1)
    elif jogador == 1:
        print(v2)
    elif jogador == 2:
         print(v0)
    else:
        print(v4)
print(f'O computador escolheu {computador}')
