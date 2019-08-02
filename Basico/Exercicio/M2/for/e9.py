'''
algoritimo para calcular a soma entre números ímpares 
que são múltiplos de três e que se encontram 
no intervalo de 1 até 500.              '-'
'''

s = 0
for c in range(0,300,+3):
    if c%2 == 0:
        s = s + c
print(f'{s}')
