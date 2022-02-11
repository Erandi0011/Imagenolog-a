# -*- coding: utf-8 -*-


#Gray level Transformation
# S = (L-1)-R 
# L= Max intensity an image can carry
# 256 (2^8)
# R =intensity of pixel

from skimage import data
import numpy as np
import matplotlib.pyplot as plt



gris= data.camera()#Imagen

plt.figure(0)
plt.imshow(gris, cmap = 'gray')#Mostrar en gris

histo = np.zeros(256)
histo1 =np.zeros(256)
histo2 =np.zeros(256)
filas = gris.shape[0]
columnas =  gris.shape[1]
salida = np.zeros((filas,columnas))
salida2 = np.zeros((filas,columnas))
print(salida.shape)


for i in range(filas):
  for j in range(columnas):
    pixel = gris[i,j]
    histo[pixel] +=1 #Histograma Original    
plt.figure(1)
plt.plot(histo)
    
for i in range(filas):
  for j in range(columnas):
    salida[i,j]= gris[i,j]+30
    if salida[i,j]< 200:
       salida[i,j]=0 
    if salida[i,j] > 255:
       salida[i,j]=255
      
plt.figure(2)
plt.imshow(salida, cmap = 'gray')#Imagen transformmada


for i in range(filas):
  for j in range(columnas):
    pixel1 = int(salida[i,j])
    histo1[pixel1] +=1 #Histograma    
plt.figure(3)
plt.plot(histo1)

#___________________


for i in range(filas):
  for j in range(columnas):
    salida2[i,j]= gris[i,j]-50
    if salida2[i,j]> 100:
       salida2[i,j]=255
    if salida2[i,j] <0:
       salida2[i,j]=0
      
plt.figure(4)
plt.imshow(salida2, cmap = 'gray')#Imagen transformmada


for i in range(filas):
  for j in range(columnas):
    pixel2 = int(salida2[i,j])
    histo2[pixel2] +=1 #Histograma    
plt.figure(5)
plt.plot(histo2)