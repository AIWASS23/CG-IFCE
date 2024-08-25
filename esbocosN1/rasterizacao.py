import math
import matplotlib.pyplot as plt
import numpy as np
import esbocosN1.imagem as imagem


class Resolucao:
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura


largura, altura = 100, 100
resolucao1 = Resolucao(largura, altura)
resolucao2 = Resolucao(largura*3, altura*3)
resolucao3 = Resolucao(largura*6, altura*6)
resolucao4 = Resolucao(largura*8, altura*6)
resolucao5 = Resolucao(int(altura*19.2), int(altura*10.8))


class Ponto:
    def __init__(self, x: float, y: float, resolucao: Resolucao) -> None:
        self.x, self.y = self.scale_point(x, y, resolucao)

    def scale_point(self, x, y, resolucao: Resolucao):
        scaled_x = ((resolucao.largura - 1) * (x + 1)) / 2
        scaled_y = ((resolucao.altura - 1) * (y + 1)) / 2
        return [round(scaled_x), round(scaled_y)]


def calula_delta(ponto_final: int, ponto_inicial: int) -> float:
    return (ponto_final - ponto_inicial)


def produz_fragmento(x: float, y: float) -> list:
    x_medio = (x)
    y_medio = y
    ponto_x_medio = int(x_medio+0.5)
    ponto_y_medio = int(y_medio+0.5)
    return [ponto_x_medio, ponto_y_medio]


def rasterizacao_delta_x_maior_delta_y(ponto1: Ponto, m, b, x2) -> list:
    x1,  y1 = ponto1.x,  ponto1.y
    pontos: list = []
    pontos.append(produz_fragmento(x1, y1))
    if (x1 < x2):
        while (x1 < x2):
            x1 = x1 + 1
            if (m != 0):
                y1 = math.ceil(m*x1 + b)
            pontos.append(produz_fragmento(x1, y1))
    else:
        aux = x1
        while (x2 < aux):
            x2 = x2 + 1
            x1 = x1-1
            if (m != 0):
                y1 = math.ceil(m*x1 + b)
            pontos.append(produz_fragmento(x1, y1))
    return pontos


def rasterizacao_delta_y_maior_delta_x(ponto1: Ponto, m, b, ponto2: Ponto) -> list:
    x1,  y1, y2 = ponto1.x,  ponto1.y, ponto2.y

    pontos: list = []
    if (y1 < y2):
        while (y1 < y2):
            pontos.append(produz_fragmento(x1, y1))
            y1 = y1 + 1
            if (m != 0):
                x1 = ((y1-b)/m)
    else:
        aux = y1
        while y2 < aux:
            pontos.append(produz_fragmento(x1, y1))
            y2 = y2 + 1
            y1 = y1 - 1
            if (m != 0):
                x1 = math.ceil((y1-b) / m)

    return pontos


def rasterizacao_de_retas(ponto1: Ponto, ponto2: Ponto) -> None:
    primeiro_ponto,  = ponto1,
    pontos: list

    delta_x = calula_delta(ponto2.x, ponto1.x)
    delta_y = calula_delta(ponto2.y, ponto1.y)

    x = primeiro_ponto.x
    y = primeiro_ponto.y
    if (delta_x != 0):
        m = delta_y/delta_x
        b = y - m * x
    else:
        m = 0  # como o x não varia , a reta não possui inclinação
        b = 0

    if (abs(delta_x) > abs(delta_y)):
        pontos = rasterizacao_delta_x_maior_delta_y(
            primeiro_ponto, m, b, ponto2.x)
    else:
        pontos = rasterizacao_delta_y_maior_delta_x(
            primeiro_ponto, m, b, ponto2)

    return pontos


def triangulo(tri_ponto1, tri_ponto2, tri_ponto3, resolucao: Resolucao):
    pontos = []
    tri_ponto1 = Ponto(tri_ponto1[0], tri_ponto1[1], resolucao)
    tri_ponto2 = Ponto(tri_ponto2[0], tri_ponto2[1], resolucao)
    tri_ponto3 = Ponto(tri_ponto3[0], tri_ponto3[1], resolucao)
    pontos.append(rasterizacao_de_retas(tri_ponto1, tri_ponto2))
    pontos.append(rasterizacao_de_retas(tri_ponto2, tri_ponto3))
    pontos.append(rasterizacao_de_retas(tri_ponto3, tri_ponto1))
    return pontos


def hexagono(hex1, hex2, hex3, hex4, hex5, hex6, resolucao):
    pontos = []
    hex1 = Ponto(hex1[0], hex1[1], resolucao)
    hex2 = Ponto(hex2[0], hex2[1], resolucao)
    hex3 = Ponto(hex3[0], hex3[1], resolucao)
    hex4 = Ponto(hex4[0], hex4[1], resolucao)
    hex5 = Ponto(hex5[0], hex5[1], resolucao)
    hex6 = Ponto(hex6[0], hex6[1], resolucao)

    pontos.append(rasterizacao_de_retas(hex1, hex2))
    pontos.append(rasterizacao_de_retas(hex2, hex3))
    pontos.append(rasterizacao_de_retas(hex3, hex4))
    pontos.append(rasterizacao_de_retas(hex4, hex5))
    pontos.append(rasterizacao_de_retas(hex5, hex6))
    pontos.append(rasterizacao_de_retas(hex6, hex1))

    return pontos


def quadrado(hex1, hex2, hex3, hex4, resolucao: Resolucao):
    pontos = []
    hex1 = Ponto(hex1[0], hex1[1], resolucao)
    hex2 = Ponto(hex2[0], hex2[1], resolucao)
    hex3 = Ponto(hex3[0], hex3[1], resolucao)
    hex4 = Ponto(hex4[0], hex4[1], resolucao)

    pontos.append(rasterizacao_de_retas(hex1, hex2))
    pontos.append(rasterizacao_de_retas(hex2, hex3))
    pontos.append(rasterizacao_de_retas(hex3, hex4))
    pontos.append(rasterizacao_de_retas(hex4, hex1))

    return pontos


def rasteriza_poligno(arestas, resolucao: Resolucao):
    # Inicializa a imagem como uma matriz de zeros
    imagem = np.zeros((resolucao.altura, resolucao.largura, 3), dtype=np.uint8)
    pontos_internos = []

    x = []
    y = []
    for pontos in arestas:
        for ponto in pontos:
            x.append((ponto[0]))
            y.append((ponto[1]))
        imagem[y, x] = [1, 1, 1]
    # Para cada linha da imagem
    for alt in range(resolucao.altura):
        # Inicializa o número de interseções com zero
        count = 0
        # Para cada aresta do polígono
        ponto_aux = []
        for lar in range(resolucao.largura):
            if (np.array_equal(imagem[alt, lar], [1, 1, 1])):
                if (alt < resolucao.altura and (lar+1) < resolucao.largura and np.array_equal(imagem[alt, lar+1], [1, 1, 1])):
                    # if ():
                    pass
                else:
                    count += 1
            if (count > 0 and count < 2):
                ponto_aux.append([alt, lar])
        if (len(ponto_aux) != 0 and count % 2 == 0):
            pontos_internos.append(ponto_aux)

    return pontos_internos


# TRIANGULO INFERIOR
tri_ponto1 = (-1, -1)
tri_ponto2 = (-0.75, -0.50)
tri_ponto3 = (-0.50, -1)

# triangulo superior
tri2_ponto1 = (-0.25, -0.5)
tri2_ponto2 = (0.25, -0.5)
tri2_ponto3 = (0, 0)
# RETA
ponto1 = (-0.75, -0.25)
ponto2 = (-0.25, 0.25)

# Reta horizontal
ponto_reta2 = (-1, -0.5)
ponto2_reta2 = (-0.5, 0.25)
# Reta vertical
ponto2_reta_v = (-0.30, -1)
ponto2_reta_v = (-0.30, -0.5)


# hexagono superior
hex_ponto1 = (-0.25, 0.5)
hex_ponto2 = (0, 0.25)
hex_ponto3 = (0.25, 0.25)
hex_ponto4 = (0.5, 0.5)
hex_ponto5 = (0.25, 0.75)
hex_ponto6 = (0, 0.75)

# hexagono inferior
hex2_ponto1 = (0.25, 0)
hex2_ponto2 = (0.50, -0.25)
hex2_ponto3 = (0.75, -0.25)
hex2_ponto4 = (1, 0)
hex2_ponto5 = (0.75, 0.25)
hex2_ponto6 = (0.5, 0.25)


quadr_p1 = (-1, 1)
quadr_p2 = (-0.5, 1)
quadr_p3 = (-0.5, 0.5)
quadr_p4 = (-1, 0.5)

# quadrado inferior
quadr2_p1 = (0, -1)
quadr2_p2 = (0.25, -1)
quadr2_p3 = (0.25, -0.75)
quadr2_p4 = (0, -0.75)


# Imagem na resolução 100 x 100
Image1 = np.zeros((resolucao1.altura, resolucao1.largura, 3), dtype=np.uint8)
# triangulo inferior
pontosTriangulo = triangulo(tri_ponto1, tri_ponto2, tri_ponto3, resolucao1)
Image1 = imagem.Imagem.criar_imagem_geometrica(Image1, pontosTriangulo)
pontos_internos = rasteriza_poligno(pontosTriangulo, resolucao1)
for ponto in pontos_internos:
    for p in ponto:
        Image1[p[0], p[1]] = [255, 0, 0]

# RETA
pontos_reta = rasterizacao_de_retas(
    Ponto(-0.75, -0.25, resolucao1), Ponto(-0.25, 0.25, resolucao1))
Image1 = imagem.Imagem.criar_imagem_reta(Image1, pontos_reta)

# RETA HOZONTAL
pontos_reta = rasterizacao_de_retas(
    Ponto(-1, 0.25, resolucao1), Ponto(-0.5, 0.25, resolucao1))
Image1 = imagem.Imagem.criar_imagem_reta(Image1, pontos_reta)

# RETA VERTICAL
pontos_reta = rasterizacao_de_retas(
    Ponto(-0.3, -1, resolucao1), Ponto(-0.3, -0.5, resolucao1))
Image1 = imagem.Imagem.criar_imagem_reta(Image1, pontos_reta)

# hexagono superior
pontoshexagono = hexagono(hex_ponto1, hex_ponto2, hex_ponto3,
                          hex_ponto4, hex_ponto5, hex_ponto6, resolucao1)
Image1 = imagem.Imagem.criar_imagem_geometrica(Image1, pontoshexagono)
pontos_internos = rasteriza_poligno(pontoshexagono, resolucao1)
for ponto in pontos_internos:
    for p in ponto:
        Image1[p[0], p[1]] = [255, 0, 0]

# hexagono inferior
pontos2hexagono = hexagono(hex2_ponto1, hex2_ponto2, hex2_ponto3,
                           hex2_ponto4, hex2_ponto5, hex2_ponto6, resolucao1)
Image1 = imagem.Imagem.criar_imagem_geometrica(Image1, pontos2hexagono)
pontos_internos = rasteriza_poligno(pontos2hexagono, resolucao1)
for ponto in pontos_internos:
    for p in ponto:
        Image1[p[0], p[1]] = [255, 0, 0]

# triangulo
pontosTriangulo2 = triangulo(tri2_ponto1, tri2_ponto2, tri2_ponto3, resolucao1)
Image1 = imagem.Imagem.criar_imagem_geometrica(Image1, pontosTriangulo2)
pontos_internos = rasteriza_poligno(pontosTriangulo2, resolucao1)
for ponto in pontos_internos:
    for p in ponto:
        Image1[p[0], p[1]] = [255, 0, 0]


# quadrado_superior
pontos_quadrado = quadrado(quadr_p1, quadr_p2, quadr_p3, quadr_p4, resolucao1)
Image1 = imagem.Imagem.criar_imagem_geometrica(Image1, pontos_quadrado)
pontos_internos = rasteriza_poligno(pontos_quadrado, resolucao1)
for ponto in pontos_internos:
    for p in ponto:
        Image1[p[0], p[1]] = [255, 0, 0]

# quadrado_inferior
pontos_quadrado = quadrado(
    quadr2_p1, quadr2_p2, quadr2_p3, quadr2_p4, resolucao1)
Image1 = imagem.Imagem.criar_imagem_geometrica(Image1, pontos_quadrado)
pontos_internos = rasteriza_poligno(pontos_quadrado, resolucao1)
for ponto in pontos_internos:
    for p in ponto:
        Image1[p[0], p[1]] = [255, 0, 0]

# FIM DO TRIANGULO


# Imagem na resolução 800 x 600
Image2 = np.zeros((resolucao4.altura, resolucao4.largura, 3), dtype=np.uint8)
# triangulo
pontosTriangulo = triangulo(tri_ponto1, tri_ponto2, tri_ponto3, resolucao4)
Image2 = imagem.Imagem.criar_imagem_geometrica(Image2, pontosTriangulo)
pontos_internos = rasteriza_poligno(pontosTriangulo, resolucao4)
for ponto in pontos_internos:
    for p in ponto:
        Image2[p[0], p[1]] = [255, 0, 0]

# FIM DO TRIANGULO

# RETA
pontos_reta = rasterizacao_de_retas(
    Ponto(-0.75, -0.25, resolucao4), Ponto(-0.25, 0.25, resolucao4))
Image2 = imagem.Imagem.criar_imagem_reta(Image2, pontos_reta)


# RETA HOZONTAL
pontos_reta = rasterizacao_de_retas(
    Ponto(-1, 0.25, resolucao4), Ponto(-0.5, 0.25, resolucao4))
Image2 = imagem.Imagem.criar_imagem_reta(Image2, pontos_reta)

# RETA VERTICAL
pontos_reta = rasterizacao_de_retas(
    Ponto(-0.3, -1, resolucao4), Ponto(-0.3, -0.5, resolucao4))
Image2 = imagem.Imagem.criar_imagem_reta(Image2, pontos_reta)

# hexagono superior
pontoshexagono = hexagono(hex_ponto1, hex_ponto2, hex_ponto3,
                          hex_ponto4, hex_ponto5, hex_ponto6, resolucao4)
Image2 = imagem.Imagem.criar_imagem_geometrica(Image2, pontoshexagono)
pontos_internos = rasteriza_poligno(pontoshexagono, resolucao4)
for ponto in pontos_internos:
    for p in ponto:
        Image2[p[0], p[1]] = [255, 0, 0]

# hexagono inferior
pontoshexa2gono = hexagono(hex2_ponto1, hex2_ponto2, hex2_ponto3,
                           hex2_ponto4, hex2_ponto5, hex2_ponto6, resolucao4)
Image2 = imagem.Imagem.criar_imagem_geometrica(Image2, pontoshexa2gono)
pontos_internos = rasteriza_poligno(pontoshexa2gono, resolucao4)
for ponto in pontos_internos:
    for p in ponto:
        Image2[p[0], p[1]] = [255, 0, 0]

pontosTriangulo2 = triangulo(tri2_ponto1, tri2_ponto2, tri2_ponto3, resolucao4)
Image2 = imagem.Imagem.criar_imagem_geometrica(Image2, pontosTriangulo2)
pontos_internos = rasteriza_poligno(pontosTriangulo2, resolucao4)
for ponto in pontos_internos:
    for p in ponto:
        Image2[p[0], p[1]] = [255, 0, 0]

pontos_quadrado = quadrado(quadr_p1, quadr_p2, quadr_p3, quadr_p4, resolucao4)
Image2 = imagem.Imagem.criar_imagem_geometrica(Image2, pontos_quadrado)
pontos_internos = rasteriza_poligno(pontos_quadrado, resolucao4)
for ponto in pontos_internos:
    for p in ponto:
        Image2[p[0], p[1]] = [255, 0, 0]

# quadrado_inferior
pontos_quadrado = quadrado(
    quadr2_p1, quadr2_p2, quadr2_p3, quadr2_p4, resolucao4)
Image2 = imagem.Imagem.criar_imagem_geometrica(Image2, pontos_quadrado)
pontos_internos = rasteriza_poligno(pontos_quadrado, resolucao4)
for ponto in pontos_internos:
    for p in ponto:
        Image2[p[0], p[1]] = [255, 0, 0]


# RESOLUÇÃO 1920X1080
Image3 = np.zeros((resolucao5.altura, resolucao5.largura, 3), dtype=np.uint8)
# triangulo
pontosTriangulo = triangulo(tri_ponto1, tri_ponto2, tri_ponto3, resolucao5)
Image3 = imagem.Imagem.criar_imagem_geometrica(Image3, pontosTriangulo)
pontos_internos = rasteriza_poligno(pontosTriangulo, resolucao5)
for ponto in pontos_internos:
    for p in ponto:
        Image3[p[0], p[1]] = [255, 0, 0]

# FIM DO TRIANGULO

# RETA
pontos_reta = rasterizacao_de_retas(
    Ponto(-0.75, -0.25, resolucao5), Ponto(-0.25, 0.25, resolucao5))
Image3 = imagem.Imagem.criar_imagem_reta(Image3, pontos_reta)

# RETA HOZONTAL
pontos_reta = rasterizacao_de_retas(
    Ponto(-1, 0.25, resolucao5), Ponto(-0.5, 0.25, resolucao5))
Image3 = imagem.Imagem.criar_imagem_reta(Image3, pontos_reta)

# RETA VERTICAL
pontos_reta = rasterizacao_de_retas(
    Ponto(-0.3, -1, resolucao5), Ponto(-0.3, -0.5, resolucao5))
Image3 = imagem.Imagem.criar_imagem_reta(Image3, pontos_reta)

# hexagono superior
pontoshexagono = hexagono(hex_ponto1, hex_ponto2, hex_ponto3,
                          hex_ponto4, hex_ponto5, hex_ponto6, resolucao5)
Image3 = imagem.Imagem.criar_imagem_geometrica(Image3, pontoshexagono)
pontos_internos = rasteriza_poligno(pontoshexagono, resolucao5)
for ponto in pontos_internos:
    for p in ponto:
        Image3[p[0], p[1]] = [255, 0, 0]

# hexagono inferior
pontoshexagono2 = hexagono(hex2_ponto1, hex2_ponto2, hex2_ponto3,
                           hex2_ponto4, hex2_ponto5, hex2_ponto6, resolucao5)
Image3 = imagem.Imagem.criar_imagem_geometrica(Image3, pontoshexagono2)
pontos_internos = rasteriza_poligno(pontoshexagono2, resolucao5)
for ponto in pontos_internos:
    for p in ponto:
        Image3[p[0], p[1]] = [255, 0, 0]

pontosTriangulo2 = triangulo(tri2_ponto1, tri2_ponto2, tri2_ponto3, resolucao5)
Image3 = imagem.Imagem.criar_imagem_geometrica(Image3, pontosTriangulo2)
pontos_internos = rasteriza_poligno(pontosTriangulo2, resolucao5)
for ponto in pontos_internos:
    for p in ponto:
        Image3[p[0], p[1]] = [255, 0, 0]

pontos_quadrado = quadrado(quadr_p1, quadr_p2, quadr_p3, quadr_p4, resolucao5)
Image3 = imagem.Imagem.criar_imagem_geometrica(Image3, pontos_quadrado)
pontos_internos = rasteriza_poligno(pontos_quadrado, resolucao5)
for ponto in pontos_internos:
    for p in ponto:
        Image3[p[0], p[1]] = [255, 0, 0]

# quadrado_inferior
pontos_quadrado = quadrado(
    quadr2_p1, quadr2_p2, quadr2_p3, quadr2_p4, resolucao5)
Image3 = imagem.Imagem.criar_imagem_geometrica(Image3, pontos_quadrado)
pontos_internos = rasteriza_poligno(pontos_quadrado, resolucao5)
for ponto in pontos_internos:
    for p in ponto:
        Image3[p[0], p[1]] = [255, 0, 0]


fig = plt.figure(figsize=(10, 10))
rows = 1
columns = 4

fig.add_subplot(rows, columns, 1)
# triangulo azul
x = [-1, -0.75, -0.50, -1]
y = [-1, -0.50, -1, -1]
plt.plot(x, y)

# reta inclinada laranja
x1 = [-0.75, -0.25]
y1 = [-0.25, 0.25]
plt.plot(x1, y1)
# reta verde horizontal
x2 = [-1, -0.5]
y2 = [0.25, 0.25]
plt.plot(x2, y2)
# reta vermelha vertical
x3 = [-0.30, -0.30]
y3 = [-1, -0.50]
plt.plot(x3, y3)
# quadrado roxo maior
x5 = [-1, -0.50, -0.50, -1, -1]
y5 = [1, 1, 0.50, 0.50, 1]
plt.plot(x5, y5)
# quadrado castanho menor
x7 = [0, 0.25, 0.25, 0, 0]
y7 = [-1, -1, -0.75, -0.75, -1]
plt.plot(x7, y7)

# hexagono superior
x8 = [-0.25,  0,  0.25, 0.5, 0.25, 0, -0.25]
y8 = [0.5, 0.25, 0.25, 0.5, 0.75, 0.75, 0.5]
plt.plot(x8, y8)
# triangulo cinza
x9 = [-0.25, 0.25, 0, -0.25]
y9 = [-0.5, -0.5, 0, -0.5]
plt.plot(x9, y9)
# hexagono inferior
x10 = [0.25, 0.50, 0.75, 1, 0.75, 0.5, 0.25]
y10 = [0, -0.25, -0.25, 0, 0.25, 0.25, 0]
plt.plot(x10, y10)
plt.title('Figuras entre -1 e 1')

fig.add_subplot(rows, columns, 2)
plt.imshow(Image1)
plt.gca().invert_yaxis()
plt.title("100x100")

fig.add_subplot(rows, columns, 3)
plt.imshow(Image2)
plt.gca().invert_yaxis()
plt.title("800x600")

fig.add_subplot(rows, columns, 4)
plt.imshow(Image3)
plt.gca().invert_yaxis()  # Inverte o eixo y
plt.title("600x600")


plt.show()
