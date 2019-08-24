import os
'''
 Elabore um algoritmo que faça a leitura de dois números reais e calcule as operações
de soma, subtração, divisão e multiplicação a partir dos valores lidos e mostre os
resultados;
'''
os.system('color f0')
a = float(input(' Digite o valor 1:\t'))
b = float(input(' Digite o valor 2:\t'))
c = a+b
print('\t Soma: {:.2f} + {:.2f} = {:.2f}'.format(a,b,c))
print(' ')
c = a-b
print('\t Sub: {:.2f} - {:.2f} = {:.2f}'.format(a,b,c))
print(' ')
c = a*b
print('\t Mult {:.2f} * {:.2f} = {:.2f}'.format(a,b,c))
print(' ')
c = a+b
print('\t Div {:.2f} / {:.2f} = {:.2f}'.format(a,b,c))