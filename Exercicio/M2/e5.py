# n = nome produto
# qe =  quantidade em estoque
# qmi = quantidade minima
# qmx = quntidade máxima

#algoritimo!

import os
import time
print('')

qmi = int(input(' Quantidade minima de: ')) 
qmx = int(input(' Quantidade máxima de: '))

while True:
    os.system('cls')
    print('')
    n = str(input(' Nome do produto: '))
    qe = int(input(f' Quantidade em estoque de {n}: '))
    if qe < qmi:
        print(' Compar {}. Quantidade em falta!'.format(n))
        print(' ')
        print(' \'-\' '*10)
    else: 
        print(' Quantidade de {} sulficiente. NÃO COMPRAR!! '.format(n))
        print(' ')
        print(' \'-\' '*10)
    time.sleep(3)
    os.system('cls')
    print('')
    r = str(input(' Deseja comtinuar? (S/N) \n ')) 
    if r != 's':
        break