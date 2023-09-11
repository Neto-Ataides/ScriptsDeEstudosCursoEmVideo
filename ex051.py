primeiro = int(input('Primeiro termo: '))
razão = int(input('razão: '))
n = int(input('númerotermos: '))
último = primeiro + (n -1) * razão
for c in range(primeiro, último + razão, razão):
    print(f'{c}', end='-> ')
print('Acabou')