valor_casa = float(input('Informe o valor da casa: '))

salario = float(input('Salario a ser recebido: '))

tempo = int(input('Tempo em anos: '))

prestacao_mensal = valor_casa / (tempo * 12)

if prestacao_mensal > 0.3*salario:
    #print(f'Para pagar o emprestimo de R$ {valor_casa} em {tempo} a prestação será de R$ {prestacao_mensal:.2f}')
    print('Emprestimo Negado! ')
else:
    #print(f'Para pagar o emprestimo de R$ {valor_casa} em {tempo} a prestação será de R$ {prestacao_mensal:.2f}')
    print('Emprestimo aprovado!')
print(f'Para pagar o emprestimo de R$ {valor_casa} em {tempo} anos a prestação será de R$ {prestacao_mensal:.2f}')