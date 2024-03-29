import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import math

def vector_size(points):
    points = np.array(points)
    distances = np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1))
    total_distance = np.sum(distances)
    n = np.round(len(points)/2)
    total_distance_avg = total_distance / n
    return total_distance_avg

def normalize_coordinates(coordinates):
    coordinates = np.array(coordinates)
    size = vector_size(coordinates)
    normalized_coordinates = coordinates / size
    return normalized_coordinates.tolist()

# def normalize_coordinates(coordinates):
#     max_distance = max(math.dist(coord, (0, 0)) for coord in coordinates)
#     normalized_coordinates = []
#     for coord in coordinates:
#         normalized_x = coord[0] / max_distance
#         normalized_y = coord[1] / max_distance
#         normalized_coordinates.append((normalized_x, normalized_y))
#     return normalized_coordinates

def printRasterArray(text, array, polygon_coords=None):
    plt.imshow(array, cmap='binary', interpolation='None')
    plt.colorbar()
    plt.title(text)
    plt.gca().set_aspect('equal', adjustable = 'box')
    plt.gca().invert_yaxis()

    if polygon_coords:
        polygon = Polygon(polygon_coords, edgecolor = 'red', facecolor = 'none')
        plt.gca().add_patch(polygon)

    plt.show()

def intervalToBinaryMatrix(curve_points, resolution):
    curve_matrix = np.zeros((resolution[1], resolution[0]))
    x_vals, y_vals = curve_points

    x_vals_scaled = ((x_vals - np.min(x_vals)) / (np.max(x_vals) - np.min(x_vals))) * (resolution[0] - 1)

    y_vals_scaled = ((y_vals - np.min(y_vals)) / (np.max(y_vals) - np.min(y_vals))) * (resolution[1] - 1)

    x_vals_scaled = np.round(x_vals_scaled).astype(int)
    y_vals_scaled = np.round(y_vals_scaled).astype(int)

    curve_matrix[y_vals_scaled, x_vals_scaled] = 1

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

def rasterizar_linha(coord):
    x_fragmentos = []
    y_fragmentos = []

    for i in range(len(coord) - 1):
        x1, y1 = coord[i]
        x2, y2 = coord[i + 1]

        x = x1
        y = y1
        deltax = x2 - x1
        deltay = y2 - y1

        if deltax != 0:
            m = deltay / deltax
            while x < x2:
                x = x + 1e-7
                y = m * x + (y1 - m * x1)
                novo_fragmento = produz_fragmento(x, y)
                x_fragmentos.extend(novo_fragmento[0])
                y_fragmentos.extend(novo_fragmento[1])
        else:
            m = deltay / 1e-7  # Usando um valor muito pequeno em vez de 0
            while y < y2:
                y = y + 1e-7
                x = x1
                novo_fragmento = produz_fragmento(x, y)
                x_fragmentos.extend(novo_fragmento[0])
                y_fragmentos.extend(novo_fragmento[1])

    return x_fragmentos, y_fragmentos

def scale_coordinates(polygons, resolution):
    scaled_polygons = []
    for p in polygons:
        scaled_p = (int(p[0] * resolution[0] * 2), int(p[1] * resolution[1] * 2))
        scaled_polygons.append(scaled_p)
    return scaled_polygons

def descale_coordinates(scaled_polygons, resolution):
    polygons = []
    for p in scaled_polygons:
        original_p = (p[0] / (resolution[0] * 2), p[1] / (resolution[1] * 2))
        polygons.append(original_p)
    return polygons

def scanline(polygons, resolution):
    scaled_polygons = scale_coordinates(polygons, resolution)
    min_y, max_y = min(p[1] for p in scaled_polygons), max(p[1] for p in scaled_polygons)
    contour_x, contour_y, fill_x, fill_y = [], [], [], []

    for y in range(min_y, max_y + 1):
        intersections = []
        for i in range(len(scaled_polygons)):
            p1, p2 = scaled_polygons[i], scaled_polygons[(i + 1) % len(scaled_polygons)]
            if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
                if p1[1] != p2[1]:
                    x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                    intersections.append(x)

        intersections.sort()
        for i in range(0, len(intersections), 2):
            fill_x.extend(range(int(intersections[i]), int(intersections[i + 1]) + 1))
            fill_y.extend([y] * (int(intersections[i + 1]) - int(intersections[i]) + 1))

        if intersections:
            contour_x.extend((min(intersections), max(intersections)))
            contour_y.extend([y] * 2)

    contour_points = list(zip(contour_x, contour_y))
    fill_points = list(zip(fill_x, fill_y))
    descaled_contour = descale_coordinates(contour_points, resolution)
    descaled_fill = descale_coordinates(fill_points, resolution)

    return tuple(zip(*descaled_contour)), tuple(zip(*descaled_fill))

# ---------------------------------- Deu Ruim ------------------------------------- #



# ------------------------ Deu bom ------------------------------------- #

# Segmento com m > 0
reta_M_maior_0 = [(1, 1), (5, 8)]
reta_normalizado_M_maior_0 = normalize_coordinates(reta_M_maior_0)
fragmentos_M_maior_0 = rasterizar_linha(reta_normalizado_M_maior_0)
matriz_rasterizada_M_maior_0 = intervalToBinaryMatrix(fragmentos_M_maior_0, (100,100))
printRasterArray(" m > 0", matriz_rasterizada_M_maior_0)

# Segmento com m < 0
reta_M_menor_0 = [(1, 8), (5, 1)]
reta_normalizado_M_menor_0 = normalize_coordinates(reta_M_menor_0)
fragmentos_M_menor_0 = rasterizar_linha(reta_normalizado_M_menor_0)
matriz_rasterizada_M_menor_0 = intervalToBinaryMatrix(fragmentos_M_menor_0, (100,100))
printRasterArray("m < 0", matriz_rasterizada_M_menor_0)

# Segmento com |Δx| > |Δy|
reta_X_maior_Y = [(1, 1), (8, 5)]
reta_normalizado_X_maior_Y = normalize_coordinates(reta_X_maior_Y)
fragmentos_X_maior_Y = rasterizar_linha(reta_normalizado_X_maior_Y)
matriz_rasterizada_X_maior_Y = intervalToBinaryMatrix(fragmentos_X_maior_Y, (100,100))
printRasterArray("|Δx| > |Δy|", matriz_rasterizada_X_maior_Y)

# Segmento com |Δy| > |Δx|
reta_Y_maior_X = [(1, 1), (5, 8)]
reta_normalizado_Y_maior_X = normalize_coordinates(reta_Y_maior_X)
fragmentos_Y_maior_X = rasterizar_linha(reta_normalizado_Y_maior_X)
matriz_rasterizada_Y_maior_X = intervalToBinaryMatrix(fragmentos_Y_maior_X, (100,100))
printRasterArray("|Δy| > |Δx|", matriz_rasterizada_Y_maior_X)

# Segmento vertical
reta_vertical = [(5, 2), (5, 8)]
reta_normalizado_vertical = normalize_coordinates(reta_vertical)
fragmentos_vertical = rasterizar_linha(reta_normalizado_vertical)
matriz_rasterizada_vertical = intervalToBinaryMatrix(fragmentos_vertical, (100,100))
printRasterArray("vertical", matriz_rasterizada_vertical)

# Segmento horizontal
reta_horizontal = [(2, 5), (8, 5)]
reta_normalizado_horizontal = normalize_coordinates(reta_horizontal)
fragmentos_horizontal = rasterizar_linha(reta_normalizado_horizontal)
matriz_rasterizada_horizontal = intervalToBinaryMatrix(fragmentos_horizontal, (100,100))
printRasterArray("horizontal", matriz_rasterizada_horizontal)

# Pontos de controle e tangentes para 5 curvas de Hermite diferentes
points1 = [(1, 1), (3, 5), (7, 2), (9, 6)]
tangents1 = [(2, 4), (4, 1), (8, 5), (10, 3)]

points2 = [(1, 1), (4, 6), (8, 2), (10, 5)]
tangents2 = [(2, 5), (5, 2), (9, 4), (11, 3)]

points3 = [(1, 1), (2, 7), (6, 3), (9, 8)]
tangents3 = [(2, 6), (3, 1), (7, 4), (10, 9)]

points4 = [(1, 1), (3, 4), (6, 6), (10, 1)]
tangents4 = [(2, 3), (4, 5), (7, 1), (11, 2)]

points5 = [(1, 1), (4, 5), (7, 1), (10, 7)]
tangents5 = [(2, 4), (5, 1), (8, 4), (11, 6)]

# Rasterização e plotagem
for i, (points, tangents) in enumerate([(points1, tangents1), (points2, tangents2), (points3, tangents3), (points4, tangents4), (points5, tangents5)], 1):
    curve_points = hermite_blend_curve(points, tangents)
    x_vals, y_vals = normalize_coordinates(curve_points)
    curve_matrix = intervalToBinaryMatrix((x_vals, y_vals), (100, 100))
    printRasterArray(f"Hermite Curve {i}", curve_matrix)
    
# Pontos de controle e tangentes para curva de Hermite com P1 = P2
points_equal = [(1, 1), (1, 2), (7, 2), (9, 6)]
tangents_equal = [(2, 4), (2, 1), (8, 5), (10, 3)]

curve_points_equal = hermite_blend_curve(points_equal, tangents_equal)
x_vals_equal, y_vals_equal = normalize_coordinates(curve_points_equal)
curve_matrix_equal = intervalToBinaryMatrix((x_vals_equal, y_vals_equal), (100, 100))
printRasterArray("Hermite Curve with P1 = P2", curve_matrix_equal)

# Pontos de controle e tangentes para curvas de Hermite com diferentes quantidades de pontos
points_2 = [(1, 1), (9, 6)]
tangents_2 = [(2, 4), (10, 3)]

points_3 = [(1, 1), (5, 5), (10, 1)]
tangents_3 = [(2, 4), (6, 4), (11, 3)]

points_4 = [(1, 1), (4, 4), (7, 6), (10, 1)]
tangents_4 = [(2, 3), (5, 5), (8, 1), (11, 2)]

# Rasterização e plotagem
for i, (points, tangents) in enumerate([(points_2, tangents_2), (points_3, tangents_3), (points_4, tangents_4)], 1):
    curve_points = hermite_blend_curve(points, tangents)
    x_vals, y_vals = normalize_coordinates(curve_points)
    curve_matrix = intervalToBinaryMatrix((x_vals, y_vals), (100, 100))
    printRasterArray(f"Hermite Curve with {len(points)} points", curve_matrix)

# Triângulos equiláteros
triangle1 = [(50, 10), (10, 90), (90, 90)]
triangle2 = [(50, 90), (10, 10), (90, 10)]
normalized_polygonT1 = normalize_coordinates(triangle1)
normalized_polygonT2 = normalize_coordinates(triangle2)
scanT1 = scanline(normalized_polygonT1, (1920,1080))
scanT2 = scanline(normalized_polygonT2, (1920,1080))
matrixT1 = intervalToBinaryMatrix(scanT1, (1920,1080))
matrixT2 = intervalToBinaryMatrix(scanT2, (1920,1080))
printRasterArray("Triangulo Equilatero", matrixT1)
printRasterArray("Triangulo Equilatero", matrixT2)

# Quadrados
square1 = [(20, 20), (80, 20), (80, 80), (20, 80)]
square2 = [(30, 30), (70, 30), (70, 70), (30, 70)]
normalized_polygonQ1 = normalize_coordinates(square1)
normalized_polygonQ2 = normalize_coordinates(square2)
scanQ1 = scanline(normalized_polygonQ1, (1920,1080))
scanQ2 = scanline(normalized_polygonQ2, (1920,1080))
matrixQ1 = intervalToBinaryMatrix(scanQ1, (1920,1080))
matrixQ2 = intervalToBinaryMatrix(scanQ2, (1920,1080))
printRasterArray("Triangulo Equilatero", matrixQ1)
printRasterArray("Triangulo Equilatero", matrixQ2)

# Hexágonos
hexagon1 = [(50, 10), (85, 30), (85, 70), (50, 90), (15, 70), (15, 30)]
hexagon2 = [(50, 30), (75, 45), (75, 75), (50, 90), (25, 75), (25, 45)]
normalized_polygonH1 = normalize_coordinates(hexagon1)
normalized_polygonH2 = normalize_coordinates(hexagon2)
scanH1 = scanline(normalized_polygonH1, (1920,1080))
scanH2 = scanline(normalized_polygonH2, (1920,1080))
matrixH1 = intervalToBinaryMatrix(scanH1, (1920,1080))
matrixH2 = intervalToBinaryMatrix(scanH2, (1920,1080))
printRasterArray("Triangulo Equilatero", matrixH1)
printRasterArray("Triangulo Equilatero", matrixH2)