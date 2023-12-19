print('=' * 40)
print(f"{'Banco CEV':^40}")
print('=' * 40)
valor = int(input('Qual o valor que você deseja sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
print(f'A quantidade de notas é ')
