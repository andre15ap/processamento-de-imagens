
# dictionary
# reduction = redução
# reduced = reduzida
# enlargement = ampliação
# enlarged = ampliada
# matrix = matriz
# width = largura
# height = altura


from PIL import Image
import numpy as np


class Bilinear:
    def __init__(self, img):
        self.image = self.getImage(img)
       
    def getImage(self, name_img):
        image = Image.open(name_img)
        # converter para tons de cinza
        # convert to grayscale
        return image.convert('L')

    def reduction(self, matrix, n):
        matrix_reduced = []

        for i in range(0, self.image.width, 2):
            for j in range(0, self.image.height, 2):
                if i+1 < self.image.width and j+1 < self.image.height:
                    matrix_reduced.append((matrix[i, j] + matrix[i, j+1] + matrix[i+1, j] + matrix[i+1, j+1]) / 4)

        
        return matrix_reduced

    # def ampliar(self):
    #     img_ampliada = Image.new('L', (int(self.imagem.width * 2), int(self.imagem.height * 2)))

    #     aux = img_ampliada.load()
    #     pixel = self.imagem.load()
    #     x = 1
    #     y = 0

    #     for i in range(0, self.imagem.height):
    #         for j in range(0, self.imagem.width):
    #             aux[i*2, j*2] = pixel[i, j]

    #     for i in range(0, self.imagem.height):
    #         for j in range(0, self.imagem.width-1):
    #             aux[x, y] = int((pixel[j, i] + pixel[j+1, i]) / 2)
    #             x += 2
    #         x = 1
    #         y += 2

    #     x = 0
    #     y = 1
    #     for i in range(0, self.imagem.height-1):
    #         for j in range(0, self.imagem.width):
    #             aux[x, y] = int((pixel[j, i] + pixel[j, i+1]) / 2)
    #             x += 2
    #         x = 0
    #         y += 2

    #     x = y = 1
    #     for i in range(0, self.imagem.height-1):
    #         for j in range(0, self.imagem.width-1):
    #             aux[x, y] = int((pixel[j, i] + pixel[j, i+1] + pixel[j+1, i] + pixel[j+1, i+1]) / 4)
    #             x += 2
    #         x = 1
    #         y += 2

    #     for i in range(img_ampliada.width):
    #         aux[i, img_ampliada.height - 1] = aux[i, img_ampliada.height - 2]

    #     for i in range(img_ampliada.height):
    #         aux[img_ampliada.width - 1, i] = aux[img_ampliada.width - 2, i]

    #     img_ampliada.save('ampliadaBIL.png')
    #     return img_ampliada

    # def resolver(self):
    #     img1 = self.ampliar()
    #     img1.show()

    #     tamanho = int(self.largura / 2), int(self.altura / 2)
    #     dados = list(self.imagem.getdata())
    #     matriz = np.reshape(dados, (self.largura, self.altura))

    #     nova_img = self.reduzir(matriz, 2)
    #     img_reduzida = Image.new('L', tamanho)
    #     img_reduzida.putdata(nova_img)
    #     img_reduzida.save('reduzidaBIL.png')
    #     img_reduzida.show()
