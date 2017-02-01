# Programa que coloca los elementos de un vector en otro.
n = input("Cantidad de Veces ")
vector = []

for i in range (n):
    elemento = input("Indique un valor ")
    vector.append(elemento)
    
vector2 = vector[:]
print "Nueva lista ",vector2
