primeiro = int(input('Primeiro termo: '))
razão = int(input('razão: '))
n = int(input('númerotermos: '))
último = primeiro + (n -1) * razão
#for c in range(primeiro, último + razão, razão):
c = 0
while c != último + razão:
    print(f'{c}', end='-> ')
    c += razão
print('Acabou')