# Ejercicio 3 del deber N°1 de Metodos númericos.

# Llamamos a la libreria

from matplotlib \
import pyplot

# Ponemos las Funciones para graficar.
def f(x):
    return x**2-x+1
def f2(x):
    return 2/1*x-1

# Aki se pone el rango de valores que puede tomar x para generar la grafica.
x = range(-20, 20)

# Con este metodo plot especificamos las funciónes que graficaremos.

pyplot.plot(x, [f(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])

# En este metodo le damos color a los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# En este metodo le damos los limites de los ejes.
pyplot.xlim(-21, 21)
pyplot.ylim(-21, 21)

# Con este metodo guardamos y exponemos el grafico mediante una imagen png.
pyplot.savefig("función_lineal.png")

# Copilamos el grafico.
pyplot.show()