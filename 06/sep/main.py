import numpy as np
import pylab as pl
# Crear un vector (arreglo) con los valores del eje X
x = [6000, 7000, 8000, 9000, 10000]
# Crear un vector (arreglo) con los valores en el eje Y para cada valor en el eje x
y = [73, 80, 85, 87, 89]
# Grafica el vector x cotra el vector Y

pl.plot (x, y)

# Crear un vector (arreglo) con los valores del eje X
x1 = [7000, 8000, 9000, 10000, 11000]

# Crear un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y2 = [73, 85, 89, 93, 95]
# Grafica el vector x contra el vector y

pl.plot (x1, y2)

pl.xlabel('Voltaje [V]')
pl.ylabel('Eficiencia [%]')
# Guardar la grafica en formato png
pl.savefig( 'temp1.png' )

