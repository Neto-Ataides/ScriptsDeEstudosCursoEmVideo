valores = []
maior = 0
menor = 0
#for v in range(0, 5):
#    valores.append(int(input(f'Digite um valor na posição {v}: ')))
#    if v == 0:
#        maior = menor = valores[v]
#    else:
#        if valores[v] == max(valores):
#            maior = valores[v]
#        if valores[v] == min(valores):
#            menor = valores[v]

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {v}: ')))
    if valores[v] == max(valores):
        maior = valores[v]
    if valores[v] == min(valores):
       menor = valores[v]
print(f'Os valores digitados são: {valores}')
print(f"O maior valor é: {maior} nas posições ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f"O menor valor é: {menor} nas posições ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
