import numpy as np

from esbocosN1.cgfinal import (
    normalize_coordinates,
    printRasterArray,
    intervalToBinaryMatrix,
    calculate_blend_for_segments,
    rasterizar_linha,
    equilateral_triangle,
    square,
    regular_hexagon,
    maior_valor
)

def scanline(polygon_coords, resolution):
    # Inicializa a matriz binária para armazenar a imagem
    image_matrix = np.zeros((resolution[1], resolution[0]))

    # Encontra as coordenadas máximas e mínimas do polígono
    min_x = int(np.min(polygon_coords[:, 0]))
    max_x = int(np.max(polygon_coords[:, 0]))
    min_y = int(np.min(polygon_coords[:, 1]))
    max_y = int(np.max(polygon_coords[:, 1]))

    # Lista para armazenar as arestas do polígono
    edges = []
    for i in range(len(polygon_coords)):
        start = polygon_coords[i]
        end = polygon_coords[(i + 1) % len(polygon_coords)]
        edges.append((start, end))

    # Para cada linha de varredura (scanline)
    for y in range(min_y, max_y + 1):
        intersections = []

        # Verifica as interseções com cada aresta
        for edge in edges:
            start, end = edge
            # Se a linha de varredura cruza a aresta
            if (start[1] < y and end[1] > y) or (start[1] > y and end[1] < y):
                x = int(start[0] + (y - start[1]) * (end[0] - start[0]) / (end[1] - start[1]))
                intersections.append(x)

        # Ordena as interseções para desenhar as linhas horizontais
        intersections.sort()

        # Preenche os pixels entre as interseções
        for i in range(0, len(intersections), 2):
            for x in range(intersections[i], intersections[i + 1] + 1):
                image_matrix[y, x] = 1

    return image_matrix

# Parâmetros dos polígonos
resolution = (500, 500)
center = [250, 250]
side_length = 100

# Desenha um triângulo equilátero
triangle_coords = equilateral_triangle(center, side_length, 0)
normalized_triangle = normalize_coordinates(triangle_coords)
binary_triangle = intervalToBinaryMatrix(normalized_triangle, resolution)
printRasterArray("Equilateral Triangle", binary_triangle)

# Desenha um quadrado
square_coords = square(center, side_length, 0)
normalized_square = normalize_coordinates(square_coords)
binary_square = intervalToBinaryMatrix(normalized_square, resolution)
printRasterArray("Square", binary_square)

# Desenha um hexágono
hexagon_coords = regular_hexagon(center, side_length, 0)
normalized_hexagon = normalize_coordinates(hexagon_coords)
binary_hexagon = intervalToBinaryMatrix(normalized_hexagon, resolution)
printRasterArray("Hexagon", binary_hexagon)

# Desenha um triângulo equilátero
triangle_image = scanline(normalized_triangle, resolution)
printRasterArray("Equilateral Triangle (Scanline)", triangle_image)

# Desenha um quadrado
square_image = scanline(normalized_square, resolution)
printRasterArray("Square (Scanline)", square_image)

# Desenha um hexágono
hexagon_image = scanline(normalized_hexagon, resolution)
printRasterArray("Hexagon (Scanline)", hexagon_image)

