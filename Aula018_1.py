#galera = [['Joao', 19], ['Ana', 59], ['Liz', 2]]
#print(galera[0][1])
#for p in galera:
    #print(f'{p[0]} tem {p[1]} anos de idade')


galera = []
dado = []
totmai = 0
totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

   
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade. ')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen +=1
        
print(f'Temos {totmai} maiores e {totmen} menores de idade. ')