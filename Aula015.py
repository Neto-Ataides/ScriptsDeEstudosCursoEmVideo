n = s = 0
valores = 0
while True:
    n = int(input('Digite um valor: '))
    
    if n == 999:
         break
    valores += 1
    s += n 
   
print(f'A soma vale {s} e o número de valores informados é {valores}')