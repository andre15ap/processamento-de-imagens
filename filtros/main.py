from laplaciano import Filtros


class Main():
    # arq = InterpolacaoBilinear('../img/pinguim.jpg')
    def __init__(self):
        print('---- init ---')
        self.filtros = Filtros('img/bial.jpg')
        self.filtros.laplaciano()
        # self.filtros.gradiente()
    


main = Main()
    