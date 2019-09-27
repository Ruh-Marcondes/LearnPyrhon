#idade
import time
atual = int(input("Desculpe ñ estou conseguindo ascessar os dados sobre o ano atual... Porfavor me informe: \n"))
print("")
ano = int(input("E em que ano você nasceu? \n"))
idade = atual - ano
print("Sua idade é: {}, caso já tenha feito aniversário se não {} ".format(idade,idade - 1))        
time.sleep(2)