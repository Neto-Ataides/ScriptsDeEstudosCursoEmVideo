'''def mostralinha():
    print('-'*30)    
        
mostralinha()
print('{:^30}'.format('Aprenda Python'))
mostralinha()'''


def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

mensagem(f'{"Aprenda Python":^30}')