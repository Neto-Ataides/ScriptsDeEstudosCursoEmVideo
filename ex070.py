print('-' * 50)
print('LOJA SUPER BARATÃO')
print('-' * 50)
quant = total = menor = cont = 0
barato = ' '
while True:
    nomeProduto = str(input('Nome do produto: '))
    precoProduto = float(input('Preço: R$ '))
    cont += 1
    total += precoProduto
    if precoProduto > 1000:
        quant += 1
    if cont == 1 or precoProduto < menor:
        menor = precoProduto
        barato = nomeProduto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Qual é o total gasto na compra: R${total:.2f}')
print(f'O número de produtos que custam mais que R$ 1000 é {quant}')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')