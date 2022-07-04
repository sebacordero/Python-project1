# Tarea Herramientas Computacionales para Investigación. 
# Sebastián Ignacio Cordero

# Incluir los paquetes de pandas y de Numpy
import pandas as pd
import numpy as np

# 1.	leer el archivo csv “tarea” y mostrar las primeras 5 filas (.head()).
tarea = pd.read_csv('tarea.csv')
print(tarea.head(n=5))

# 2.	leer el archivo csv “tarea” y mostrar las primeras 3 filas (,nrows=3).
print(tarea.head(n=3))


# 3.	Imprime el contenido de una columna como serie (tan sólo imprimí la columna entre corchetes!)


# 4.	crear una nueva serie 'calidad-color' (utilizá corchetes para definir el nombre de la serie). 
# 5.	encontrar el número de filas y columnas (.shape)) y el tipo de datos de cada columna (.dtypes).
# 6.	resumir sólo las columnas 'objeto' (.describe(include=['object'])). 
# 7.	renombrar dos de las columnas (.rename(columns={…). Imprimir antes y después incluyendo una línea que describa cada una (ej print("Original"))
# 9.	eliminar múltiples filas a la vez (usar axis=0 que se refiere a las filas). 
# 8.	eliminar la segunda y tercer columna (.drop()).
# 10.	ordenar la columna `cut’ en orden ascendente (tarea.cut.sort_values). ¿Qué tipo de objeto es `cut’ usándolo así? 
# 11.	ordenar toda la base por 'carat' en orden descendente. 
# 12.	filtrar aquellas filas que x>5, y>5 y z>5.
# 13.	filtrar las filas para que sólo muestren `carat’ mayor a 0,4 (usar for x in tarea.carat:…)
# 14.	filtrar filas que son Premium o Ideal (tarea.cut.sin() o usar |). 
# 15.	calcular summary statistics de  `carat’ (.describe). 
# 16.	calcular la media de cada columna numérica (.mean()). 
# 17.	calcular la media del precio de cada tipo de `cut’ (tarea.groupby().price.mean()). 
# 18.	calcular la cantidad, el mínimo y el máximo precio para cada `cut’ ((tarea.groupby().price.agg([]))) . 

# 19.	mostrar los valores que puede tomar `cut’ (.unique()). 

# 20.	contar cuántas veces aparece cada valor de `cut’ ((tarea.cut.value_counts())) 

# 21.	mostrar los porcentajes de cada valor de `cut’. 
# 22.	calcular una tabla de doble entrada con `cut’ y `color’ (pd.crosstab)
# 23.	crear un histograma de ‘cut’ (.plot(kind=’hist’)). 
# 24.	crear un gráfico de barras de 'cut' . 
# 25.	contar el número de missing valies en cada columna (.isnull().sum()). 
# 26.	comprobar el número de filas y columnas y eliminarlas si falta algún valor en una fila (.dropna(how='any')).
# 27.	eliminar una fila si faltan todos los valores ((.dropna(how='all')). 
# 28.	mostrar las filas 0, 2, 5 y todas las columnas (.loc[]). 
# 29.	mostrar las filas 0 a 2 (inclusive) y las columnas 'color' y 'precio' . 
# 30.	mostrar las filas en las que la 'cut' es 'Premium' más la columna 'color'. 
# 31.	obtener 5 filas de muestra al azar (.sample()). 
# 32.	obtener una muestra del 75% de las filas sin reemplazarlas (.sample(frac=0.75, random_state=XX))
# 33.	contar las filas duplicadas.
