from datetime import date
nasc = int(input('Informe o ano de nascimento: '))


atual = date.today().year

idade = atual - nasc

falt = 18 - idade

alist = falt + atual

if idade == 18:
    print('''Você deve comparecer a junta Militar para alistamento obrigatório
          ''')
elif idade < 18:
    print(f'Faltam {falt} anos para você se alistar, ou seja, no {alist} ano.')
else:
    print('Você já deveria ter se aprensentado para o serviço militar obrigadorio')

