'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma A + B = {a+b}')

# Programa Principal

soma(b=4,a=5)
soma(8, 9)'''

'''def cont(*num):
    tam = len(num)
    print(f' Recebi os valores {num} e sao ao todo {tam} números')


cont(2, 1, 7)
cont(8, 9)
cont(4, 4, 7, 6, 2)'''

val = [7,2,5,0,4]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        
dobra(val)
val_ord = sorted(val)
print(val)
print(val_ord)
