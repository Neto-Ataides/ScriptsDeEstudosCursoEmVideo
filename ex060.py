from math import factorial

n = int(input('Inforem um número para calcular o fatorial: '))
c = n
f = factorial(n)
# while c > 0:
for c in range(c, 0, -1):
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
# c -= 1
print(f'{f}')
