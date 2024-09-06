from VizinhoMaisProximo import VizinhoMaisProximo
from InterpolacaoBilinear import Interpolacao_Bilinear

if __name__ == '__main__':

	vizinho = VizinhoMaisProximo("PI01NNBI\\imagens\\imagemteste.png")
	vizinho.carregaImagem()
	interpolacao = Interpolacao_Bilinear("PI01NNBI\\imagens\\imagemteste.png")
	interpolacao.carregaImagem()

	op = -1

	menuStr = "\n\nMenu:\n"
	menuStr += "Vizinho Mais Próximo\n1 - Por Redução\n2 - Por Ampliação\n\n"
	menuStr += "Interpolação Bilinear\n3 - Para Redução\n4 - Para Ampliação\n\nDigite 0 para sair."

	while op != 0:
		op = input(menuStr)
		op = int(op)
		if op == 1:
			vizinho.reducao()
		elif op == 2:
			vizinho.ampliacao()
		elif op == 3:
			interpolacao.reducao()
		elif op == 4:
			interpolacao.ampliacao()

	print("Fim execução!!")
