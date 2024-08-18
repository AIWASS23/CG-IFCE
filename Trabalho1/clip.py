import numpy as np
from hermite import hermite_blend

INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_out_code(x, y, clip_window):
    xmin, ymin, xmax, ymax = clip_window
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland_clip(reta, clip_window):
    x0, y0 = reta[0].A1
    x1, y1 = reta[1].A1
    out_code0 = compute_out_code(x0, y0, clip_window)
    out_code1 = compute_out_code(x1, y1, clip_window)
    accept = False

    while True:
        if not (out_code0 | out_code1):
            accept = True
            break
        elif out_code0 & out_code1:
            break
        else:
            x, y = 0.0, 0.0
            out_code_out = out_code0 if out_code0 else out_code1

            xmin, ymin, xmax, ymax = clip_window
            if out_code_out & TOP:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif out_code_out & BOTTOM:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif out_code_out & RIGHT:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif out_code_out & LEFT:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            if out_code_out == out_code0:
                x0, y0 = x, y
                out_code0 = compute_out_code(x0, y0, clip_window)
            else:
                x1, y1 = x, y
                out_code1 = compute_out_code(x1, y1, clip_window)

    if accept:
        return np.matrix([[x0, y0], [x1, y1]])
    else:
        return []
    
def inside(p, edge, clip_window):

    if edge == 'left':
        return p[0] >= clip_window[0]  # Verifica se x está à direita da borda esquerda
    elif edge == 'right':
        return p[0] <= clip_window[2]  # Verifica se x está à esquerda da borda direita
    elif edge == 'bottom':
        return p[1] >= clip_window[1]  # Verifica se y está acima da borda inferior
    elif edge == 'top':
        return p[1] <= clip_window[3]  # Verifica se y está abaixo da borda superior


def intersection(p1, p2, edge, clip_window):
    if edge == 'left':
        x = clip_window[0]
        y = p1[1] + (p2[1] - p1[1]) * (x - p1[0]) / (p2[0] - p1[0])
    elif edge == 'right':
        x = clip_window[2]
        y = p1[1] + (p2[1] - p1[1]) * (x - p1[0]) / (p2[0] - p1[0])
    elif edge == 'bottom':
        y = clip_window[1]
        x = p1[0] + (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1])
    elif edge == 'top':
        y = clip_window[3]
        x = p1[0] + (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1])
    return (x, y)

def sutherland_hodgman_clip(polygon, clip_window):

    edges = ['left', 'right', 'bottom', 'top']

    for edge in edges:
        new_polygon = []
        for i in range(polygon.shape[0]):
            p1 = polygon[i].A1
            p2 = polygon[(i + 1) % polygon.shape[0]].A1
            if len(p1) == 0 or len(p2) == 0 :
                continue
            if inside(p2, edge, clip_window):
                if not inside(p1, edge, clip_window):
                    new_polygon.append(intersection(p1, p2, edge, clip_window))
                new_polygon.append(p2)
            elif inside(p1, edge, clip_window):
                new_polygon.append(intersection(p1, p2, edge, clip_window))
        polygon = np.matrix(new_polygon)
    return polygon

def hermite_curve_clip(P_points, T_points, clip_window):
    curve_points = hermite_blend(P_points, T_points, num_points=5)
    clipped_curve = []

    for i in range(len(curve_points) - 1):
        reta = np.matrix([curve_points[i].A1, curve_points[i + 1].A1])
        clipped_segment = cohen_sutherland_clip(reta, clip_window)
        if clipped_segment is not None and not (isinstance(clipped_segment, list) and len(clipped_segment) == 0):
            clipped_curve.append(clipped_segment)

    return np.concatenate(clipped_curve, axis=0) if clipped_curve else clipped_curve