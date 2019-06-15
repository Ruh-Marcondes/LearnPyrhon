'''
Sites.google.com/etec/maromo.net

Ler idade
Dizer idade em meses!!
Dizer se pode votar 
'-'
'''
import os
from datetime import datetime
#------------------------------------------------------
print('')
n = (str(input(' Digite seu nome: ')))
a = (int(input(' Digite o ano que você nasceu: ')))
m = (int(input(' Digite em que mês você nasceu: ')))
d = (int(input(' Digite o dia que você nasceu: ')))
now = datetime.now()
#-----------------------------------------------------


i = now.year - a
if m > now.month:
    i -= 1
elif m == now.month:
    if d > now.day:
        i -= 1 
    else:
        pass 

if i > 18:
    print('')
    print(f'{n}, obrigatóriamente você tem que votar!')
elif i < 18 and i > 16:
    print('')
    print(' Pode votar, mas não é obrigatório...')
else:
    print('')
    print(f' {n}, não pode votar não tem 18 anos ainda.')