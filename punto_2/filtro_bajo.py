import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftshift, ifft2, ifftshift 
#lectura de imagen
foto = plt.imread("imagen.png")
#aplicacion de transformada de fourier al arreglo generado por la imagen
freq = fft2(foto)
#Valores para aplicar la suavizacion sobre la imagen
b = 2
sigma = 1
#Variable para indicar los valores de las frecuencias que se quieren dejar pasar
fcorte = 100
#funcion que suaviza la imagen
def func_gau(x, b, sigma):
	return np.exp(-(x-b)**2/(2*sigma**2))
#nfil, ncol = foto.shape()
freqs = fftshift(freq)
#frecuencias que quiero que deje pasar el filtro en valor absoluto
freqs[abs(freqs)<fcorte] = 0
#aplicacion de la inversa de la transformada de fourier
freqis = ifftshift(freqs)
itf = ifft2(freqis)
#tomo solo las frecuencias con valor absoluto
ifta = np.abs(itf)
#paso las frecuencias a graficar por la funcion que suaviza la imagen 
grafica = func_gau(ifta, b, sigma)
#grafico las frecuencias una vez se encuentran suavizadas
plt.imshow(grafica)
plt.savefig("bajas")
