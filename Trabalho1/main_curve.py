import numpy as np
from hermite import calculate_blend_for_segments
from plotter import Plotter
from raster import Raster

# curvas
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

# Pontos de controle e tangentes para curva de Hermite com P1 = P2
points_equal = np.matrix([(1, 1), (1, 1), (7, 2), (9, 6)])
tangents_equal = np.matrix([(2, 4), (2, 4), (8, 5), (10, 3)])

resolucoes = [
    (100, 100),
    (300, 300),
    (800, 600),
    (1920, 1080)
]


pontosCurvas= [
  [points1, tangents1],
  [points2, tangents2],
  [points3, tangents3],
  [points4, tangents4],
  [points5, tangents5],
  [points_equal, tangents_equal],
]

comandoCurvas = {
  calculate_blend_for_segments: [range(0,6), None]
}

rasterCurvas = Raster(pontosCurvas)
pontoDeControle, curvas = rasterCurvas.rasterize(comandoCurvas)

for resolucao in resolucoes:
    plotter = Plotter(curvas, pontoDeControle)
    plotter.plot_points("Sistema de Coordenada Mundo", resolucao)