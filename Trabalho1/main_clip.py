import numpy as np
from clip import cohen_sutherland_clip
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

pontosRetasClip = [
    reta_M_maior_0, 
    reta_M_menor_0, 
    reta_X_maior_Y, 
    reta_Y_maior_X, 
    reta_vertical, 
    reta_horizontal
]

clip_commands = {
    cohen_sutherland_clip: range(0, 6)
}

commands_after_clip = {
    rasterizar_linha: [range(0, 6), None]
}

raster = Raster(pontosRetasClip)

aspect_ratio = 1/2 # dimensoes de tela larg = aspc_ratio * altura
clip_window = [-1 * aspect_ratio, -1, 1 * aspect_ratio, 1] # x e y min max 

clip_points, clipped_figure = raster.rasterize_clip(
    clip_window, 
    clip_commands,
    commands_after_clip
)

for resolucao in resolucoes:
    plotter = Plotter(clipped_figure, [])
    plotter.plot_points("Sistema de Coordenada Mundo", resolucao)