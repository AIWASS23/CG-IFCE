import numpy as np
from cgfinal import (
    normalize_coordinates,
    printRasterArray,
    intervalToBinaryMatrix,
    calculate_blend_for_segments,
    rasterizar_linha,
    scanline,
    equilateral_triangle,
    square,
    regular_hexagon,
    maior_valor
)

# -------------------- Retas ------------------------------- #

resolutions = [(100,100), (300,300), (800,600), (1920,1080)]

for res in resolutions:

    # Segmento com m > 0
    reta_M_maior_0 = np.matrix([(1, 1), (5, 8)])
    reta_normalizado_M_maior_0 = normalize_coordinates(reta_M_maior_0)
    fragmentos_M_maior_0 = rasterizar_linha(reta_normalizado_M_maior_0,maior_valor(res))
    matriz_rasterizada_M_maior_0 = intervalToBinaryMatrix(fragmentos_M_maior_0, res)
    printRasterArray("Line with m > 0", matriz_rasterizada_M_maior_0)

    # Segmento com m < 0
    reta_M_menor_0 = np.matrix([(1, 8), (5, 1)])
    reta_normalizado_M_menor_0 = normalize_coordinates(reta_M_menor_0)
    fragmentos_M_menor_0 = rasterizar_linha(reta_normalizado_M_menor_0, maior_valor(res))
    matriz_rasterizada_M_menor_0 = intervalToBinaryMatrix(fragmentos_M_menor_0, res)
    printRasterArray("Line with m < 0", matriz_rasterizada_M_menor_0)

    # # Segmento com |Δx| > |Δy|
    reta_X_maior_Y =  np.matrix([(1, 1), (8, 5)])
    reta_normalizado_X_maior_Y = normalize_coordinates(reta_X_maior_Y)
    fragmentos_X_maior_Y = rasterizar_linha(reta_normalizado_X_maior_Y, maior_valor(res))
    matriz_rasterizada_X_maior_Y = intervalToBinaryMatrix(fragmentos_X_maior_Y, res)
    printRasterArray("Line with |Δx| > |Δy|", matriz_rasterizada_X_maior_Y)

    # # Segmento com |Δy| > |Δx|
    reta_Y_maior_X =  np.matrix([(1, 1), (5, 8)])
    reta_normalizado_Y_maior_X = normalize_coordinates(reta_Y_maior_X)
    fragmentos_Y_maior_X = rasterizar_linha(reta_normalizado_Y_maior_X, maior_valor(res))
    matriz_rasterizada_Y_maior_X = intervalToBinaryMatrix(fragmentos_Y_maior_X, res)
    printRasterArray("Line with |Δy| > |Δx|", matriz_rasterizada_Y_maior_X)

    # # Segmento vertical
    reta_vertical =  np.matrix([(5, 2), (5, 8)])
    reta_normalizado_vertical = normalize_coordinates(reta_vertical)
    fragmentos_vertical = rasterizar_linha(reta_normalizado_vertical, maior_valor(res))
    matriz_rasterizada_vertical = intervalToBinaryMatrix(fragmentos_vertical, res)
    printRasterArray("Segmento vertical", matriz_rasterizada_vertical)

    # # Segmento horizontal
    reta_horizontal =  np.matrix([(2, 5), (8, 5)])
    reta_normalizado_horizontal = normalize_coordinates(reta_horizontal)
    fragmentos_horizontal = rasterizar_linha(reta_normalizado_horizontal, maior_valor(res))
    matriz_rasterizada_horizontal = intervalToBinaryMatrix(fragmentos_horizontal, res)
    printRasterArray("Segmento horizontal", matriz_rasterizada_horizontal)

    # ------------------------- Curvas ------------------------------------------- #

    # Pontos de controle e tangentes para 5 curvas de Hermite diferentes

    points1 = np.matrix([(1, 1), (3, 5), (7, 2), (9, 6)])
    tangents1 = np.matrix([(2, 4), (4, 1), (8, 5), (10, 3)])

    points2 = np.matrix([(1, 1), (4, 6), (8, 2), (10, 5)])
    tangents2 = np.matrix([(2, 5), (5, 2), (9, 4), (11, 3)])

    points3 =  np.matrix([(1, 1), (2, 7), (6, 3), (9, 8)])
    tangents3 =  np.matrix([(2, 6), (3, 1), (7, 4), (10, 9)])

    points4 =  np.matrix([(1, 1), (3, 4), (6, 6), (10, 1)])
    tangents4 =  np.matrix([(2, 3), (4, 5), (7, 1), (11, 2)])

    points5 =  np.matrix([(1, 1), (4, 5), (7, 1), (10, 7)])
    tangents5 =  np.matrix([(2, 4), (5, 1), (8, 4), (11, 6)])

    # Rasterização e plotagem
    for i, (points, tangents) in enumerate([(points1, tangents1), (points2, tangents2), (points3, tangents3), (points4, tangents4), (points5, tangents5)], 1):
        points_norm = normalize_coordinates(points)
        tangents_norm = normalize_coordinates(tangents)
        curve_points = calculate_blend_for_segments(points_norm, tangents_norm, maior_valor(res))
        curve_matrix = intervalToBinaryMatrix(curve_points, res)
        printRasterArray(f"Hermite Curve {i}", curve_matrix)

    # Pontos de controle e tangentes para curva de Hermite com P1 = P2
    points_equal = np.matrix([(1, 1), (1, 1), (7, 2), (9, 6)])
    tangents_equal = np.matrix([(2, 4), (2, 4), (8, 5), (10, 3)])

    points_equal_normalize = normalize_coordinates(points_equal)
    tangents_equal_normalize = normalize_coordinates(tangents_equal)

    curve_points_equal = calculate_blend_for_segments(points_equal_normalize, tangents_equal_normalize, maior_valor(res))
    matrix = intervalToBinaryMatrix(curve_points_equal, res)
    printRasterArray("Hermite Curve with P1 = P2", matrix)
    
    # Pontos de controle e tangentes para curvas de Hermite com diferentes quantidades de pontos

    points_2 = [(1, 1), (9, 6)]
    tangents_2 = [(2, 4), (10, 3)]

    points_3 = [(1, 1), (5, 5), (10, 1)]
    tangents_3 = [(2, 4), (6, 4), (11, 3)]

    points_4 = [(1, 1), (4, 4), (7, 6), (10, 1)]
    tangents_4 = [(2, 3), (5, 5), (8, 1), (11, 2)]

    # Rasterização e plotagem
    for i, (points, tangents) in enumerate([(points_2, tangents_2), (points_3, tangents_3), (points_4, tangents_4)], 1):
        curve_points = calculate_blend_for_segments(points, tangents, maior_valor(res))
        curve_matrix = intervalToBinaryMatrix(curve_points, res)
        printRasterArray(f"Hermite Curve with {i + 1} points", curve_matrix)

    # ------------------------------ Polígonos ------------------------------------------- #

    # Coordenadas dos polígonos
    triangle1 = equilateral_triangle((10, 10), 5, 0)
    triangle1_normalized = normalize_coordinates(triangle1)
    
    triangle2 = equilateral_triangle((50, 50), 30, 15)
    triangle2_normalized = normalize_coordinates(triangle2)
    
    square1 = square((10, 10), 5, 0)
    square1_normalized = normalize_coordinates(square1)
    
    square2 = square((50, 50), 30, 15)
    square2_normalized = normalize_coordinates(square2)
    
    hexagon1 = regular_hexagon((10, 10), 5, 0)
    hexagon1_normalized = normalize_coordinates(hexagon1)
    
    hexagon2 = regular_hexagon((50, 50), 30, 15)
    hexagon2_normalized = normalize_coordinates(hexagon2)

    # Gerar contorno e preenchimento para cada polígono
    contour_triangle1, fill_triangle1 = scanline(triangle1_normalized)
    matrizFill_triangle1 = intervalToBinaryMatrix(fill_triangle1, res)
    matrizCountour_triangle1 = intervalToBinaryMatrix(contour_triangle1, res)

    contour_triangle2, fill_triangle2 = scanline(triangle2_normalized)
    matrizFill_triangle2 = intervalToBinaryMatrix(fill_triangle2, res)
    matrizCountour_triangle2 = intervalToBinaryMatrix(contour_triangle2, res)

    contour_square1, fill_square1 = scanline(square1_normalized)
    matrizFill_square1 = intervalToBinaryMatrix(fill_square1, res)
    matrizCountour_square1 = intervalToBinaryMatrix(contour_square1, res)

    contour_square2, fill_square2 = scanline(square2_normalized)
    matrizFill_square2 = intervalToBinaryMatrix(fill_square2, res)
    matrizCountour_square2 = intervalToBinaryMatrix(contour_square2, res)

    contour_hexagon1, fill_hexagon1 = scanline(hexagon1_normalized)
    matrizFill_hexagon1 = intervalToBinaryMatrix(fill_hexagon1, res)
    matrizCountour_hexagon1 = intervalToBinaryMatrix(contour_hexagon1, res)

    contour_hexagon2, fill_hexagon2 = scanline(hexagon2_normalized)
    matrizFill_hexagon2 = intervalToBinaryMatrix(fill_hexagon2, res)
    matrizCountour_hexagon2 = intervalToBinaryMatrix(contour_hexagon2, res)

    # Imprimir os resultados
    printRasterArray("Fill - Triangulo_1", matrizFill_triangle1)
    printRasterArray("Contour - Triangulo_1", matrizCountour_triangle1)

    printRasterArray("Fill - Triangulo_2", matrizFill_triangle2)
    printRasterArray("Contour - Triangulo_2", matrizCountour_triangle2)

    printRasterArray("Fill - Quadrado_1", matrizFill_square1)
    printRasterArray("Contour - Quadrado_1", matrizCountour_square1)

    printRasterArray("Fill - Quadrado_2", matrizFill_square2)
    printRasterArray("Contour - Quadrado_2", matrizCountour_square2)

    printRasterArray("Fill - Hexagono_1", matrizFill_hexagon1)
    printRasterArray("Contour - Hexagono_1", matrizCountour_hexagon1)

    printRasterArray("Fill - Hexagono_2", matrizFill_hexagon2)
    printRasterArray("Contour -  Hexagono_2", matrizCountour_hexagon2)