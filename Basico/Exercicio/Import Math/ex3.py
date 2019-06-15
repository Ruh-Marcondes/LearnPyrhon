import math
import os
import time
#Sem import math.hypot()
#h² = b² + c²
os.system('echo.')
time.sleep(1)

print(" Hipotenusa do triângulo retângulo 9cm 4cm hcm ")
h = ((9**2) + (4**2))
h = math.sqrt(h)
h = math.floor(h)
time.sleep(0.5)
print(" Hipotenusa aproximadamente =  {}".format(h))
time.sleep(3)

os.system('cls')

print(" Calculo de hipotenusa ")
os.system('echo.')
time.sleep(1)
b = float(input(" Digite um lado \n "))
os.system('echo.')
c = float(input("Digite o outro lado \n "))
h = ((b**2) + (c**2))
h = math.sqrt(h)
time.sleep(0.5)
print("A hipotenusa do triângulo, cuja os lados são {} e {} é {} ".format(b,c,h))
os.system('cls')

#Com import math.hypot()

print(" Hipotenusa do triângulo retângulo 9cm 4cm hcm ")
d = math.hypot(9,4)
time.sleep(0.5)
print(" Hipotenusa {}".format(d))
os.system('echo.')
time.sleep(0.5)
l1 = float(input(" Digite um lado: \n "))
l2 = float (input(" Digite o outro lado: \n "))
f = math.hypot(l1,l2)
f =  math.floor(f)
print(" Hipotenusa aproximadamente =  {}".format(f))