times = ('Palmeiras', 'Internacional', 'Flamengo', 'Corinthians',
         'Fluminense', 'Athletico-PR', 'Atlético-MG',
         'São Paulo', 'América-MG', 'Fortaleza')
print(f"Lista de times do brasileirão: {times}")
print(f'Os 5 primeiros sao:  {times[0:5]}')
print(f" Os quatro útimos times são {sorted(times)}")
print(f"O Fortaleza está na {times.index('Fortaleza')+1}ª posição")

for i in enumerate(times):
    print(i)
