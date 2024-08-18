from plotter import Plotter
from polygon import equilateral_triangle, regular_hexagon, square
from raster import Raster
from scanline import scanline

# poligono
triangle1 = equilateral_triangle((50, 50), 40, 0)
triangle2 = equilateral_triangle((50, 50), 60, 45)
square1 = square((5, 5), 10, 0)
square2 = square((50, 50), 40, 12)
hexagon1 = regular_hexagon((50, 50), 40, 60)
hexagon2 = regular_hexagon((50, 50), 60, 0)

pontosPoligonos = [
    triangle1,
    triangle2,
    square1,
    square2,
    hexagon1,
    hexagon2
]

resolucoes = [
    (100, 100),
    (300, 300),
    (800, 600),
    (1920, 1080)
]

styles = [1, 0]

for style in styles:

    comandoPoligonos = {
        scanline: [range(0,6), style]
    }

    rasterPoligonos = Raster(pontosPoligonos)
    pontoDeControlePoligonos, poligono = rasterPoligonos.rasterize(comandoPoligonos)

    for resolucao in resolucoes:
        plotter = Plotter(poligono, pontoDeControlePoligonos)
        plotter.plot_points("Sistema de Coordenada Mundo", resolucao)