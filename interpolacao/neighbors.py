# work of image processing
# students:  André Assunção Pinheiro & Lendel Moura Sanches

# Interpolation


# dictionary
# nearest neighbors = vizihos mais proximos
# neighbors = vizinhos
# reduction = redução
# reduced = reduzida
# enlargement = ampliação
# enlarged = ampliada
# width = largura
# height = altura

from PIL import Image
import numpy as np


class NearestNeighbors:
    def __init__(self, img):
        self.image = self.get_image(img)

    def get_image(self, nome_img):
        image = Image.open(nome_img)

        # converter para tons de cinza
        # convert to grayscale
        return image.convert('L')  

    def show(self):
        self.image.show()
   
    def reduction(self):
        # cria imagem em branco, com metado do tamanho
        # create a blank image, half the size
        img_reduced = Image.new('L', (int(self.image.width / 2), int(self.image.height / 2)), color='white')
        # img_reduced.show()
        aux = img_reduced.load()
        pixel = self.image.load()
        x = y = 0
        print('height = {}, width = {}'.format(self.image.height, self.image.width))
        for i in range(0, self.image.height, 2):
            for j in range(0, self.image.width, 2):
                # print(' i = {}, j = {}'.format(i,j))
                aux[x, y] = pixel[i, j]
                y += 1
            y = 0
            x += 1

        img_reduced.save('img/neighbors_reduction.png')
        img_reduced.show()
        return img_reduced

    def enlargement(self):
        # cria imagem em branco, com o dobro do tamanho
        # create a blank image, double the size
        img_enlarged = Image.new('L', (int(self.image.width * 2), int(self.image.height * 2)), color='white')

        aux = img_enlarged.load()
        pixel = self.image.load()
        x = y = 0

        for column in range(0, img_enlarged.height, 2):
            for line in range(0, img_enlarged.width, 2):
                aux[column, line] = pixel[x, y]
                if line < img_enlarged.width:
                    aux[column, line+1] = pixel[x, y]
                if column < img_enlarged.height:
                    aux[column+1, line] = pixel[x, y]
                if column < img_enlarged.height and line < img_enlarged.width:
                    aux[column+1, line+1] = pixel[x, y]

                y += 1
            y = 0
            x += 1

        img_enlarged.save('img/neighbors_enlargement.png')
        img_enlarged.show()
        return img_enlarged