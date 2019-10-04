#!/usr/bin/env python3

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys

class Veiculo():
    def __init__(self, placa, consumo):
        self.placa = placa
        self.consumo = consumo

if __name__ == "__main__":
    veiculos = []

    while True:
        linha = input()
    
        if linha in '0':
            break
 
        media = 0
        cont = 0
        
        n = int(linha)

        for x in range(0,n):
            linha = input()
            temp = linha.split(" ")
            consumo = float(temp[1]) / float(temp[2])
            veiculos.append(Veiculo(temp[0],consumo))
            media += consumo
            cont += 1

        media /= cont
        
        for vc in veiculos:
            if vc.consumo < media:
                print("%s" % (vc.placa))

    sys.exit()
        