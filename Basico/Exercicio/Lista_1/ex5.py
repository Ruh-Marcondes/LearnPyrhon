import os
'''
Faça um algoritmo que receba o salário mínimo atual e o valor do salário de um funcionário. 
Calcule e mostre a quantidade de salários mínimos que este funcionário
recebe.
'''
os.system ('color f0')
os.system('echo.')
salmin = (float(input('\t Digite o valor do salário minímo atual: ')))
salfunc = (float(input('\t digite o valor do salário do funcionário: ')))
e = salfunc/salmin
print('\n A quantidade de salários minímos recebidos por esse funcionário eh {:.2f}'.format(e))