import numpy as np
from raster_line import rasterizar_linha

def hermite_points(P_points, T_points, num_points):
  t = np.linspace(0, 1, num_points)
  T = np.matrix([t**3, t**2, t, np.ones(t.shape[0])])
  G = np.vstack((P_points, T_points))
  H = np.matrix([[2,-2,1,1], [-3,3,-2,-1], [0,0,1,0], [1,0,0,0]])
  return T.T * H * G

def hermite_blend(P_points, T_points, num_points=50):
  segments = []
  for i in range(len(P_points) - 1):
    start_index = i
    end_index = i + 2
    blended_segment = hermite_points(P_points[start_index:end_index], T_points[start_index:end_index], num_points)
    segments.append(blended_segment)
  return np.concatenate(segments, axis=0)

def calculate_blend_for_segments(P_points, T_points):
    pontos_curva = hermite_blend(P_points, T_points)
    pontos_conectados = rasterizar_linha(pontos_curva)
    return pontos_conectados