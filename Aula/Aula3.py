#Condiçoes (P1)
# Simples e Compostas 
# If Else
# progrmas não são bipolares... Como eu...
import os
import time
os.system('echo.')
n = str(input('Digite teu nome? \n '))
if n == 'Ruahma':
    time.sleep(0.5)
    print(' \'-\' '*5)
    print('')
    print(' Hello, {}, Bem - Vinda!'.format(n))
    print('')
    print(' \'-\' '*5)
else:
    print('Hello, {}'.format(n))

time.sleep(3)
os.system('cls')

r = str(input(' Deseja continuar ? \n escolha s pra sim e n para não: '))
if r == 's':
    print('')
    print(' Calculo de média \n obs: -\'Como se nunca tivesse feito esse exe\' ')
    print('')
    no = input(' Qual o nome do aluno: ')
    print('')
    n1 = float(input(' Digite a primeira nota do {}: '.format(no)))
    print('')
    n2 = float(input(' Digite a segunda nota do {}: '.format(no)))
    m = (n1+n2)/2
    if m>= 6.0:

        print(' Aprovado')
    else:
        print(' Reprovado')
        time.sleep(0.5)
        print('')
        print('-'*15)
        print('')
    r = str(input(' Deseja continuar ? \n escolha s pra sim e n para não: '))
    if r == 's': 
        print('')
        os.system('cls')
        print('...Continuando')
        time.sleep(3)
        print(' Sorry I\'m tired' )
        print(' Bey - bey \'-\' ') 
    else:
        time.sleep(0.5)
        print(' Tchau \'-\' ')
        time.sleep(1)
        os.system('cls')  
else:
    time.sleep(0.5)
    print(' Tchau \'-\' ')
    time.sleep(1)
    os.system('cls')    