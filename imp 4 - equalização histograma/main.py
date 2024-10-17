from PIL import Image
import matplotlib.pyplot as plt

def plot_histogram(image, title):
    # Calcula a frequência dos níveis de cinza
    histogram = [0] * 256
    width, height = image.size

    for i in range(width):
        for j in range(height):
            gray_value = image.getpixel((i,j))
            histogram[gray_value] += 1

    # Plot do histograma
    plt.figure()
    plt.title(title)
    plt.bar(range(256), histogram, color='gray')
    plt.xlabel('Níveis de Cinza')
    plt.ylabel('Frequência')
    plt.show()

# Carregando a imagem
img = Image.open('lena.png')
grayscale_image = img.convert('L')
grayscale_image.save('lena-greyscale.png')

# Dimensões da imagem
width, height = grayscale_image.size
pixel_qtd = width * height

# Inicializa as listas
equalized_value = []
gray_levels_sums = [0] * 256
frequency_sum = 0

# Contagem da frequência de cada nível de cinza
for i in range(width):
    for j in range(height):
        gray_levels_sums[grayscale_image.getpixel((i,j))] += 1

# Calcula a nova tabela de valores equalizados ..........
for i in range(256):
    frequency = gray_levels_sums[i] / pixel_qtd
    frequency_sum += frequency
    equalized_value.append(round(frequency_sum * 255))

# Criando uma nova imagem para a equalizada
equalized_image = Image.new('L', (width, height))

# Aplica a equalização à imagem
for i in range(width):
    for j in range(height):
        original_value = grayscale_image.getpixel((i,j))
        equalized_image.putpixel((i,j), equalized_value[original_value])

# Salvando a imagem equalizada
equalized_image.save('equalized-lena.png')

# Plotando os histogramas
plot_histogram(grayscale_image, 'Histograma da Imagem Original')
plot_histogram(equalized_image, 'Histograma da Imagem Equalizada')
