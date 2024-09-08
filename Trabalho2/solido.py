from dataclasses import dataclass, field
from typing import List
import numpy as np
from numpy import ndarray


@dataclass
class Solido:
    vertices: dict = field(default_factory=dict)
    arestas: dict = field(default_factory=dict)
    faces: List[List[str]] = field(default_factory=list)
    titulo: str = ""
    cor: str = ""

    def __init__(self, vertices: dict, arestas: dict, faces: List[List[str]], titulo: str, cor: str):
        self.vertices = vertices
        self.arestas = arestas
        self.faces = faces
        self.titulo = titulo
        self.cor = cor

    def array_de_vertices(self) -> ndarray:
        return np.array(list(self.vertices.values()))

    def matriz_para_vertices(self, array_vertice: ndarray) -> None:
        for i, vertice in enumerate(self.vertices):
            self.vertices[vertice] = array_vertice[i]

    def multiplicacao_por_matriz(self, matriz: np.matrix) -> None:
        uns = [[1.0]] * len(self.vertices) 
        x = np.append(self.array_de_vertices(), uns, axis=1)
        matriz_vertices_homogenea = np.asmatrix(x)
        matriz_transposta_vertices = matriz_vertices_homogenea.transpose()

        for i, vertice in enumerate(self.vertices):
            col = matriz_transposta_vertices[:, i]
            nova_col = matriz * col
            matriz_transposta_vertices[:, i] = nova_col

        matriz_transposta_vertices = np.delete(matriz_transposta_vertices, -1, 0)  # Remove a linha de uns
        self.matriz_para_vertices(np.array(matriz_transposta_vertices.transpose()))

    def adiciona_nos_eixos(self, eixo_x: float = 0, eixo_y: float = 0, eixo_z: float = 0) -> None:
        matriz_vertices = self.array_de_vertices()
        matriz_vertices[:, [0]] = matriz_vertices[:, [0]] + eixo_x
        matriz_vertices[:, [1]] = matriz_vertices[:, [1]] + eixo_y
        matriz_vertices[:, [2]] = matriz_vertices[:, [2]] + eixo_z
        self.matriz_para_vertices(matriz_vertices)

    def centro_de_massa(self) -> List:
        matriz_vertices = self.array_de_vertices()
        media_x = np.median(matriz_vertices[:, [0]])
        media_y = np.median(matriz_vertices[:, [1]])
        media_z = np.median(matriz_vertices[:, [2]])

        return [media_x, media_y, media_z]
    
    def obter_maximo_valor_dos_vertices(self) -> float:
        matriz_vertices = self.array_de_vertices()
        max_x = np.max(np.abs(matriz_vertices[:, 0]))
        max_y = np.max(np.abs(matriz_vertices[:, 1]))
        max_z = np.max(np.abs(matriz_vertices[:, 2]))
    
        return max(max_x, max_y, max_z)
    
    def escala(self, fator_x: float, fator_y: float, fator_z: float) -> None: 
        matriz_escala = np.diag([fator_x, fator_y, fator_z, 1])
        self.multiplicacao_por_matriz(matriz_escala)

            
    def rotacao(self, angulo: float, eixo: str) -> None:
        rad = np.radians(angulo)  # Converte o ângulo para radianos

        if eixo.lower() == 'x':
            matriz_rotacao = np.array([[1, 0, 0, 0],
                                   [0, np.cos(rad), -np.sin(rad), 0],
                                   [0, np.sin(rad), np.cos(rad), 0],
                                   [0, 0, 0, 1]])
        elif eixo.lower() == 'y':
            matriz_rotacao = np.array([[np.cos(rad), 0, np.sin(rad), 0],
                                   [0, 1, 0, 0],
                                   [-np.sin(rad), 0, np.cos(rad), 0],
                                   [0, 0, 0, 1]])
        elif eixo.lower() == 'z':
            matriz_rotacao = np.array([[np.cos(rad), -np.sin(rad), 0, 0],
                                   [np.sin(rad), np.cos(rad), 0, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 1]])
        else:
            raise ValueError("Eixo inválido! Escolha entre 'x', 'y' ou 'z'.")

        self.multiplicacao_por_matriz(matriz_rotacao)


    def translacao(self, eixo_x: float, eixo_y: float, eixo_z: float) -> None:
        matriz_translacao = np.identity(4)
        matriz_translacao[0, 3] = eixo_x
        matriz_translacao[1, 3] = eixo_y
        matriz_translacao[2, 3] = eixo_z

        self.multiplicacao_por_matriz(matriz_translacao)

    def cisalhamento(self, fator_xy: float = 0, fator_xz: float = 0, fator_yx: float = 0, fator_yz: float = 0, fator_zx: float = 0, fator_zy: float = 0) -> None:
        matriz_cisalhamento = np.identity(4)

        matriz_cisalhamento[0, 1] = fator_xy  # Cisalhamento no eixo X em relação ao Y
        matriz_cisalhamento[0, 2] = fator_xz  # Cisalhamento no eixo X em relação ao Z
        matriz_cisalhamento[1, 0] = fator_yx  # Cisalhamento no eixo Y em relação ao X
        matriz_cisalhamento[1, 2] = fator_yz  # Cisalhamento no eixo Y em relação ao Z
        matriz_cisalhamento[2, 0] = fator_zx  # Cisalhamento no eixo Z em relação ao X
        matriz_cisalhamento[2, 1] = fator_zy  # Cisalhamento no eixo Z em relação ao Y

        self.multiplicacao_por_matriz(matriz_cisalhamento)