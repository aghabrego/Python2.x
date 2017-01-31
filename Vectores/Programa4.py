# Programa que determina el mayor elemento de un vector.
n = input("Cantidad de Veces ")
vector = []
mayor = 0

for i in range(n):
    elemento = input("Indique un numero ")
    vector.append(elemento)
    i = i + 1
    
for i in range(n):
    if vector[i] > mayor:
        mayor = vector[i]

print "El valor mayor es ",mayor
