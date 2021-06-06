
# Llamamos a la función numpy
import numpy as pn
# Escribimos la función para buscar
x=pn.pi/3
# Como se debe truncar hasta 50 ponemos 51 para que nos salgan todos los valores
n=51
# Inicializamos la función en 0
Funcion=0
print("")
print("Truncamiento con Tylor")
print("")
# T representa el numero de truncamiento y F(x) los resultados
print("T |     F(x)")
print("--------------------")
# Con esta función desarrollamos el ejercicio
for  T  in  range(n):
     Funcion=Funcion+(-1)**T*x**(2*T+1) /pn.math.factorial(2*T+1)
     print(T,Funcion)
