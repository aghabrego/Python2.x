# -*- coding: cp1252 -*-
# Programa que lee n valores y los colocas en posiciones pares del vector y escribe 0 en las posiciones impares.
n = input("Cantidad de Veces ")
i = 0
vec = []

while i < n:
    num = raw_input("Indique un valor ")

    if i % 2 == 0:
        vec.append(num)
    else:
        vec.append(0)
    i=i+1

print vec
