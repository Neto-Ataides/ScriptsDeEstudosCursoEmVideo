print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
razão = int(input('Razão da Pa: '))
n = int(input('númerotermos: '))
an = a1 + (n - 1) * razão
# for c in range(primeiro, último + razão, razão):
c = a1
mais = 10
nt = 0
while mais != 0:
    nt += mais
    while c <= an:
        print(f'{c}', end='-> ')
        c += razão
    print('Pausa')
    mais = int(input('Mais quantos termos você quer inserir? '))
print('Acabou')
