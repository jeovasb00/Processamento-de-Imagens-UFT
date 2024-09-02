from PIL import Image #biblioteca para manipulação de imagens
import numpy as np #biblioteca usada para operações de matriz.

#A classe InterpolacaoBilinear é responsável por manipular a imagem. No método __init__, são inicializados atributos como o nome da imagem (nome_imagem), 
#as dimensões da imagem (m e n), a matriz que representa os pixels da imagem (matriz), e a imagem propriamente dita (img).

class InterpolacaoBilinear():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem
		self.m = 0
		self.n = 0
		self.matriz = []
		self.img = []

#Este método carrega a imagem e converte-a para uma matriz de pixels em tons de cinza ('L' significa grayscale). Ele também define as dimensões da imagem (m e n) e imprime a matriz da imagem.
	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregarImagem(self):
		img = Image.open(self.nome_imagem)
		self.img = img
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 1)
		#Dimensão N
		self.n = np.size(self.matriz, 0)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)


#Este método realiza a redução da imagem usando interpolação bilinear. Ele cria uma nova matriz (saida) com metade das dimensões originais. Para cada bloco 2x2 na matriz original, 
#o método calcula a média dos quatro pixels para determinar o valor do pixel correspondente na imagem reduzida. O resultado é então exibido.

	'''
	Interpolação Bilinear para Redução
	'''
	def paraReducao(self):
		saida = np.zeros([self.m//2,self.n//2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#Ternário em Python
		tamM = self.m-1 if self.m/2 != 0 else self.m
		tamN = self.n-1 if self.n/2 != 0 else self.n

		#Blocos 2x2 de pixels na imagem original são combinados em um único pixel na imagem reduzida. Interpolação bilinear usa a média desses 4 pixels para calcular o valor do novo pixel. 
		#A imagem resultante é suavemente reduzida em tamanho, preservando a informação visual de forma contínua.

		for i in range(0,tamM,2):
			for j in range(0,tamN,2):
				x = self.matriz
				if i < tamM and j < tamN:
					soma = int(x[i][j]) + int(x[i][j+1]) + int(x[i+1][j]) + int(x[i+1][j+1])
					saida[i//2][j//2] = int(soma/4)

											
		print(saida)
		imagem = Image.fromarray(saida)		
		self.img.show()
		imagem.show()

	'''
	Interpolação Bilinear para Ampliação
	Ainda a fazer, código abaixo é do Vizinho mais próx
	'''
	def paraAmpliacao(self):
		#Criando nova matriz com dimensões M*2xN*2
		#A nova matriz é criada com o dobro do tamanho da original.
		saida = np.zeros([self.m*2,self.n*2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

     #Os pixels que correspondem diretamente aos pixels da matriz original são copiados.
		for i in range(m1-1):
			for j in range(n1-1):
				#Se coluna j é par, então saida[i][j] = matriz[metade][metade]
				if j%2 == 0 and i%2 == 0:
					saida[i][j] = self.matriz[int(i/2)][int(j/2)]


	
		for i in range(m1-1):
			for j in range(n1-1):
    			#Os pixels restantes são preenchidos com valores interpolados com base nos pixels vizinhos.
				#Se c, c = (f(i,j) + f(i,j+1) + f(i+1,j) + f(i+1,j+1))/4
				if i%2 != 0 and j%2 != 0:
					soma = int(saida[i-1][j-1]) + int(saida[i-1][j+1])
					soma += int(saida[i+1][j-1]) + int(saida[i+1][j+1])
					saida[i][j] = int(soma/4)
					
				#Este bloco preenche os pixels na horizontal, calculando a média entre os pixels à esquerda e à direita (horizontais) da nova matriz.
				#Se a ou e, a = (f(i,j) + f(i,j+1))/2
				elif i%2 == 0 and j%2 != 0:
					saida[i][j] = int((int(saida[i][j-1]) + int(saida[i][j+1])) /2)
				#Se b ou d, b = (f(i,j+1) + f(i+1,j+1))/2
				elif i%2 != 0 and (i-1)%2 == 0:
					saida[i][j] = int((int(saida[i-1][j]) + int(saida[i+1][j])) /2)
				#Tratamento da última coluna
				if i == (m1-2):
					saida[m1-1][j] = saida[i][j]
				#Tratamento da última linha
				if j == (n1-2):
					saida[i][n1-1] = saida[i][j]
					
		#Tratamento do último pixel: Matriz[M][N]
		saida[m1-1][n1-1] = saida[m1-1][n1-2]

		print(saida)
		imagem = Image.fromarray(saida)		
		self.img.show()
		imagem.show()