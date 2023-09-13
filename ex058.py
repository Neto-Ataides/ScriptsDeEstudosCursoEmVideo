from random import randint
comput = randint(1,40)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Dê um palpite: '))
    palpites += 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('Mais... Tente outra vez.')
        elif jogador > comput:
            print('Menos... Tente outra vez.')
print(f'Você deu {palpites} palpites, e o número sorteado foi: {comput}')