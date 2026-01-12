import numpy as np

datos = np.array([2,2,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7])

#media
media = np.mean(datos)
print(f'Media : {media}')

#mediana
mediana = np.median(datos)
print(f'Mediana : {mediana}')

#moda
valores,conteos = np.unique(datos,return_counts=True)
moda = valores[np.argmax(conteos)]
print(f'Moda : {moda}')