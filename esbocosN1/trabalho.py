import numpy as np
import matplotlib.pyplot as plt

#-------------------------- Estrutura de Dados --------------------------------------------#

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
        self.cor = [255, 0, 0]

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

def rasterizarLinha(xInicial, yInicial, xFinal, yFinal, numeroDePontos):
    lista = []

    diferencaEntreX = xFinal - xInicial
    diferencaEntreY = yFinal - yInicial

    if abs(diferencaEntreX) >= abs(diferencaEntreY):
        passos = abs(diferencaEntreX)
    else:
        passos = abs(diferencaEntreY)

    pontoMedioX = diferencaEntreX / (numeroDePontos - 1)
    pontoMedioY = diferencaEntreY / (numeroDePontos - 1)

    x = xInicial
    y = yInicial

    for i in range(numeroDePontos):
        xArredondado, yArredondado = (x, y)
        
        if xArredondado >= min(xInicial, xFinal) and xArredondado <= max(xInicial, xFinal) and \
           yArredondado >= min(yInicial, yFinal) and yArredondado <= max(yInicial, yFinal):
            lista.append((xArredondado, yArredondado))

        x += pontoMedioX
        y += pontoMedioY

    return lista

def curvaHermite(P0, T0, P1, T1, numeroDePontos):
    pontos = []

    for t in np.linspace(0, 1, numeroDePontos):
        H1 = 2*t**3 - 3*t**2 + 1 # P0
        H2 = t**3 - 2*t**2 + t # T0
        H3 = -2*t**3 + 3*t**2 # P1
        H4 = t**3 - t**2 # T1

        x = H1 * P0.x + H2 * T0.x + H3 * P1.x + H4 * T1.x
        y = H1 * P0.y + H2 * T0.y + H3 * P1.y + H4 * T1.y

        pontos.append((x, y))

    return pontos

def plotarRasterizacao(aresta, numeroDePontos):
    pontos = rasterizarLinha(aresta.p1.x, aresta.p1.y, aresta.p2.x, aresta.p2.y, numeroDePontos)
    
    # Inicializar o gráfico
    plt.figure(figsize=(8, 8))
    plt.grid()
    plt.axis('equal')
        
    for ponto in pontos[1:-1]:  # Exclui os pontos iniciais e finais
        plt.plot(ponto[0], ponto[1], 'ks', markersize=2)

    # Plotar os pontos finais
    plt.plot([aresta.p1.x, aresta.p2.x], [aresta.p1.y, aresta.p2.y], 'ro')

    # Mostrar o gráfico
    plt.show()
    
def plotarCurva(P0, T0, P1, T1, numeroDePontos):
    pontosHermite = curvaHermite(P0, T0, P1, T1, numeroDePontos)
    
    # Inicializar o gráfico
    plt.figure(figsize=(8, 8))
    plt.grid()
    plt.axis('equal')

    # Plotar os pontos de controle em vermelho
    plt.plot([P0.x, P1.x], [P0.y, P1.y], 'ro')

    # Plotar a curva de Hermite em azul
    for i in range(len(pontosHermite) - 1):
        pontosReta = rasterizarLinha(pontosHermite[i][0], pontosHermite[i][1], pontosHermite[i+1][0], pontosHermite[i+1][1], numeroDePontos)
        for ponto in pontosReta[1:-1]:
            plt.plot(ponto[0], ponto[1], 'ks', markersize=2)
    
    for ponto in pontosHermite:
        plt.plot(ponto[0], ponto[1], 'bo', markersize=2)
        
    plt.title('Curva de Hermite')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


# P0 = Ponto(-2, 0)
# P1 = Ponto(2, 0)
# T0 = Ponto(-20, 10)
# T1 = Ponto(-10, 20)
# plotarCurva(P0, T0, P1, T1, 30)