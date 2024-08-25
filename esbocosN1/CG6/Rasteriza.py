#Operações com as matrizes
import numpy as np
#Biblioteca para plotar os gráficos
import matplotlib.pyplot as plt
import math

resolutions = [(50, 50), (100, 100), (300, 300), (600, 600), (600, 800), (1080, 1920)]

class Matriz:
    def __init__(self): 
        self.matriz = [np.zeros(res + (3,), dtype=np.uint8) for res in resolutions]

    def zerarMatriz(self):
        self.matriz.clear()
        self.matriz = [np.zeros(res + (3,), dtype=np.uint8) for res in resolutions]

class Reta:
    def __init__(self, pontos, color=(1, 1, 1)):
        self.pontos = pontos
        self.color = color

    # Desenhar Reta
    def draw_Reta(self, matriz):
        for matriz_desenho in matriz:
            for i in range(len(self.pontos) - 1): 
                x1, y1 = ajustar_res(*self.pontos[i], *matriz_desenho.shape[:2])
                x2, y2 = ajustar_res(*self.pontos[i + 1], *matriz_desenho.shape[:2])
                pontos_rasterizados = rasterizar(x1, y1, x2, y2)
                for p in pontos_rasterizados:
                    if 0 <= p[0] < matriz_desenho.shape[0] and 0 <= p[1] < matriz_desenho.shape[1]:
                        matriz_desenho[p[0], p[1]] = self.color

class Poligono:
    def __init__(self, pontos, color=(1, 1, 1)):
        self.pontos = pontos
        self.color = color

    # Desenhar Polígono
    def draw_poligono(self, matriz):
        for matriz_desenho in matriz:
            for i in range(len(self.pontos)):
                x1, y1 = ajustar_res(*self.pontos[i], *matriz_desenho.shape[:2])
                x2, y2 = ajustar_res(*self.pontos[(i + 1) % len(self.pontos)], *matriz_desenho.shape[:2])
                pontos_rasterizados = rasterizar(x1, y1, x2, y2)
                for p in pontos_rasterizados:
                    if 0 <= p[0] < matriz_desenho.shape[0] and 0 <= p[1] < matriz_desenho.shape[1]:
                        matriz_desenho[p[0], p[1]] = self.color
            preenche_poligono(matriz_desenho, self.color)

class Curva:
    def __init__(self, pontos, tangentes,num_seg, color=(1, 1, 1)):
        self.pontos = pontos
        self.color = color
        self.tangentes = tangentes
        self.num_seg = num_seg
        
    def rasteriza_curva_hermite(self, x0, y0, x1, y1, rx0, ry0, rx1, ry1):
        lista = []

        # Número de segmentos de reta para a rasterização
        num_segmentos = self.num_seg

        for i in range(num_segmentos):
            t = i / num_segmentos

            # Fórmula da curva de Hermite
            h1 = 2*t**3 - 3*t**2 + 1
            h2 = -2*t**3 + 3*t**2
            h3 = t**3 - 2*t**2 + t
            h4 = t**3 - t**2

            # Calcula as coordenadas (x, y) da curva de Hermite
            y = h1 * x0 + h2 * x1 + h3 * rx0 + h4 * rx1
            x = h1 * y0 + h2 * y1 + h3 * ry0 + h4 * ry1

            # Arredonda as coordenadas para o ponto mais próximo na grade de pixels
            x_pixel = round(x)
            y_pixel = round(y)

            lista.append((x_pixel, y_pixel))

        return lista
    
    #Desenha Curva
    def draw_Curva(self, matriz):
        for matriz_desenho in matriz:
            for i in range(len(self.pontos) - 1):
                x0, y0 = ajustar_res(*self.pontos[i], *matriz_desenho.shape[:2])
                x1, y1 = ajustar_res(*self.pontos[i + 1], *matriz_desenho.shape[:2])
                rx0, ry0 = ajustar_res(*self.tangentes[i], *matriz_desenho.shape[:2])
                rx1, ry1 = ajustar_res(*self.tangentes[i + 1], *matriz_desenho.shape[:2])

                pontos_curva = self.rasteriza_curva_hermite(x0, y0, x1, y1, rx0, ry0, rx1, ry1)
                pontos_rasterizados = []
                for c in range(len(pontos_curva) - 1):
                    pontos_rasterizados += (rasterizar(pontos_curva[c][0],pontos_curva[c][1],pontos_curva[c + 1][0],pontos_curva[c + 1][1]))   
                for p in pontos_rasterizados:
                    if 0 <= p[0] < matriz_desenho.shape[0] and 0 <= p[1] < matriz_desenho.shape[1]:
                        matriz_desenho[p[0], p[1]] = self.color

class Tela:
    def __init__(self):
        self.lines = []
        self.polygons = []
        self.curvas = []

    # Adicionar Reta
    def add_Reta(self, reta):
        self.lines.append(reta)

    # Adicionar Poligono
    def add_Poligono(self, polygon):
        self.polygons.append(polygon)
        
    # Adicionar Curvas
    def add_Curva(self, curvas):
        self.curvas.append(curvas)
    
    # Remover Poligono
    def remover_Poligono(self):
        self.polygons.pop()
        myMatriz.zerarMatriz()

    # Remover Reta
    def remove_Reta(self):
        if len(self.lines) != 0:
            self.lines.pop()
            myMatriz.zerarMatriz()

    # Desenhar Tela
    def draw_Tela(self, matriz):
        for linha in self.lines:
            linha.draw_Reta(matriz)

        for polygon in self.polygons:
            polygon.draw_poligono(matriz)
            
        for curva in self.curvas:
            curva.draw_Curva(matriz)

myMatriz = Matriz()

#Plota e mostra os gráficos
def mostrar():
    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    axs = axs.ravel()

    for i in range(len(myMatriz.matriz)):
        axs[i].imshow(myMatriz.matriz[i].astype("uint8"))
        axs[i].set_title(f"{resolutions[i][0]}x{resolutions[i][1]}")
        axs[i].invert_yaxis()
    plt.tight_layout()

    plt.show()

# Realiza o calculo para redimencionar a reta em relação a resolução
def ajustar_res(x_antigo, y_antigo, l, a):
    x_novo = int(((l - 1) * (x_antigo+1)) / 2)
    y_novo = int(((a-1)*(y_antigo+1))/2)
    return x_novo, y_novo

# Rasterizar reta
def rasterizar(x1, y1, x2, y2):
    lista = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dy == 0:
        steps = dx or 1
    elif dx >= dy:
        steps = dx
    else:
        steps = dy

    x_inc = (x2 - x1) / steps
    y_inc = (y2 - y1) / steps

    x = x1
    y = y1

    for i in range(steps):
        xm, ym = produz_fragmento(x, y)
        lista.append((xm, ym))
        x += x_inc
        y += y_inc

    xm, ym = produz_fragmento(x2, y2)
    lista.append((xm, ym))

    return lista
# Produzir fragmento
def produz_fragmento(x, y):
    xm = round(x)
    ym = round(y)
    return xm, ym

#Preencher
def preenche_poligono(matriz, cor):
    # lista para guardar as posições horizontais
    horizontal = []
    # ler a matriz horizontalmente e guardar as posições internas
    for i in range(matriz.shape[0]):
        dentro = False
        horizontalLinha = []
        counter = 0
        for j in range(matriz.shape[1]):
            if all(matriz[i][j] == cor):
                if all(matriz[i][min(matriz.shape[1] - 1, j + 1)] == [0, 0, 0]): 
                    counter += 1
                    dentro = not dentro
            elif dentro and (all(matriz[i][j] == cor) or (any(matriz[i][j] != [0, 0, 0]) and all(matriz[i][j] != cor) and all(matriz[i][j] != [255, 255, 255]))):
                # encontrou outra cor, continua procurando até achar a cor original novamente
                while j < matriz.shape[1] and (all(matriz[i][j] != cor) or (any(matriz[i][j] != [0, 0, 0]) and all(matriz[i][j] != cor) and all(matriz[i][j] != [255, 255, 255]))):
                    j += 1
                if j < matriz.shape[1]:
                    dentro = not dentro
            elif dentro:
                horizontalLinha.append((j, i))
        if counter == 1 or counter == 0:
            horizontalLinha.clear()
        else:
            for elemento in horizontalLinha:
                horizontal.append(elemento)

    # pintar os pontos internos na matriz
    for point in horizontal:
        matriz[point[1]][point[0]] = cor


def add_Resolution(resolution):
    resolutions.append(resolution)
    
def remove_Resolution():
    resolutions.pop()
    

