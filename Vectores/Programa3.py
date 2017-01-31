# -*- coding: cp1252 -*-
#programa que calcula el producto de los elementos de un vector que están en las
#posiciones impares
vec = [10,5,4,5,3,10]
pro = 1

for i in range(6):
    if i % 2 <> 0:
        pro = pro * vec[i]

print "Productor de posicion impar ",pro
    
