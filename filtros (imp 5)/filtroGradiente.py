import cv2
import numpy as np

img = cv2.imread('/home/jeovabarbosa/Processamento-de-Imagens-UFT/filtros (imp 5)/imagem.jpeg', cv2.IMREAD_GRAYSCALE)

def filtro_sobel(img):
    # Aplicando Sobel horizontal e vertical
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    # Magnitude do gradiente
    sobel = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Escalando para [0, 255]
    sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
    
    return sobel

# Aplicando o Filtro de Sobel
img_sobel = filtro_sobel(img)

# Exibindo a imagem do gradiente
cv2.imshow('Filtro Sobel', img_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()