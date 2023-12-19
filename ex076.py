print('-' * 50)
print(f"{'LISTAGEM DE PREÇOS':^50}")
print('-' * 50)

listagem = ('lápis', 1.20, 'borracha', 0.85,
            'canelta', 1.85,
            'caderno', 10.85, 'Estojo', 4.50,
            'Mochila', 68.45)
#for pos in range(0, len(listagem)):
#    if pos % 2 == 0:
#        print(f"{listagem[pos]:.<50}", end="")
#    else:
#        print(f"R${listagem[pos]:>6.2f}")
#print('-' * 50)

for pos in range(0,len(listagem),2):
    print(f"{listagem[pos]:.<40}",f"R${listagem[pos+1]:>6.2f}")
print('-' * 50)
