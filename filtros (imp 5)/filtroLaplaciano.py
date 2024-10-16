import cv2
import numpy as np

img = cv2.imread('/home/jeovabarbosa/Processamento-de-Imagens-UFT/filtros (imp 5)/imagem.jpeg', cv2.IMREAD_GRAYSCALE)

def filtro_laplaciano(img, mascara):
    # Aplicando a máscara laplaciana
    img_filtrada = cv2.filter2D(img, -1, mascara)
    
    # Tratando valores negativos (opção 1: atribuindo 0)
    img_filtrada[img_filtrada < 0] = 0
    
    # Opcional: Escalando para o intervalo [0, 255] (opção 2)
    img_filtrada = cv2.normalize(img_filtrada, None, 0, 255, cv2.NORM_MINMAX)
    
    return img_filtrada

# Definindo as máscaras
mascara_1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
mascara_2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
mascara_3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
mascara_4 = np.array([[2, -1, 2], [-1, -4, -1], [2, -1, 2]])

# Aplicando as diferentes máscaras
img_laplaciano_1 = filtro_laplaciano(img, mascara_1)
img_laplaciano_2 = filtro_laplaciano(img, mascara_2)
img_laplaciano_3 = filtro_laplaciano(img, mascara_3)
img_laplaciano_4 = filtro_laplaciano(img, mascara_4)

# Exibindo as imagens resultantes
cv2.imshow('Laplaciano Mascara 1', img_laplaciano_1)
cv2.imshow('Laplaciano Mascara 2', img_laplaciano_2)
cv2.imshow('Laplaciano Mascara 3', img_laplaciano_3)
cv2.imshow('Laplaciano Mascara 4', img_laplaciano_4)
cv2.waitKey(0)
cv2.destroyAllWindows()