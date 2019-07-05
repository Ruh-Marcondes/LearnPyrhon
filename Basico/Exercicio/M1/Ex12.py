'''
 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
print(" '-' "*5)
p = float(input('Escolha um produto e digite seu preço '))
des = p*5/100
print(f'Parabém seu produto tem um desconto de {des:.2f},',end='')
print(' sendo assim seu novo valor será {:.2f}'.format(p-des))