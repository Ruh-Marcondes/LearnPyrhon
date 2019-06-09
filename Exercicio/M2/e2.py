'''
IMC só que mais completo
'''
import time

n = str(input(' Digite seu nome: '))
n = n.capitalize()
time.sleep(0.5)
print('')
print('*'*50)
print("Vou calcular seu IMC (Índice de Massa Corpórea)")
p = float(input("Digite seu peso: \n"))
a = float(input("Digite sua altura: \n"))
imc = p/a**2
time.sleep(0.5)
print('')
print('*'*50)
print(" {} seu IMC é: {:.2f}.".format(n,imc),end='')
if imc < 20:
    print(' E está abaixo do peso.')
elif imc >= 20 and imc < 25:
    print(' E está normal.')
else:
    print(' E está acima do peso, procure um nutricionista...')
