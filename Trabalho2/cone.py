import numpy as np
from solido import Solido
from typing import List


def constroi_vertices_cone(raio: float, altura: float, num_divisoes: int = 20):
    vertices = dict()
    # Base inferior
    for i in range(num_divisoes):
        angulo = 2 * np.pi * i / num_divisoes
        x = raio * np.cos(angulo)
        y = raio * np.sin(angulo)
        vertices[f"V{i + 1}"] = [x, y, 0]

    # Vértice superior (ápice)
    vertices["Vápice"] = [0, 0, altura]

    return vertices


def constroi_arestas_cone(num_divisoes: int = 20):
    arestas = dict()
    # Arestas da base
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            arestas[f"A{i + 1}"] = (f"V{i + 1}", "V1")  # Última aresta conecta o último vértice ao primeiro
        else:
            arestas[f"A{i + 1}"] = (f"V{i + 1}", f"V{i + 2}")

    # Arestas laterais
    for i in range(num_divisoes):
        arestas[f"AL{i + 1}"] = (f"V{i + 1}", "Vápice")

    return arestas

def constroi_faces_cone(num_divisoes: int = 20) -> List[List[str]]:
    faces = []
    # Faces laterais
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            faces.append([f"V{i + 1}", "Vápice", "V1"])  # Última face conecta o último vértice ao primeiro
        else:
            faces.append([f"V{i + 1}", "Vápice", f"V{i + 2}"])

    # Base inferior
    base_face = [f"V{i + 1}" for i in range(num_divisoes)]
    faces.append(base_face)

    return faces


class Cone(Solido):
    """
    Cone com base circular de raio e uma altura definida.
    """

    def __init__(
            self,
            raio: float,
            altura: float,
            num_divisoes: int = 20,
            titulo: str = "Cone",
            cor: str = "orange"):
        super().__init__(
            constroi_vertices_cone(raio, altura, num_divisoes),
            constroi_arestas_cone(num_divisoes),
            constroi_faces_cone(num_divisoes),
            titulo,
            cor
        )
