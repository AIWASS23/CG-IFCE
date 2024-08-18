import math
import numpy as np

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
