# Calculo da comissão
# n = nome
# p = Preço Unitário
# q = quantidade vendida
# t = total do valor vendido
# c = comissão de 5%
n = input("Digite o nome do funcionário: \n ")
p = float(input("Digite qual o válor unitário da peça: \n "))
q = int(input("Digite a quantidade vendida: \n "))
t = p*q
# Não se pode ter váriaveis com letra maiúscula
c = t*5/100
print(" O total recibido é R$ {}. \n Para o fúnciorio {} a comissão será {}.".format(t,n,c))
#fim do algoritimo
