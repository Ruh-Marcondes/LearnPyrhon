'''
solcita salário e calcula INSS(11%)
calcula contribuição,
 tabela || salário < 800 = 2% (contribuição sindical)
 salário >= 800 && <= 1500 3% (contribuição sindical)
 salário > 1500 5% (contribuição sindical)
  mostrar - sal bruto, sál liquido, valor pago de inss 
 e valor pago de contribuição sindical 
 variáveis
 s =salário
 cs = contribuição sindical
 ins = inss
 n = nome do funcionário
 sl = salário líquido  
'''
import time
import os 
print(' ')
n = str(input(' Digite o nome: '))
s = float(input(' Digite o valor do sálario: '))

ins =  s * 11 /100

if s < 800:
    cs = s * 2 /100
elif s >= 800 and s <= 1500:
    cs = s * 3 / 100
else:
    cs = 5 * 5 /100

sl = s - ins - cs
time.sleep(2)
os.system('cls')
time.sleep(1)
print(f' Dados de {n}: ')
time.sleep(0.5)
print(f' Salári bruto: {s:.2f} \n Salário líquido: {sl:.2f}')
time.sleep(0.5)
print(f' Valor pago de INSS: {ins:.2f}\n Contribuição Sindical: {cs:.2f}')