import numpy
import matplotlib.pyplot

def arredondarCoordenadas(x, y):
    xm = round(x)
    ym = round(y)
    return xm, ym

def mostrarEspaco(img):
    matplotlib.pyplot.imshow(img)
    matplotlib.pyplot.gca().invert_yaxis()
    matplotlib.pyplot.grid(False)
    matplotlib.pyplot.show()

resolucoes = [(100, 100), (300, 300), (800, 600), (1920, 1080)]
matriz = [numpy.zeros(resolucao + (3,), dtype = numpy.uint8) for resolucao in resolucoes]

# Realiza o calculo para redimencionar a reta em relação a resolução
def ajusteDeResolucao(x_antigo, y_antigo, l, a):
    x_novo = int(((l - 1) * (x_antigo + 1)) / 2)
    y_novo = int(((a - 1) * (y_antigo + 1)) / 2)
    return x_novo, y_novo

def rasterizarPontoMedio(xInicial, yInicial, xFinal, yFinal):
    lista = []

    diferencaEntreX = xFinal - xInicial
    diferencaEntreY = yFinal - yInicial

    if abs(diferencaEntreX) >= abs(diferencaEntreY):
        passos = abs(diferencaEntreX)
    else:
        passos = abs(diferencaEntreY)

    pontoMedioX = diferencaEntreX / passos
    pontoMedioY = diferencaEntreY / passos

    x = xInicial
    y = yInicial

    for i in range(passos):
        xArredondado, yArredondado = arredondarCoordenadas(x, y)
        lista.append((xArredondado, yArredondado))
        x += pontoMedioX
        y += pontoMedioY

    xm, ym = arredondarCoordenadas(xFinal, yFinal)
    lista.append((xm, ym))

    return lista

#Reta
class Reta:

    def __init__(self, pontos, cor = (1, 1, 1)):
        self.pontos = pontos
        self.cor = cor

    def desenharReta(self, matriz):
        for matriz_desenho in matriz:
            for i in range(len(self.pontos)-1):
                xInicial, yInicial = ajusteDeResolucao(
                    self.pontos[i][0],
                    self.pontos[i][1],
                    matriz_desenho.shape[0],
                    matriz_desenho.shape[1]
                )
                xFinal, yFinal = ajusteDeResolucao(
                    self.pontos[i + 1][0],
                    self.pontos[i + 1][1],
                    matriz_desenho.shape[0],
                    matriz_desenho.shape[1]
                )
                pontosRasterizados = rasterizarPontoMedio(
                    xInicial, 
                    yInicial, 
                    xFinal, 
                    yFinal
                )
                for ponto in pontosRasterizados:
                    if 0 <= ponto[0] < matriz_desenho.shape[0] and 0 <= ponto[1] < matriz_desenho.shape[1]:
                        matriz_desenho[ponto[0], ponto[1]] = self.cor
                

class Tela:
    def __init__(self):
        self.linhas = []

    def adicionarReta(self, reta):
        self.linhas.append(reta)

    def desenharTela(self, matriz):
        for linha in self.linhas:
            linha.desenharReta(matriz)

grade = Tela()
grade.adicionarReta(Reta([[-1, -1], [1, 1]], cor=(255, 0, 0)))
grade.adicionarReta(Reta([[-1, 0], [1, 0]], cor=(0, 255, 0)))
grade.adicionarReta(Reta([[0, -1], [0, 1]], cor=(0, 0, 255)))
grade.adicionarReta(Reta([[-1, 1], [1, -1]], cor=(255, 255, 255)))
# maximaDimensao = max(max(matriz_desenho.shape) for matriz_desenho in matriz)
# matplotlib.pyplot.xlim(-maximaDimensao // 2, maximaDimensao // 2)  
# matplotlib.pyplot.ylim(-maximaDimensao // 2, maximaDimensao // 2)

grade.desenharTela(matriz)
for matriz_desenho in matriz:
    mostrarEspaco(matriz_desenho)
