import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem binária (em tons de cinza)
# Substitua 'imagem_binaria.jpg' pelo caminho da sua imagem binária
imagem = cv2.imread('/home/jeovabarbosa/Processamento-de-Imagens-UFT/imp 6 - morfologia e segmentação/Morfologia matemática/hand.png', cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    raise Exception("Erro ao carregar a imagem.")

# Encontrar os contornos na imagem binária
# O segundo parâmetro define o método de detecção de contornos (cv2.RETR_EXTERNAL detecta apenas os contornos externos)
# O terceiro parâmetro define o método de aproximação de contornos (cv2.CHAIN_APPROX_SIMPLE armazena apenas os pontos de contorno essenciais)
contornos, hierarquia = cv2.findContours(imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Criar uma imagem em branco para desenhar os contornos
# A imagem será do mesmo tamanho da imagem original
imagem_contornos = np.zeros_like(imagem)

# Desenhar os contornos na imagem vazia (branca)
# O terceiro parâmetro -1 indica que todos os contornos encontrados serão desenhados
cv2.drawContours(imagem_contornos, contornos, -1, (255, 255, 255), 1)  # Desenhar contornos na cor branca (255)

# Exibir os contornos detectados
plt.figure(figsize=(10,5))

# Imagem original
plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Binária')

# Imagem com contornos
plt.subplot(1, 2, 2)
plt.imshow(imagem_contornos, cmap='gray')
plt.title('Contornos Extraídos')

plt.show()

# Opcional: salvar a imagem com contornos
cv2.imwrite('/home/jeovabarbosa/Processamento-de-Imagens-UFT/imp 6 - morfologia e segmentação/Morfologia matemática/contornos_extraidos.png', imagem_contornos)
