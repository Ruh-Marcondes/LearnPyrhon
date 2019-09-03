import os
'''
    Elabore um algoritmo que receba o valor de um produto,
     seu percentual de desconto. 
     Calcule e mostre o preço do produto após o desconto.
'''

n = (float(input('\tDigite o valor do produto: ')))
per = (float(input('\tDigite o percentual de aumento do segunte modo ex--> 40% -- 0.40:\t')))
u = (per*n)
n = n-u
os.system('cls')
print("\tO novo preço do produto é {:.2f}".format(n))