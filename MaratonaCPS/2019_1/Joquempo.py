#!/usr/bin/env python3

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys

if __name__ == "__main__":

    while True:
        linha = input()
    
        if linha in '0':
            break
                
        n = int(linha)
        
        joao = 0
        pedro = 0

        for x in range(0,n):
            linha = input()
            temp = linha.split(" ")
            ganhador = 0
            if temp[1]=="pedra":
                if temp[3]=="tesoura":
                    ganhador = 0
                else:
                    ganhador = 1
            if temp[1]=="papel":
                if temp[3]=="pedra":
                    ganhador = 0
                else:
                    ganhador = 1
            if temp[1]=="tesoura":
                if temp[3]=="papel":
                    ganhador = 0
                else:
                    ganhador = 1
                    
            if temp[0]=="Pedro":
                if ganhador==0:
                    pedro += 1
                else:
                    joao += 1
            else:
                if ganhador==0:
                    joao += 1
                else:
                    pedro += 1
                
        if joao==pedro:
            print("Empate")
        else:
            if joao > pedro:
                print("%s %i" % ("Joao",joao))
            else:
                print("%s %i" % ("Pedro",pedro))

    sys.exit()
