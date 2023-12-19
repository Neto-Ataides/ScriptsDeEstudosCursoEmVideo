#from random import sample
from random import randint
'''a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')'''

a = tuple(randint(1, 10) for n in range(5))

print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')