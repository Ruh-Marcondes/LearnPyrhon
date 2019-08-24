import os
'''
O Preço de um automóvel é calculado pela soma do preço de fábrica, mais o preço
dos impostos (45% do preço de fábrica), mais o percentual dos vendedores (28% do
preço de fábrica). Faça um algoritmo que imprima o nome do automóvel e seu preço
final.
'''
os.system('color f0')
print(' ')
a = float(input('\t Digite o preço de fábrica do automóvel: '))
b = a * 0.45
a +=b
print('\t Preço do autómoel: {:.2f}'.format(a))
os.system('pause')
os.system('color ')