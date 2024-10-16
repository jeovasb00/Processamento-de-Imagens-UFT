import cv2
import numpy as np

# Função para aplicar o Filtro da Média
def filtro_media(img, kernel_size=3):
    # Criando a máscara (kernel) da média
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    
    # Aplicando o filtro
    img_filtrada = cv2.filter2D(img, -1, kernel)
    
    return img_filtrada

# Carregar imagem em escala de cinza
img = cv2.imread('/home/jeovabarbosa/Processamento-de-Imagens-UFT/filtros (imp 5)/imagem.jpeg', cv2.IMREAD_GRAYSCALE)

# Aplicando o Filtro da Média com uma máscara de 3x3
img_media = filtro_media(img, 3)

# Exibindo a imagem original e filtrada
cv2.imshow('Original', img)
cv2.imshow('Filtro da Media', img_media)
cv2.waitKey(0)
cv2.destroyAllWindows()
