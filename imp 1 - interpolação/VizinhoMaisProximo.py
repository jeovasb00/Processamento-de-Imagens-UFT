from PIL import Image
import numpy as np

#A classe VizinhoMaisProximo encapsula toda a funcionalidade necessária para executar a interpolação por vizinho mais próximo.

class VizinhoMaisProximo():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem  #nome_imagem: Armazena o nome do arquivo da imagem
		self.m = 0  #m: Armazenam a altura da imagem.
		self.n = 0 #n: Armazena a largura da imagem.
		self.matriz = []  #matriz: Armazena a imagem como uma matriz numpy (grayscale).
		self.img = []  #img: Armazena o objeto imagem da PIL.

	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregaImagem(self):
		img = Image.open(self.nome_imagem) 
		self.img = img
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 1)
		#Dimensão N
		self.n = np.size(self.matriz, 0)
		print(f"Linhas: {self.m}\nColunas: {self.n}\n")
		print(self.matriz)

	'''
	Vizinho Mais Próximo por redução
	'''
	def reducao(self):
		saida = np.zeros([self.m//2,self.n//2]) #divide a matriz pela metade
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print(f"Linhas: {m1}\nColunas: {n1}\n")

		#Determina o tamanho tamM e tamN para a iteração, ajustando para dimensões ímpares.
		tamM = self.m-1 if self.m/2 != 0 else self.m
		tamN = self.n-1 if self.n/2 != 0 else self.n

		#Percorre a matriz original em passos de 2 (para selecionar apenas os pixels que devem ser mantidos na imagem reduzida).
		for i in range(tamM): 
			for j in range(tamN):
				if i%2 == 0 and j%2 == 0:
					saida[i//2][j//2] = self.matriz[i][j] #Atribui o valor do pixel da matriz original ao pixel correspondente na matriz de saída.

		#exibe a matriz
		print(saida) 
		imagem = Image.fromarray(saida)
		self.img.show()		
		imagem.show()


	# Vizinho Mais Próximo por Ampliação

	def ampliacao(self):
		#Criando nova matriz com o dobro de tamanho com dimensões M*2xN*2
		saida = np.zeros([self.m*2,self.n*2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print(f"Linhas: {m1}\nColunas: {n1}\n")


		#Percorre a nova matriz saida para preenchê-la: 
		for i in range(m1):
			for j in range(n1):
				if j%2 == 0 and i%2 == 0: #Se tanto i quanto j são pares, copia o valor do pixel correspondente na matriz original.
					saida[i][j] = self.matriz[i//2][j//2]
				elif j!=0 and j%2 != 0: #Se j é ímpar, copia o valor do pixel anterior na mesma linha (j-1).
					saida[i][j] = saida[i][j-1]
				if i%2 != 0: #Se i é ímpar, copia o valor do pixel na linha anterior (i-1).
					saida[i][j] = saida[i-1][j]
				
		

		print(saida)
		imagem = Image.fromarray(saida)		
		self.img.show()
		imagem.show()