# work of image processing
# students:  André Assunção Pinheiro and Lendel Moura Sanches


# dictionary
# interpolation = interpolação
# neighbors = vizinhos
# NearestNeighbors = vizinhos mais proximos
# reduction = redução
# reduced = reduzida

# from Interpolacao.interpolacaoBilinear import InterpolacaoBilinear
from rotulacao import Rotulacao

class Main():
    # arq = InterpolacaoBilinear('../img/pinguim.jpg')
    def __init__(self):
        print('---- init ---')
        self.rotulacao = Rotulacao('img/pata.jpg')
        self.rotulacao.executa()
        # self.rotulacao.print_img_matriz_binaria()
        # self.nearest_neighbors.enlargement()


main = Main()
# main.nearest_neighbors.reduction()
# main.nearest_neighbors.enlargement()
