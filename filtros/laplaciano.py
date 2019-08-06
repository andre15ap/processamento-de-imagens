from PIL import Image


class Filtros:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def criar_imagem(self, img):
        return Image.new('L', (int(img.width), int(img.height)))

    def mascara1(self, i, j):
        pixels = self.imagem.load()
        valor = int((pixels[i-1, j-1]*(0) + pixels[i-1, j]*(1) + pixels[i-1, j+1]*(0) +
                    pixels[i, j-1]*(1)    + pixels[i, j]*(-4)  + pixels[i, j+1]*(1) +
                    pixels[i+1, j-1]*(0)  + pixels[i+1, j]*(1) + pixels[i+1, j+1]*(0)) / 9)
        return valor

    def mascara2(self, i, j):
        pixels = self.imagem.load()
        valor = int((pixels[i-1, j-1]*(1)  + pixels[i-1, j]*(1)   + pixels[i-1, j+1]*(1) +
                    pixels[i, j-1]*(1)     + pixels[i, j]*(-8)    + pixels[i, j+1]*(1) +
                    pixels[i+1, j-1]*(1)   + pixels[i+1, j]*(1)   + pixels[i+1, j+1]*(1)) / 9)
        return valor

    def mascara3(self, i, j):
        pixels = self.imagem.load()
        valor = int((pixels[i-1, j-1]*(0)  + pixels[i-1, j]*(-1)   + pixels[i-1, j+1]*(0) +
                    pixels[i, j-1]*(-1)    + pixels[i, j]*(4)      + pixels[i, j+1]*(-1) +
                    pixels[i+1, j-1]*(0)   + pixels[i+1, j]*(-1)   + pixels[i+1, j+1]*(0)) / 9)
        return valor

    def mascara4(self, i, j):
        pixels = self.imagem.load()
        valor = int((pixels[i-1, j-1]*(-1)  + pixels[i-1, j]*(-1)   + pixels[i-1, j+1]*(-1) +
                    pixels[i, j-1]*(-1)     + pixels[i, j]*(8)      + pixels[i, j+1]*(-1) +
                    pixels[i+1, j-1]*(-1)   + pixels[i+1, j]*(-1)   + pixels[i+1, j+1]*(-1)) / 9)
        return valor

    def laplaciano(self):
        self.imagem.show()

        
        nova_img = self.criar_imagem(self.imagem)
        img_resultado = nova_img.load()

        nova_img_negativa = self.criar_imagem(self.imagem)
        img_resultado_negativa = nova_img_negativa.load()

        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                valor = self.mascara2(i,j)

                if valor < 0:
                    img_resultado[i, j] = 0
                    img_resultado_negativa[i, j] = 0
                else:
                    img_resultado[i, j] =  valor
                    img_resultado_negativa[i, j] =  255 - valor

        nova_img.save('img/laplaciano.png')
        nova_img_negativa.save('img/laplaciano_neg.png')
        nova_img.show()
        nova_img_negativa.show()

    
    def sobel1(self, i, j):
        pixels = self.imagem.load()
        valor = int((pixels[i-1, j-1]*(-1)  + pixels[i-1, j]*(-2)   + pixels[i-1, j+1]*(-1) +
                    pixels[i, j-1]*(0)     + pixels[i, j]*(0)      + pixels[i, j+1]*(0) +
                    pixels[i+1, j-1]*(1)   + pixels[i+1, j]*(2)   + pixels[i+1, j+1]*(1)))
        return valor

    def sobel2(self, i, j):
        pixels = self.imagem.load()
        valor = int((pixels[i-1, j-1]*(-1)  + pixels[i-1, j]*(0)   + pixels[i-1, j+1]*(1) +
                    pixels[i, j-1]*(-2)     + pixels[i, j]*(0)      + pixels[i, j+1]*(2) +
                    pixels[i+1, j-1]*(-1)   + pixels[i+1, j]*(0)   + pixels[i+1, j+1]*(1)))
        return valor
    
    def gradiente(self):
        self.imagem.show()
    
        nova_img = self.criar_imagem(self.imagem)
        img_resultado = nova_img.load()

        nova_img_negativa = self.criar_imagem(self.imagem)
        img_resultado_negativa = nova_img_negativa.load()

        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                
                valor = self.sobel2(i,j)

                if valor < 0:
                    img_resultado[i, j] = 0
                    img_resultado_negativa[i, j] = 0
                else:
                    img_resultado[i, j] =  valor
                    img_resultado_negativa[i, j] =  255 - valor

        nova_img.save('img/laplaciano2.png')
        nova_img_negativa.save('img/laplaciano_neg2.png')
        nova_img.show()
        nova_img_negativa.show()
        self.soma()



    def soma(self):
        img1 = self.obterImagem('img/laplaciano1.png')
        img2 = self.obterImagem('img/laplaciano2.png')
        nova_img_soma = self.criar_imagem(self.imagem)
        img_resultado_soma = nova_img_soma.load()

        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                # valor = img1[i,j] + img2[i,j]
                
                img_resultado_soma[i, j] = img1.getpixel((i,j)) + img2.getpixel((i,j))
                
        nova_img_soma.save('img/soma_gradiente.png')
        
        nova_img_soma.show()
    