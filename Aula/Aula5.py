#do - While
'''
While True:
    ..
    ..
    ..
    if p == p:
        break
'''
# while 
# break - pode quebrar um laço
cont =  1
while cont <=10:
    cont += 1 
    print(cont)
print(' End ')

n = s = 0

while True:
    n = int(input(' Digite um número: '))
    if n == 999:
        break
    else:
        s += n
#print('\n  A soma dos números é {}'.format(s))
print(f' \n  A soma vale {s}')
    