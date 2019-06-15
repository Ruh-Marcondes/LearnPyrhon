#imput os é para comandos do CMD
import time
import os
print(" Vamos rolver a função f(x) = X + 40 ")
time.sleep(0.5)
x = float(input(" Digite um valor para 'x': \n "))
y = x + 40
time.sleep(0.5)
print(" [f({}) = {} + 40] = {} ".format(x,x,y))
time.sleep(0.5)
os.system('cls')
print("Agora vamos calcular para a função f(x) = x² + 3")
x = float(input(" Digite um valor para 'x': \n "))
y = ((x**2) + 3)
time.sleep(0.5)
print(" [f({}) = {}² + 3] = {} ".format(x,x,y))