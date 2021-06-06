# Ejercicio 2 del deber N°1 de Metodos númericos.

import numpy as np
print("\n")
print ("                   Matriz 2x2")
print("\n")
print ("Ingresar los valores de la matriz:")
print("\n")
print ("|a b|")
print ("|c d|")
print("\n")

# Ingresamos los valores de la matriz 2X2

a = float( input ('Ingrese el valor de a : '))
b = float( input ('Ingrese el valor de b : '))
c = float( input ('Ingrese el valor de c : '))
d = float( input ('Ingrese el valor de d : '))

# Diseñamos y mostramos la matriz con numpy

print("\n")
new_matrix = np.matrix([[a,b],[c,d]])
print("Matriz: ")
print(new_matrix)

# calculamos la matriz inversa con la función de numpy y mostramos

print("\n")
print("Matriz Inversa: ")
x=np.linalg.inv(new_matrix)
print(x)