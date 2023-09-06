lanche = ('hamburger', 'suco', 'pizza', 'pudim')
# print(lanche)
# print(lanche[1:])
# print(len(lanche))

'''for cont in range(0, len(lanche)):
        print(f"Euvou comer {lanche[cont]}")'''
        
#for comida in lanche:
#    print(f"Euvou comer {comida}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print(type(sorted(lanche)))
