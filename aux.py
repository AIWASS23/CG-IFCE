polygon = [(10, 10), (50, 80), (80, 30), (30, 10)]
normalized_polygon = normalize_coordinates(polygon)
contour,fill = scanline(normalized_polygon, (800,600) )

matrizFill = intervalToBinaryMatrix(fill, (800,600))
matrizCountour = intervalToBinaryMatrix(contour, (800,600))

printRasterArray("rasterização de polignos", matrizFill)

points = [(0, 0), (0, 0)]
tangents = [(1, 0), (1, -1)]

curve_points = hermite_blend_curve(points, tangents,  num_points=10000)


curve_matrix = intervalToBinaryMatrix(curve_points, (100,100))
printRasterArray("Curvas de Hermite", curve_matrix)

curve_matrix = intervalToBinaryMatrix(curve_points, (300,300))
printRasterArray("Curvas de Hermite", curve_matrix)

curve_matrix = intervalToBinaryMatrix(curve_points, (800,600))
printRasterArray("Curvas de Hermite", curve_matrix)

curve_matrix = intervalToBinaryMatrix(curve_points, (1920,1080))
printRasterArray("Curvas de Hermite", curve_matrix)

reta = [(10,10), (70,40)]
reta_normalizado = normalize_coordinates(reta)
fragmentos = rasterizar_linha(reta_normalizado)

matriz_rasterizada = intervalToBinaryMatrix(fragmentos, (50,50))
printRasterArray("rasterização de retas", matriz_rasterizada)