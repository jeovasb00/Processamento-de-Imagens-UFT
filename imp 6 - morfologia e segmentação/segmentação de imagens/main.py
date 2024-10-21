import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem em escala de cinza
img = cv2.imread('/home/jeovabarbosa/Processamento-de-Imagens-UFT/imp 6 - morfologia e segmentação/segmentação de imagens/img.jpg', cv2.IMREAD_GRAYSCALE)

# Função para calcular o histograma
def calcular_histograma(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist

# Função para encontrar o limiar pelo método do vale
def encontrar_limiar_vale(hist):
    # Encontrando os picos
    picos = []
    for i in range(1, len(hist) - 1):
        if hist[i] > hist[i - 1] and hist[i] > hist[i + 1]:
            picos.append(i)
    
    if len(picos) < 2:
        raise Exception("Não foi possível encontrar dois picos significativos no histograma.")

    # Buscando o vale (mínimo) entre os dois picos mais proeminentes
    vale = picos[0]
    minimo_valor = hist[vale]
    
    # Iterando entre os dois picos para encontrar o menor valor (vale)
    for i in range(picos[0], picos[1]):
        if hist[i] < minimo_valor:
            minimo_valor = hist[i]
            vale = i
    
    return vale

# Função de segmentação baseada no limiar encontrado
def segmentar_por_limiar(img, limiar):
    # Aplicar o limiar na imagem
    _, img_segmentada = cv2.threshold(img, limiar, 255, cv2.THRESH_BINARY)
    return img_segmentada


# Calcular o histograma da imagem
hist = calcular_histograma(img)

# Encontrar o limiar usando o método do vale
limiar = encontrar_limiar_vale(hist)

# Aplicar a segmentação
img_segmentada = segmentar_por_limiar(img, limiar)

# Exibir resultados
plt.figure(figsize=(10,5))

# Histograma
plt.subplot(1, 2, 1)
plt.plot(hist)
plt.title('Histograma da Imagem')

# Imagem segmentada
plt.subplot(1, 2, 2)
plt.imshow(img_segmentada, cmap='gray')
plt.title(f'Segmentação com limiar: {limiar}')

plt.show()

cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Segmentada', img_segmentada)
cv2.waitKey(0)
cv2.destroyAllWindows()