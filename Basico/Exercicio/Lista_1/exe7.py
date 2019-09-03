import os
import math 
'''
Desenvolva um algoritmo que receba os valores dos catetos de um triangulo, calcule
e mostre o valor da hipotenusa (hipotenusa = raiz quadrada (cateto1+ cateto2).
'''

l1 = float(input(" Digite um cateto:\t "))
l2 = float (input(" Digite o outro cateto:\t "))
f = math.hypot(l1,l2)
f =  math.floor(f)
print(" Hipotenusa aproximadamente =  {}".format(f))