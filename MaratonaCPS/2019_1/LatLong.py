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
 
        temp = linha.split(";")
        temp1 = temp[0].split(" ")
        temp2 = temp[1].split(" ")
        
        a = temp1[0]
        lat = float(a[:len(a)-1])
        a = temp2[0];
        lon = float(a[:len(a)-1])

        if len(temp1) > 1:
            a = temp1[1]
            lat += float(a[:len(a)-1]) / 60
            if len(temp1) > 2:
                a = temp1[2]
                lat += float(a[:len(a) - 1]) / 3600

        if len(temp2) > 1:
            a = temp2[1]
            lon += float(a[:len(a) - 1]) / 60
            if len(temp2) > 2:
                a = temp2[2]
                lon += float(a[:len(a) - 1]) / 3600

        if lat < 0:
            latitude = "Sul"
        elif lat == 0:
            latitude = "Equador"
        else:
            latitude = "Norte"

        if lon < 0:
            longitude = "Oeste"
        elif lon == 0:
            longitude = "Greenwich"
        else:
            longitude = "Leste"

        print("%s %s" % (latitude, longitude))
        
    sys.exit()