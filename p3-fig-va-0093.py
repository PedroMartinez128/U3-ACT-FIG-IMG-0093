
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
# Pedro Martinez NC. 0093pip install matplotlib
print("\n  Pedro Martinez NC.0093")
print("\n UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imagen=cv2.imread("josejose_img.jpg")
plt.imshow(mi_imagen)
plt.title("Jose Jose y Pedro Martinez 0093")
plt.show()
print("\n +-+-+- puntos en la imagen -+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300,200,103]
y = [100,400,500,200,171]
plt.scatter(x,y,s=20,c="red")
plt.show()
print("\n +-+-+- Cuadro en la imagen-+-+-+")
mi_imagen = cv2.imread("josejose_img.jpg")
plt.imshow(mi_imagen)
# Las cordenadas originales
# x = [100, 100, 500, 500, 100]
# y = [500, 100, 100, 500, 500]

x = [170, 170, 380, 380, 170]
y = [320, 100, 100, 320, 320]
plt.plot(x,y,c="blue")
plt.show()
print("-+-+- circulo verde en la imagen")

I = cv2.imread("josejose_img.jpg")

# Mostrar imagen
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))

# Número de puntos
N = 30

# Crear arreglos
x = np.zeros((N+1,))
y = np.zeros((N+1,))

# Centro del círculo
(xc, yc) = (340, 320)

# Radio
r = 150

# Calcular coordenadas del círculo
for i in range(N+1):
    t = 2 * np.pi * i / N
    x[i] = xc + r * np.cos(t)
    y[i] = yc + r * np.sin(t)

# Dibujar círculo verde
plt.plot(x, y, c="green")
plt.title("Circulo verde en la imagen")
plt.show()