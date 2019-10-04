#!/usr/bin/env python3

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys

if __name__ == "__main__":
    ingredientes = [["Milho verde", 200, 0, 0,"Kg"], ["Oleo vegetal", 200, 120, 0,"L"],
    ["Acucar", 250, 360, 0,"Kg"], ["Fuba", 200, 0, 0,"Kg"], ["Ovos", 4, 4, 0,""],
    ["Farinha de trigo", 15, 240, 0,"Kg"], ["Coco ralado", 15, 100, 0,"Kg"],
    ["Fermento em po", 5, 10, 0,"Kg"], ["Leite de coco", 0, 200, 0,"L"]]

    while True:
        linha = input()
    
        if linha in '0':
            break
                
        n = int(linha)

        for x in range(0,n):
            linha = input()
            temp = linha.split(" ")
            milho = int(temp[0])
            coco = int(temp[1])
            for i in ingredientes:
                i[3] += i[1] * milho
                i[3] += i[2] * coco

        for i  in ingredientes:
            if i[4]=="":
                print("%s %i" % (i[0],i[3]))
            else:
                print("%s %i%s" % (i[0],i[3]/1000,i[4]))

    sys.exit()
