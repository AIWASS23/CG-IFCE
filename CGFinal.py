import matplotlib.pyplot as plt
import numpy as np
import math

def normalize_coordinates(points):
    
    points_x = points[:, 0]
    points_y = points[:, 1]
    points_x_lenght = math.sqrt((points_x.T * points_x).A1[0])
    points_y_lenght = math.sqrt((points_y.T * points_y).A1[0])

    lenght_matrix = np.matrix([[points_x_lenght,0], [0, points_y_lenght]])
    return points * np.linalg.inv(lenght_matrix)


def printRasterArray(text, array, polygon_coords=None):
    
    plt.imshow(array, cmap='binary', interpolation='None')
    plt.colorbar()  
    plt.title(text)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()  
    plt.show()

def intervalToBinaryMatrix(points, resolution):
    
    points_matrix = np.zeros((resolution[1], resolution[0]))

    x_vals, y_vals = np.array(points)[:, 0], np.array(points)[:, 1]

    if np.max(x_vals) - np.min(x_vals) == 0:
        x_range = np.full_like(x_vals, resolution[0] // 2) 
    else:
        x_range = np.max(x_vals) - np.min(x_vals)

    if np.max(y_vals) - np.min(y_vals) == 0:
        y_range = np.full_like(y_vals, resolution[1] // 2) 
    else:
        y_range = np.max(y_vals) - np.min(y_vals)

    x_vals_scaled = ((x_vals - np.min(x_vals)) / x_range) * (resolution[0] - 1)
    y_vals_scaled = ((y_vals - np.min(y_vals)) / y_range) * (resolution[1] - 1)

    x_vals_scaled = np.round(x_vals_scaled).astype(int)
    y_vals_scaled = np.round(y_vals_scaled).astype(int)

    points_matrix[y_vals_scaled, x_vals_scaled] = 1

    return points_matrix

def hermite_blend(P_points, T_points, num_points):
    t = np.linspace(0, 1, num_points)
    T = np.matrix([t**3, t**2, t, np.ones(t.shape[0])])
    G = np.vstack((P_points, T_points))
    H = np.matrix([[2,-2,1,1], [-3,3,-2,-1], [0,0,1,0], [1,0,0,0]])
    P = T.T * H * G
    return P

def calculate_blend_for_segments(points, tangents, num_points):
    segments = []
    for i in range(len(points) - 1):
        start_index = i
        end_index = i + 2
        blended_segment = hermite_blend(points[start_index:end_index], tangents[start_index:end_index], num_points)
        segments.append(blended_segment)
    return np.concatenate(segments, axis=0)

def produz_fragmento(coord):
    xm = coord[:, 0]
    ym = coord[:, 1]
    xp = coord[:, 0] + 0.5
    yp = coord[:, 1] + 0.5
    return np.column_stack((xm, ym, xp, yp))

def rasterizar_linha(coord, num_fragments):
    
    coord_matrix = np.matrix(coord)
    deltas = np.diff(coord_matrix, axis=0)
    increments = deltas / num_fragments
    fragmentos = np.empty((0, 2))
    
    for j in range(num_fragments):
        coordenadas = coord_matrix[:-1] + j * increments
        novo_fragmento = produz_fragmento(coordenadas)
        fragmentos = np.vstack((fragmentos, novo_fragmento[:, :2]))

    return fragmentos

def scanline(polygons, step = 1e-3):
    min_y = np.min(polygons[:, 1])
    max_y = np.max(polygons[:, 1])

    contour_points = np.matrix([])
    fill_points = np.matrix([])

    for y in np.arange(min_y, max_y + 1, step):
        intersections = []

        for i in range(len(polygons)):
            p1 = polygons[i].A1.tolist()
            p2 = polygons[(i + 1) % len(polygons)].A1.tolist()

            if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
                if p1[1] != p2[1]:
                    x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                    intersections.append(x)

        intersections.sort()

        for i in range(0, len(intersections), 2):
            interval = np.arange(intersections[i], intersections[i + 1], step)
            fill_row = np.column_stack((interval, np.full_like(interval, y)))
            if fill_points.size == 0:
                fill_points = fill_row
            else:
                fill_points = np.vstack((fill_points, fill_row))

        if intersections:
            contour_row = np.array([[min(intersections), y], [max(intersections), y]])
            if contour_points.size == 0:
                contour_points = contour_row
            else:
                contour_points = np.vstack((contour_points, contour_row))

    return contour_points, fill_points

def equilateral_triangle(center, side_length, angle):
    
    vertices = []
    for i in range(3):
        x = center[0] + side_length * math.cos(math.radians(angle + i * 120))
        y = center[1] + side_length * math.sin(math.radians(angle + i * 120))
        vertices.append([x, y])
    return np.matrix(vertices)

def square(center, side_length, angle):
    
    vertices = []
    for i in range(4):
        x = center[0] + side_length * math.cos(math.radians(angle + i * 90))
        y = center[1] + side_length * math.sin(math.radians(angle + i * 90))
        vertices.append([x, y])
    return np.matrix(vertices)

def regular_hexagon(center, side_length, angle):
    
    vertices = []
    for i in range(6):
        x = center[0] + side_length * math.cos(math.radians(angle + i * 60))
        y = center[1] + side_length * math.sin(math.radians(angle + i * 60))
        vertices.append([x, y])
    return np.matrix(vertices)

def maior_valor(tupla: tuple) -> int :
    max_valor = max(tupla)
    inteiro = int(max_valor)
    return inteiro
