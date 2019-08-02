'''
Faça um algoritimo que mostra na tela 
uma contagem regrassiva para o estouro de fogos de artificio,
indo de 10 até 0,
com um segundo de pausa entre eles;
'''

import time
import os

def july():
    print( ' * '*6)
    for c in range(0,3):
        print('*' ,end=' ')
        print('  '*7,end=' ')
        print('*')
    print('*    4 july!     *')
    for c in range(0,3):
        print('*' ,end=' ')
        print('  '*7,end=' ')
        print('*')
    print(' * '*6)


for d in range(10,-1,-1):
    print('{}'.format(d))
    time.sleep(1)
    os.system('cls')
print(' ')
for j in range(0,4):
    july()
    time.sleep(1)