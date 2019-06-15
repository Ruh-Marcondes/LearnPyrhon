#Condiçoes (P1)
# Simples e Compostas 
# If Else
# progrmas não são bipolares... Como eu...

from os import system
import time

def carinha():
    print(' \'-\' '*5)
    print('')


def carinha2():
    print('')
    print(' \'-\' '*5)


def tracinho():
    print('')
    print('-'*15)

def hello():
    n = str(input('Digite teu nome? \n '))
    if n == 'Ruahma':
        time.sleep(0.5)
        carinha()
        print(' Hello, {}, Bem - Vinda!'.format(n))
        carinha2()
    else:
        print('Hello, {}'.format(n))


def media():
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
        tracinho()


print('')
hello()
time.sleep(3)
system('cls')
print('')
while True:
    print(' OPC: ')
    p = int(input(' 1...Hello \n 2... Media 3.. Sair'))
    if p != 1 or p != 2 or p != 3:
        print(' Erro! \n Escolha outra opção')
    elif p == 1:
        hello()
    elif p == 3:
        media()
    else:
        break
    r = str(input(' Deseja continuar ? \n escolha s pra sim e n para não: '))
    if r == 's': 
        print('')
        system('cls')
        print('...Continuando')
        time.sleep(3)
        print(' Sorry I\'m tired' )
        print(' Bey - bey \'-\' ')
        break 
    else:
        time.sleep(0.5)
        print(' Tchau \'-\' ')
        time.sleep(1)
        system('cls')
        break