#idade
atual = int(input("Desculpe ñ estou conseguindo ascessar os dados sobre o ano atual... Porfavor me informe: \n"))
ano = int(input("E em que ano você nasceu? \n"))
idade = atual - ano
print("Sua idade é: {}, caso já tenha feito aniversário se não {} ".format(idade,idade - 1))        