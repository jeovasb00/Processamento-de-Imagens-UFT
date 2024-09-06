from VizinhoMaisProximo import VizinhoMaisProximo
from InterpolacaoBilinear import Interpolacao_Bilinear

if __name__ == '__main__':

	vizinho = VizinhoMaisProximo("PI01NNBI\\imagens\\imagemteste.png")
	vizinho.carregaImagem()
	interpolacao = Interpolacao_Bilinear("PI01NNBI\\imagens\\imagemteste.png")
	interpolacao.carregaImagem()

	n = -1

	menuStr = "\n\nMenu:\n"
	menuStr += "Vizinho Mais Próximo\n1 - Por Redução\n2 - Por Ampliação\n\n"
	menuStr += "Interpolação Bilinear\n3 - Para Redução\n4 - Para Ampliação\n\nDigite 0 para sair."

	while n != 0:
		n = input(menuStr)
		n = int(n)
		if n == 1:
			vizinho.reducao()
		elif n == 2:
			vizinho.ampliacao()
		elif n == 3:
			interpolacao.reducao()
		elif n == 4:
			interpolacao.ampliacao()
