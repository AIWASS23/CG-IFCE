import numpy as np
from solido import Solido

def curva_hermite(P1, P2, T1, T2, t):

    h1 = 2 * t ** 3 - 3 * t ** 2 + 1
    h2 = -2 * t ** 3 + 3 * t ** 2
    h3 = t ** 3 - 2 * t ** 2 + t
    h4 = t ** 3 - t ** 2

    return h1 * P1 + h2 * P2 + h3 * T1 + h4 * T2


def constroi_vertices_cano(P1: np.array, P2: np.array, T1: np.array, T2: np.array, raio: float, num_divisoes: int = 20,
                           num_pontos_circ: int = 20):
    vertices = dict()

    for i in range(num_divisoes):
        t = i / (num_divisoes - 1)
        centro = curva_hermite(P1, P2, T1, T2, t)

        # Construir circunferência ao redor do ponto na curva
        for j in range(num_pontos_circ):
            angulo = 2 * np.pi * j / num_pontos_circ
            x = raio * np.cos(angulo)
            y = raio * np.sin(angulo)
            vertices[f"V{i * num_pontos_circ + j + 1}"] = [centro[0] + x, centro[1] + y, centro[2]]

    return vertices


def constroi_arestas_cano(num_divisoes: int = 20, num_pontos_circ: int = 20):
    arestas = dict()

    # Arestas ao longo da circunferência
    for i in range(num_divisoes):
        for j in range(num_pontos_circ):
            if j == num_pontos_circ - 1:
                arestas[f"Ac{i * num_pontos_circ + j + 1}"] = (
                f"V{i * num_pontos_circ + j + 1}", f"V{i * num_pontos_circ + 1}")
            else:
                arestas[f"Ac{i * num_pontos_circ + j + 1}"] = (
                f"V{i * num_pontos_circ + j + 1}", f"V{i * num_pontos_circ + j + 2}")

    # Arestas ao longo do comprimento do cano
    for i in range(num_divisoes - 1):
        for j in range(num_pontos_circ):
            arestas[f"Al{i * num_pontos_circ + j + 1}"] = (
            f"V{i * num_pontos_circ + j + 1}", f"V{(i + 1) * num_pontos_circ + j + 1}")

    return arestas

def constroi_faces_cano(num_divisoes: int = 20, num_pontos_circ: int = 20):
    faces = []

    for i in range(num_divisoes - 1):
        for j in range(num_pontos_circ):
            if j == num_pontos_circ - 1:
                faces.append([f"V{i * num_pontos_circ + j + 1}",
                              f"V{i * num_pontos_circ + 1}",
                              f"V{(i + 1) * num_pontos_circ + 1}",
                              f"V{(i + 1) * num_pontos_circ + j + 1}"])
            else:
                faces.append([f"V{i * num_pontos_circ + j + 1}",
                              f"V{i * num_pontos_circ + j + 2}",
                              f"V{(i + 1) * num_pontos_circ + j + 2}",
                              f"V{(i + 1) * num_pontos_circ + j + 1}"])

    return faces


class Cano(Solido):

    def __init__(
            self,
            P1: np.array,
            P2: np.array,
            T1: np.array,
            T2: np.array,
            raio: float,
            num_divisoes: int = 20,
            num_pontos_circ: int = 20,
            titulo: str = "Cano",
            cor: str = "gray"):

        super().__init__(
            constroi_vertices_cano(P1, P2, T1, T2, raio, num_divisoes, num_pontos_circ),
            constroi_arestas_cano(num_divisoes, num_pontos_circ),
            constroi_faces_cano(num_divisoes, num_pontos_circ),
            titulo,
            cor
        )
