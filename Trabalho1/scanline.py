import numpy as np
from raster_line import rasterizar_linha

def find_intersections(x_or_y, vertices, axis):
    intersections = []
    num_vertices = len(vertices)
    for i in range(num_vertices):
        p1 = vertices[i].A1.tolist()
        p2 = vertices[(i + 1) % num_vertices].A1.tolist()
        if (p1[axis] <= x_or_y < p2[axis]) or (p2[axis] <= x_or_y < p1[axis]):
            if p1[axis] != p2[axis]:
                other_axis = 1 - axis  # 0 if axis == 1, and 1 if axis == 0
                val = p1[other_axis] + (x_or_y - p1[axis]) * (p2[other_axis] - p1[other_axis]) / (p2[axis] - p1[axis])
                intersections.append(val)
    intersections.sort()
    return intersections

def scanline(polygons, step=1e-3):
    min_x, max_x = np.min(polygons[:, 0]), np.max(polygons[:, 0])
    min_y, max_y = np.min(polygons[:, 1]), np.max(polygons[:, 1])

    contour_points_set = set()
    fill_points = []

    for x in np.arange(min_x, max_x, step):
        intersections = find_intersections(x, polygons, axis=0)

        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                fill_points.append(rasterizar_linha(np.matrix([(x, intersections[i]), (x, intersections[i + 1])])))

        if intersections:
            contour_points_set.add((x, intersections[0]))
            contour_points_set.add((x, intersections[-1]))

    for y in np.arange(min_y, max_y, step):
        intersections = find_intersections(y, polygons, axis=1)

        if intersections:
            contour_points_set.add((intersections[0], y))
            contour_points_set.add((intersections[-1], y))

    contour_points = np.matrix(list(contour_points_set))

    if fill_points:
      fill_points = np.concatenate(fill_points)

    return contour_points, fill_points
