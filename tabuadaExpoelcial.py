'''
Tabuada exponencial 
'''
from time import sleep

def base():
    n = int(input(' Escolha o número da base : '))
    for c in range(0,11):
        s = n**c
        print(f' {n} elevado a {c}  é  {s}')
        sleep (0.2)
 


def expoen():
     n = int(input(' Escolha o número do expoente: '))
     for c in range(0,11):
        s = c**n
        print(f' {c} elevado a {n}  é  {s}')
        sleep (0.2)
        


def opc():
    print(' Escolha uma opc:')
    print(' 1 ~~ Base')
    print(' 2 ~~ Expoente')
    print(' 0 ~~ Sair')
        
def p1():
    while True:
        print ('')
        opc()
        p = int(input(' '))
        if p !=0 and p != 1 and p != 2:
            print(' Escolhe certo!')
        elif p == 1:
            base ()
        elif p == 2:
           expoen()
        else:
            break
        
         
print(' ')        
print(" Tabuada Exponencial  '-' ")
print(' ')
p1()       
print(' ') 
print(' Fim do algoritmo  de tabuada exponencial')
print(" '-' ")