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


class Rotulacao:
    def __init__(self, img):
        self.image = self.get_image(img)
        self.pixels = []
        self.label = 1
        # self.size = 6
        self.size = self.image.width
        linha1 = [1,0,1,1,1,0]
        linha2 = [1,1,0,1,1,0]
        linha3 = [1,1,1,0,0,0]
        linha4 = [0,0,1,0,1,0]
        linha5 = [0,0,1,1,1,0]
        linha6 = [0,1,1,1,1,0]
        self.matrix_teste = [linha1,linha2,linha3,linha4,linha5,linha6]
       

    def get_image(self, nome_img):
        image = Image.open(nome_img)

        # converter para tons de cinza
        # convert to grayscale
        # return image  
        return image.convert('L')  

    def show(self):
        self.image.show()

    def pixel_pertence(self, x, y):
        # print(self.image.getpixel((x,y)))
        if self.image.getpixel((y,x)) < 160:
        # if self.matrix_teste[x][y] == 1:
            return True
        return False
    
    def print_img_matriz_binaria(self):
        for i in range(0, self.image.width):
            for j in range(0, self.image.height):
                if self.pixel_pertence(i,j):
                    print('-', end=' ')
                else:
                    print('0', end=' ')
            print('')

    def incremente_lebal(self, x,y):
        self.label +=1

    def executa(self):
        pixel = self.image.load()
       
        matrix = self.get_matrix_rotulos()
        
        iguais = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                # self.image.putpixel((i,j),100)
                rotulo = {}
                rotulo['p'] = (i,j)
                rotulo['l'] = 0
                

                matrix[i][j] = rotulo
               
                # se pixel atual pertence a sentenca
                if self.pixel_pertence(i,j):
                    if i == 0:
                        #i == 0 e j == 0 
                        if j == 0:
                            #so rotula
                            # print('--- entrou aqui i ={} j={} '.format(i,j))
                            matrix[i][j]['l'] = self.label
                            self.incremente_lebal(i,j)

                        # i == 0  e j != 0
                        else:
                            #verifica o J - 1 (o de traz)
                            if self.pixel_pertence(i,j-1):
                                matrix[i][j]['l'] = matrix[i][j-1]['l']
                            # se o de traz não pertence, adiciona nova label
                            else:
                                matrix[i][j]['l'] = self.label
                                self.incremente_lebal(i,j)

                    else:
                        # i != 0 e j == 0
                        if j == 0:
                            #verifica o i - 1 ( o de cima)
                            if self.pixel_pertence(i-1,j):
                                matrix[i][j]['l'] = matrix[i-1][j]['l']
                                
                            # se o de cima nao pertente, adiciona nova label
                            else:
                                matrix[i][j]['l'] = self.label
                                self.incremente_lebal(i,j)
                        # i != 0 e j != 0
                        else:
                            #verifica o j -1 e o i -1 ( de traz e de cima )
                            if self.pixel_pertence(i, j-1) and self.pixel_pertence(i-1, j):
                                matrix[i][j]['l'] = matrix[i][j-1]['l']
                                if not matrix[i-1][j]['l'] == matrix[i][j-1]['l']:
                                    igual = (matrix[i-1][j]['l'],matrix[i][j-1]['l'])
                                    if not igual in iguais:
                                        iguais.append(igual)
                                #mula a label para uma so
                                # matrix[i-1][j]['l'] = matrix[i][j-1]['l']
                            # somente o de traz
                            elif self.pixel_pertence(i, j-1):
                                    matrix[i][j]['l'] = matrix[i][j-1]['l']
                            # somente o de cima
                            elif self.pixel_pertence(i-1, j):
                                matrix[i][j]['l'] = matrix[i-1][j]['l']
                            # nem o de cima nem o de traz
                            else:
                                matrix[i][j]['l'] = self.label
                                self.incremente_lebal(i,j)

        print('------------------ Matriz Rotulada ---------------------')
        self.print_matrix(matrix)
        print('-------- Matriz Após remover repetidos -----------------')
        self.remove_repetidos(matrix, iguais)


    def remove_repetidos(self, matrix, repetidos):

        for repetido in repetidos:
            for i in range(0, self.size):
                # print(matrix[i][0])
                for j in range(0, self.size):
                    # se a primeira posicao da tupla existe, troca pela segunda posicao 
                    if matrix[i][j]['l'] == repetido[0]:
                        matrix[i][j]['l'] = repetido[1]
        
        self.print_matrix(matrix)
        self.print_new_img(matrix)


    def print_matrix(self, matrix):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if matrix[i][j]['l'] == 0:
                    print('  ', end=' ')
                else:
                    if matrix[i][j]['l'] < 10:
                        print('0{}'.format(matrix[i][j]['l']), end=' ')
                    else:
                        print(matrix[i][j]['l'], end=' ')
                # print(matrix[i][j], end='')
            print('')


    def print_new_img(self, matrix):
        pixel = self.image
        for i in range(0, self.size):
            for j in range(0, self.size):
                if not matrix[i][j]['l'] == 0:
                    if matrix[i][j]['l'] * 4 < 230:
                        pixel.putpixel((j,i),matrix[i][j]['l'] * 4)
                    elif matrix[i][j]['l'] * 3 < 230:
                        pixel.putpixel((j,i),matrix[i][j]['l'] * 3)
                    elif matrix[i][j]['l'] * 2 < 230:
                        pixel.putpixel((j,i),matrix[i][j]['l'] * 2)
                    else:
                        pixel.putpixel((j,i),matrix[i][j]['l'])
           

        pixel.show()




    def print_matrix_teste(self, matrix):
        for i in range(0, self.size):
            # print(matrix[i][0])
            for j in range(0, self.size):
                print(matrix[i][j], end=' ')
                # print(matrix[i][j], end='')
            print('')

    def get_matrix(self):       
        matrix = []
        dic = {}
        for i in range(0, self.image.height):
            line = []
            for j in range(0, self.image.width):
                line.append(dic)
            matrix.append(line)
    
        return matrix

    def get_matrix_rotulos(self):       
        matrix = []
        dic = {}
        for i in range(0, self.size):
            line = []
            for j in range(0, self.size):
                line.append(dic)
            matrix.append(line)
    
        return matrix


                
               
   
 