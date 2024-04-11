# resolucoes = [(100, 100), (300, 300), (800, 600), (1920, 1080)]
# matriz = [np.zeros(resolucao + (3,), dtype = np.uint8) for resolucao in resolucoes]

def bresenham_line(x0, y0, x1, y1):
    points = []
    
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    while True:
        points.append((x0, y0))

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points


def scanline_fill(vertices):
    # Ordenar os vértices verticalmente
    vertices.sort(key=lambda vertex: vertex.y)

    ymin = int(min(vertex.y for vertex in vertices))
    ymax = int(max(vertex.y for vertex in vertices))

    # Inicializar lista de ativas
    active_edges = []

    # Inicializar lista de preenchimento
    scanline = [None] * (ymax - ymin + 1)

    for y in range(ymin, ymax + 1):
        # Remover arestas da lista ativa
        active_edges = [edge for edge in active_edges if edge['ymax'] != y]

        # Adicionar novas arestas à lista ativa
        for edge in vertices:
            if edge.ymin == y:
                active_edges.append({'ymin': edge.ymin, 'ymax': edge.ymax, 'x': edge.x, 'dx': edge.dx, 'dy': edge.dy})

        # Ordenar lista ativa pela coordenada x
        active_edges.sort(key=lambda edge: edge['x'])

        # Preencher a scanline
        for i in range(0, len(active_edges), 2):
            x1 = int(active_edges[i]['x'])
            x2 = int(active_edges[i + 1]['x'])

            for x in range(x1, x2 + 1):
                scanline[y - ymin][x] = (x, y)

        # Atualizar as coordenadas x das arestas na lista ativa
        for edge in active_edges:
            edge['x'] += edge['dx'] / edge['dy']

    return scanline


def normalize_coordinates(x, y, width, height):
    x_normalized = (x + 1) * (width - 1) / 2
    y_normalized = (1 - y) * (height - 1) / 2
    return x_normalized, y_normalized

def cohen_sutherland_clipping(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    def compute_outcode(x, y):
        code = 0
        if x < xmin:
            code |= 1
        elif x > xmax:
            code |= 2
        if y < ymin:
            code |= 4
        elif y > ymax:
            code |= 8
        return code

    outcode0 = compute_outcode(x0, y0)
    outcode1 = compute_outcode(x1, y1)

    accept = False

    while True:
        if not (outcode0 | outcode1):
            accept = True
            break
        elif outcode0 & outcode1:
            break
        else:
            x, y = 0, 0
            outcode_out = outcode0 if outcode0 else outcode1

            if outcode_out & 1:
                x = xmin
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
            elif outcode_out & 2:
                x = xmax
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
            elif outcode_out & 4:
                y = ymin
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
            elif outcode_out & 8:
                y = ymax
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)

            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)

    if accept:
        return int(x0), int(y0), int(x1), int(y1)
    else:
        return None

def ajusteDeResolucao(x_antigo, y_antigo, l, a):
    x_novo = int(((l - 1) * (x_antigo + 1)) / 2)
    y_novo = int(((a - 1) * (y_antigo + 1)) / 2)
    return x_novo, y_novo

def arredondarCoordenadas(x, y):
    xm = round(x)
    ym = round(y)
    return xm, ym

def criarPoligono(tamanhoLado, centro, numLados):
    angulo = 360 / numLados
    pontos = []
    
    for i in range(numLados):
        x = centro.x + tamanhoLado * np.cos(np.radians(angulo * i))
        y = centro.y + tamanhoLado * np.sin(np.radians(angulo * i))
        pontos.append(Ponto(x, y))
    
    return pontos