import numpy as np
from plotter import Plotter
from raster import Raster
from raster_line import rasterizar_linha

reta_M_maior_0 = np.matrix([(1, 1), (5, 8)])
reta_M_menor_0 = np.matrix([(1, 8), (5, 1)])
reta_X_maior_Y =  np.matrix([(1, 1), (8, 5)])
reta_Y_maior_X =  np.matrix([(1, 1), (5, 8)])
reta_vertical =  np.matrix([(5, 2), (5, 8)])
reta_horizontal =  np.matrix([(2, 5), (8, 5)])

resolucoes = [
    (100, 100),
    (300, 300),
    (800, 600),
    (1920, 1080)
]

pontosRetas = [
    reta_M_maior_0, 
    reta_M_menor_0, 
    reta_X_maior_Y, 
    reta_Y_maior_X, 
    reta_vertical, 
    reta_horizontal
]

comandoReta = {
    rasterizar_linha: [range(0,6), None],
}

rasterRetas = Raster(pontosRetas)
pontoDeControleReta, retas = rasterRetas.rasterize(comandoReta)

for resolucao in resolucoes:
    plotter = Plotter(retas, pontoDeControleReta)
    plotter.plot_points("Sistema de Coordenada Mundo", resolucao)