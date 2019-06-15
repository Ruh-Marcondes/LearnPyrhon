#quartos de 1 a  n
from time import time
from os import system 

# Algoritimo principal

n = open('portas.in','r')

s = open('portas.out','w')
 
for line in n:
    splitted_line = line.split(' ')
    for values in splitted_line:
        value_as_int = int(values)


while True:
    if value_as_int > 0:
        i = 0
        while i < value_as_int:
            i += 1
            h = i * value_as_int 
            if h < value_as_int:
                print(f'{h}')
            else:
                break
    else:
        break

