import numpy as np
import matplotlib.pyplot as plt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Aresta:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Face:
    def __init__(self, pontos):
        self.pontos = pontos  # Lista de pontos que formam a face
        self.arestas = []     # Lista de arestas que formam a face

        # Criação de arestas
        for i in range(len(pontos)):
            self.arestas.append(Aresta(
                pontos[i], 
                pontos[(i + 1) % len(pontos)]
            ))

class Mundo2D:
    def __init__(self):
        self.pontos = []  # Lista de pontos
        self.faces = []   # Lista de faces
        self.arestas = [] # Lista de arestas
        self.cor = 255 # Cor padrão (vermelho)

    def adicionarPonto(self, x, y):
        ponto = Ponto(x, y)
        self.pontos.append(ponto)
        return ponto

    def adicionarFace(self, ponto_indices):
        pontos = [self.pontos[i] for i in ponto_indices]
        face = Face(pontos)
        self.faces.append(face)

        # Atualização da lista de arestas
        for aresta in face.arestas:
            if aresta not in self.arestas:
                self.arestas.append(aresta)

    def pegarPonto(self, index):
        return self.pontos[index]

    def pegarAresta(self, index):
        return self.arestas[index]

    def pegarFace(self, index):
        return self.faces[index]

    def desenharReta(self, matriz):
        for matriz_desenho in matriz:
            for i in range(len(self.pontos) - 1):
                xInicial, yInicial = self.ajusteDeResolucao(
                    self.pontos[i].x,
                    self.pontos[i].y,
                    matriz_desenho.shape[0],
                    matriz_desenho.shape[1]
                )
                xFinal, yFinal = self.ajusteDeResolucao(
                    self.pontos[i + 1].x,
                    self.pontos[i + 1].y,
                    matriz_desenho.shape[0],
                    matriz_desenho.shape[1]
                )
                pontosRasterizados = self.rasterizarPontoMedio(
                    xInicial, 
                    yInicial, 
                    xFinal, 
                    yFinal
                )
                for ponto in pontosRasterizados:
                    if 0 <= ponto[0] < matriz_desenho.shape[0] and 0 <= ponto[1] < matriz_desenho.shape[1]:
                        matriz_desenho[ponto[0], ponto[1]] = self.cor

    def ajusteDeResolucao(self, x, y, maxX, maxY):
        xAjustado = int((x + 1) * (maxX - 1) / 2)
        yAjustado = int((1 - (y + 1) / 2) * (maxY - 1))
        return xAjustado, yAjustado

    def rasterizarPontoMedio(self, x1, y1, x2, y2):
        pontos = []

        dx = x2 - x1
        dy = y2 - y1
        x = x1
        y = y1

        if dx >= 0:
            incX = 1
        else:
            incX = -1
            dx = -dx

        if dy >= 0:
            incY = 1
        else:
            incY = -1
            dy = -dy

        if dx >= dy:
            d = 2 * dy - dx
            incE = 2 * dy
            incNE = 2 * (dy - dx)

            while x != x2:
                pontos.append([x, y])
                if d <= 0:
                    d += incE
                    x += incX
                else:
                    d += incNE
                    x += incX
                    y += incY
        else:
            d = 2 * dx - dy
            incE = 2 * dx
            incNE = 2 * (dx - dy)

            while y != y2:
                pontos.append([x, y])
                if d <= 0:
                    d += incE
                    y += incY
                else:
                    d += incNE
                    x += incX
                    y += incY

        pontos.append([x, y])

        return pontos

    def plotar_rasterizacao(self, matriz):
        self.desenharReta(matriz)
        plt.figure(figsize=(8, 8))
        plt.imshow(matriz, cmap='gray')
        plt.axis('off')
        plt.show()

# Exemplo de uso
mundo = Mundo2D()
p1 = mundo.adicionarPonto(-1, -1)
p2 = mundo.adicionarPonto(1, 1)
#mundo.desenharReta([np.zeros((200, 200, 3), dtype=np.uint8)])
mundo.plotar_rasterizacao(np.zeros((200, 200, 3), dtype=np.uint8))
