import os
import time
'''
Faça um algoritmo que receba o número de horas trabalhadas e o valor do salário
mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo:
a. A hora trabalhada vale a metade do salário mínimo;
b. O salário bruto equivale ao número de horas trabalhadas multiplicado pelo
valor da hora trabalhada
c. O imposto equivale a 3% do salário bruto;
d. O salário a receber equivale ao salário bruto menos o imposto.
'''
h = (int(input('\tDigite o número de hr trabalhados: ')))
sm = (float(input('\tDigite o valor do salário minímo:  ')))
time.sleep(0.5)
os.system('cls')
