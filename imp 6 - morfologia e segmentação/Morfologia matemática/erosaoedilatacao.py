import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar uma imagem em tons de cinza
# Substitua 'imagem_tons_cinza.jpg' pelo caminho da sua imagem
imagem = cv2.imread('/home/jeovabarbosa/Processamento-de-Imagens-UFT/imp 6 - morfologia e segmentação/Morfologia matemática/fotografo.png', cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    raise Exception("Erro ao carregar a imagem.")

# Definir o elemento estruturante (kernel)
# Um kernel quadrado 5x5 é comum, mas você pode ajustar conforme necessário
kernel = np.ones((5, 5), np.uint8)

# Aplicar Erosão
imagem_erosao = cv2.erode(imagem, kernel, iterations=1)

# Aplicar Dilatação
imagem_dilatacao = cv2.dilate(imagem, kernel, iterations=1)

# Exibir os resultados
plt.figure(figsize=(15,5))

# Imagem original
plt.subplot(1, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')

# Imagem erodida
plt.subplot(1, 3, 2)
plt.imshow(imagem_erosao, cmap='gray')
plt.title('Erosão')

# Imagem dilatada
plt.subplot(1, 3, 3)
plt.imshow(imagem_dilatacao, cmap='gray')
plt.title('Dilatação')

plt.show()

# Opcional: salvar as imagens resultantes
cv2.imwrite('/home/jeovabarbosa/Processamento-de-Imagens-UFT/imp 6 - morfologia e segmentação/Morfologia matemática/imagem_erosao.jpg', imagem_erosao)
cv2.imwrite('/home/jeovabarbosa/Processamento-de-Imagens-UFT/imp 6 - morfologia e segmentação/Morfologia matemática/imagem_dilatacao.jpg', imagem_dilatacao)