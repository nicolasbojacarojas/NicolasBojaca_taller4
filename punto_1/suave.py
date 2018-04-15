import numpy as np
import matplotlib.pyplot as plt
#variables que van a ser tomadas en la funcion gaussiana
b = 2
sigma = 1
#funcion que toma un arreglo dado y devuelve un valor correspondiente a este una vez se le ha aplicado la funcion gaussiana 
def func_gau(x, b, sigma):
	return np.exp(-(x-b)**2/(2*sigma**2))
#lectura de la imagen a suavizar
foto=plt.imread("imagen.png")
#se toman los valores arrojados de la funcion sobre el arreglo de la imagen, los cuales corresponden a una imagen suavizada
suave = func_gau(foto, b, sigma)
#grafica de la imagen sobre los nuevos valores suavizados
plt.imshow(suave)
plt.savefig("suave")







