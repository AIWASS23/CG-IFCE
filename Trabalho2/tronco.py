import numpy as np
from solido import Solido
from typing import List


def constroi_vertices_tronco_cone(raio_base_inferior: float, raio_base_superior: float, altura: float,
                                  num_divisoes: int = 20):
    vertices = dict()

    # Base inferior
    for i in range(num_divisoes):
        angulo = 2 * np.pi * i / num_divisoes
        x_inferior = raio_base_inferior * np.cos(angulo)
        y_inferior = raio_base_inferior * np.sin(angulo)
        vertices[f"Vbi{i + 1}"] = [x_inferior, y_inferior, 0]

    # Base superior
    for i in range(num_divisoes):
        angulo = 2 * np.pi * i / num_divisoes
        x_superior = raio_base_superior * np.cos(angulo)
        y_superior = raio_base_superior * np.sin(angulo)
        vertices[f"Vbs{i + 1}"] = [x_superior, y_superior, altura]

    return vertices


def constroi_arestas_tronco_cone(num_divisoes: int = 20):
    arestas = dict()

    # Arestas da base inferior
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            arestas[f"Abi{i + 1}"] = (f"Vbi{i + 1}", "Vbi1")  # Última aresta conecta o último vértice ao primeiro
        else:
            arestas[f"Abi{i + 1}"] = (f"Vbi{i + 1}", f"Vbi{i + 2}")

    # Arestas da base superior
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            arestas[f"Abs{i + 1}"] = (f"Vbs{i + 1}", "Vbs1")  # Última aresta conecta o último vértice ao primeiro
        else:
            arestas[f"Abs{i + 1}"] = (f"Vbs{i + 1}", f"Vbs{i + 2}")

    # Arestas laterais conectando a base inferior à base superior
    for i in range(num_divisoes):
        arestas[f"Al{i + 1}"] = (f"Vbi{i + 1}", f"Vbs{i + 1}")

    return arestas

def constroi_faces_tronco_cone(num_divisoes: int = 20) -> List[List[str]]:
    faces = []

    # Faces laterais
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            # Última face conecta o último vértice da base inferior ao primeiro
            faces.append([f"Vbi{i + 1}", f"Vbs{i + 1}", "Vbs1", "Vbi1"])
        else:
            faces.append([f"Vbi{i + 1}", f"Vbs{i + 1}", f"Vbs{i + 2}", f"Vbi{i + 2}"])

    # Base inferior
    base_inferior_face = [f"Vbi{i + 1}" for i in range(num_divisoes)]
    faces.append(base_inferior_face)

    # Base superior
    base_superior_face = [f"Vbs{i + 1}" for i in range(num_divisoes)]
    faces.append(base_superior_face)

    return faces



class TroncoDeCone(Solido):
    """
    Tronco de cone com uma base superior e inferior circulares.
    """

    def __init__(
            self,
            raio_base_inferior: float,
            raio_base_superior: float,
            altura: float,
            num_divisoes: int = 20,
            titulo: str = "Tronco de Cone",
            cor: str = "blue"):

        super().__init__(
            constroi_vertices_tronco_cone(raio_base_inferior, raio_base_superior, altura, num_divisoes),
            constroi_arestas_tronco_cone(num_divisoes),
            constroi_faces_tronco_cone(num_divisoes),
            titulo,
            cor
        )
