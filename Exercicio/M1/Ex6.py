#IMC
print("Vou calcular seu IMC (Índice de Massa Corpórea)")
p = float(input("Digite seu peso: \n"))
a = float(input("Digite sua altura: \n"))
imc = (p/a**2)
print("Seu IMC é: {}".format(imc))
