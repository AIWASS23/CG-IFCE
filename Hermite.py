import numpy
import matplotlib.pyplot

def hermiteMatrix(a, b, c, d):
    matrizDeHermite = numpy.array([
        [a, -a, b, c],
        [-b, a, -2*b, -c],
        [0, 0, d, 0],
        [0, 0, -d, 0]
    ])
    return matrizDeHermite

def curvaDeHermite(P1, P2, T1, T2, numeroDePontos, H):
    t = numpy.linspace(0, 1, numeroDePontos)
    
    pontos = []
    for i in range(numeroDePontos):
        T = numpy.array([t[i]**3, t[i]**2, t[i], 1])
        ponto = numpy.dot(
            T, 
            numpy.dot(H, numpy.array([P1, P2, T1, T2]))
        )
        pontos.append(ponto)
    
    return numpy.array(pontos)

# def rasterize_curve(curve_points):
#     for i in range(len(curve_points) - 1):
#         matplotlib.pyplot.plot([curve_points[i][0], curve_points[i+1][0]], [curve_points[i][1], curve_points[i+1][1]], color='b')

def rasterize_curve(curve_points, color):
    for i in range(len(curve_points) - 1):
        matplotlib.pyplot.plot([curve_points[i][0], curve_points[i+1][0]], [curve_points[i][1], curve_points[i+1][1]], color=color)


custom_H = hermiteMatrix(2, -2, 1, 1)

# Exemplo de uso
P1 = numpy.array([0, 1])
P2 = numpy.array([1, 1])
T1 = numpy.array([1, 0])
T2 = numpy.array([0, 1])

max_abs_coord = max(max(abs(P1).max(), abs(P2).max()), abs(T1).max(), abs(T2).max())
# P1_normalized = P1 / max_abs_coord
# P2_normalized = P2 / max_abs_coord
# T1_normalized = T1 / max_abs_coord
# T2_normalized = T2 / max_abs_coord

num_points = 10

curve_points = curvaDeHermite(P1, P2, T1, T2, num_points, custom_H)
#curve_points = curvaDeHermite(P1_normalized, P2_normalized, T1_normalized, T2_normalized, num_points, custom_H)

resolutions = [(100, 100), (300, 300), (800, 600), (1920, 1080)]

for resolution in resolutions:
    max_resolution = max(resolution)
    curve_points_scaled = curve_points * max_resolution / max_abs_coord
    
    matplotlib.pyplot.figure(figsize=(resolution[0]/100, resolution[1]/100))  # Ajuste de escala para exibição
    rasterize_curve(curve_points_scaled, "red")
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.show()

# for resolution in resolutions:
#     matplotlib.pyplot.figure(figsize = (resolution[0]/100, resolution[1]/100))  # Ajuste de escala para exibição
#     rasterize_curve(curve_points, "red")
#     matplotlib.pyplot.axis('equal')
#     matplotlib.pyplot.show()