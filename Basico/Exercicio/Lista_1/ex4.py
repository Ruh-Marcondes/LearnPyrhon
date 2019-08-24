import os
'''
Faça um algoritmo que receba 4 números calcule,
imprima a soma e a média dos números lidos
'''
os.system("color f0")
a = float(input('\t Digite o valor 1:  '))
b = float(input('\t Digite o valor 2:  '))
c = float(input('\t Digite o valor 3:  '))
d = float(input('\t Digite o valor 4:  '))

e = a + + b + c + d
print('\t A soma de {:.2f} + {:.2f} + {:.2f} + {:.2f} = {:.2f}'.format(a,b,c,d,e))
e = e/4
print('\t A média eh: {:.2f} '.format(e))