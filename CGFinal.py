import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def printRasterArray(text, array, polygon_coords = None):
    # Plot the array
    plt.imshow(array, cmap='binary', interpolation='None')
    plt.colorbar()  # Add a color bar to show mapping of values
    plt.title(text)

    # Set aspect ratio to be equal
    plt.gca().set_aspect('equal', adjustable='box')

    # Draw polygon if coordinates are provided
    if polygon_coords:
        polygon = Polygon(polygon_coords, edgecolor='red', facecolor='none')
        plt.gca().add_patch(polygon)

    plt.show()
    
def intervalToBinaryMatrix(curve_points, resolution):
    # Inicializa uma matriz de zeros com altura e largura especificadas pela resolução
    # A resolução é uma tupla (altura, largura), mas é revertida aqui para largura e altura
    curve_matrix = np.zeros((resolution[1], resolution[0]))

    # Separa os pontos da curva em coordenadas x e y
    x_vals, y_vals = curve_points

    # Escala os valores x para caber na largura da matriz
    x_vals_scaled = ((x_vals - np.min(x_vals)) / (np.max(x_vals) - np.min(x_vals))) * (resolution[0] - 1)

    # Escala os valores y para caber na altura da matriz
    y_vals_scaled = ((y_vals - np.min(y_vals)) / (np.max(y_vals) - np.min(y_vals))) * (resolution[1] - 1)

    # Arredonda os valores escalados para os índices inteiros da matriz
    x_vals_scaled = np.round(x_vals_scaled).astype(int)
    y_vals_scaled = np.round(y_vals_scaled).astype(int)

    # Define os valores correspondentes a 1 na matriz para os pontos da curva
    curve_matrix[y_vals_scaled, x_vals_scaled] = 1

    # Retorna a matriz binária resultante
    return curve_matrix

def hermite_blend(P0, P1, T0, T1, num_points=100):

    t = np.linspace(0, 1, num_points)
    H0 = 2*t**3 - 3*t**2 + 1
    H1 = -2*t**3 + 3*t**2
    H2 = t**3 - 2*t**2 + t
    H3 = t**3 - t**2
    x = P0[0]*H0 + P1[0]*H1 + T0[0]*H2 + T1[0]*H3
    y = P0[1]*H0 + P1[1]*H1 + T0[1]*H2 + T1[1]*H3
    return np.array([x, y])

def hermite_blend_curve(points, tangents, num_points=100):

    curve_points = []
    for i in range(len(points) - 1):
        P0, P1 = points[i], points[i+1]
        T0, T1 = tangents[i], tangents[i+1]
        curve_segment = hermite_blend(P0, P1, T0, T1, num_points=num_points)
        curve_points.append(curve_segment)
    return np.concatenate(curve_points, axis=1)

def produz_fragmento(x, y):
    xm = [x]
    ym = [y]
    xp = [x + 0.5]
    yp = [y + 0.5]
    return xm, ym, xp, yp

def rasterizar_linha(x1, y1, x2, y2, num_pontos):
    xm, ym, xp, yp = produz_fragmento(x1, y1)
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx

    x_fragmentos = xm
    y_fragmentos = ym

    x = x1
    y = y1

    if num_pontos > 0:
        incremento_x = dx / num_pontos
        for _ in range(num_pontos):
            x += incremento_x
            y = m * x + (y1 - m * x1)  # calculando y com base na equação da reta
            novo_fragmento = produz_fragmento(x, y)
            x_fragmentos.extend(novo_fragmento[0])
            y_fragmentos.extend(novo_fragmento[1])

    return x_fragmentos, y_fragmentos

def scanline(polygons):
    # Encontrar o valor mínimo e máximo de y
    min_y = min(p[1] for p in polygons)
    max_y = max(p[1] for p in polygons)

    # Inicializar os arrays x e y
    array_x = []
    array_y = []

    # Para cada linha de varredura
    for y in range(min_y, max_y + 1):
        # Inicializar a lista de interseções
        intersections = []

        # Para cada aresta do polígono
        for i in range(len(polygons)):
            p1 = polygons[i]
            p2 = polygons[(i + 1) % len(polygons)]

            # Verificar se a linha de varredura intercepta a aresta
            if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
                if p1[1] != p2[1]:
                    x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                    intersections.append(x)

        # Ordenar as interseções
        intersections.sort()

        # Adicionar interseções aos arrays x e y
        for i in range(0, len(intersections), 2):
            array_x.extend(list(range(int(intersections[i]), int(intersections[i + 1]) + 1)))
            array_y.extend([y] * (int(intersections[i + 1]) - int(intersections[i]) + 1))

    return array_x, array_y

# Define control points and tangents
# curva
points = [(0, 0), (0, 0)]
tangents = [(1, 0), (1, -1)]

curve_points = hermite_blend_curve(points, tangents,  num_points=10000)
curve_matrix = intervalToBinaryMatrix(curve_points, (100,100))
printRasterArray("Curvas de Hermite", curve_matrix)

curve_matrix = intervalToBinaryMatrix(curve_points, (300,300))
printRasterArray("Curvas de Hermite", curve_matrix)

curve_matrix = intervalToBinaryMatrix(curve_points, (1920,1080))
printRasterArray("Curvas de Hermite", curve_matrix)

#retas

x1 = 10
y1 = 10
x2 = 70
y2 = 40
fragmentos = rasterizar_linha(x1, y1, x2, y2, int(1e5))

matriz_rasterizada = intervalToBinaryMatrix(fragmentos, (1920,1080))
printRasterArray("rasterização de retas", matriz_rasterizada)

#poligonos

polygon = [(10, 10), (50, 80), (80, 30), (30, 10)]
polygon_rasterizado = scanline(polygon)

matriz_rasterizada = intervalToBinaryMatrix(polygon_rasterizado, (300,300))
printRasterArray("rasterização de polignos", matriz_rasterizada)