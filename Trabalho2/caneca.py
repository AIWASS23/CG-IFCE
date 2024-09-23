import numpy as np
from solido import Solido
from typing import List, Dict
from cano import Cano

def constroi_vertices_caneca(raio_base: float, altura: float, raio_alca: float, num_divisoes: int = 20):
    vertices = dict()

    # Vertices da base e topo do corpo da caneca
    for i in range(num_divisoes):
        angulo = 2 * np.pi * i / num_divisoes
        x = raio_base * np.cos(angulo)
        y = raio_base * np.sin(angulo)
        vertices[f"Vbase_inf{i + 1}"] = [x, y, 0]
        vertices[f"Vbase_sup{i + 1}"] = [x, y, altura]

    # Vertices da alça, distribuídos em arco semicircular
    for i in range(num_divisoes // 2):
        angulo = np.pi * i / (num_divisoes // 2 - 1)
        x = raio_alca * np.cos(angulo) + raio_base + raio_alca
        z = raio_alca * np.sin(angulo) + altura / 2
        vertices[f"Valca{i + 1}"] = [x, 0, z]

    return vertices


def constroi_arestas_caneca(num_divisoes: int = 20):
    arestas = dict()

    # Arestas do corpo da caneca
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            arestas[f"Acorpo{i + 1}"] = (f"Vbase_inf{i + 1}", "Vbase_inf1")
            arestas[f"Acorpo{i + 1 + num_divisoes}"] = (f"Vbase_sup{i + 1}", "Vbase_sup1")
        else:
            arestas[f"Acorpo{i + 1}"] = (f"Vbase_inf{i + 1}", f"Vbase_inf{i + 2}")
            arestas[f"Acorpo{i + 1 + num_divisoes}"] = (f"Vbase_sup{i + 1}", f"Vbase_sup{i + 2}")
        arestas[f"Acorpo{i + 1 + 2 * num_divisoes}"] = (f"Vbase_inf{i + 1}", f"Vbase_sup{i + 1}")

    # Arestas da alça
    for i in range(num_divisoes // 2 - 1):
        arestas[f"Aalca{i + 1}"] = (f"Valca{i + 1}", f"Valca{i + 2}")

    # Conexões da alça com o corpo
    arestas["Aconector1"] = ("Vbase_sup1", "Valca1")
    arestas["Aconector2"] = (f"Vbase_sup{num_divisoes // 2}", f"Valca{num_divisoes // 2}")

    return arestas


def constroi_faces_caneca(num_divisoes: int = 20):
    faces = dict()
    
    # Faces do corpo da caneca
    for i in range(num_divisoes):
        if i == num_divisoes - 1:
            faces[f"Fcorpo{i + 1}"] = (f"Vbase_inf{i + 1}", "Vbase_inf1", "Vbase_sup1", f"Vbase_sup{i + 1}")
        else:
            faces[f"Fcorpo{i + 1}"] = (f"Vbase_inf{i + 1}", f"Vbase_inf{i + 2}", f"Vbase_sup{i + 2}", f"Vbase_sup{i + 1}")

    # Faces da base inferior e superior
    faces["Fbase_inf"] = tuple(f"Vbase_inf{i + 1}" for i in range(num_divisoes))
    faces["Fbase_sup"] = tuple(f"Vbase_sup{i + 1}" for i in range(num_divisoes))

    # Ajustar faces da alça (garantir que todos os vértices referenciados existam)
    for i in range(num_divisoes // 2 - 1):
        faces[f"Falca{i + 1}"] = (f"Valca{i + 1}", f"Valca{i + 2}")

    return faces




class Caneca(Solido):

    def __init__(self,
                 raio_base: float,
                 altura: float,
                 raio_alca: float,
                 num_divisoes: int = 20,
                 titulo: str = "Caneca",
                 cor: str = "brown"):

        super().__init__(
            constroi_vertices_caneca(raio_base, altura, raio_alca, num_divisoes),
            constroi_arestas_caneca(num_divisoes),
            constroi_faces_caneca(num_divisoes),
            titulo,
            cor
        )

# class Caneca(Solido):
#     def __init__(self, raio_base: float, altura: float, raio_alca: float, num_divisoes: int = 20, num_pontos_circ: int = 20, titulo: str = "Caneca", cor: str = "brown"):
#         vertices, faces, arestas = self.constroi_caneca(raio_base, altura, raio_alca, num_divisoes, num_pontos_circ)
#         super().__init__(vertices, arestas, faces, titulo, cor)

#     def constroi_caneca(self, raio_base: float, altura: float, raio_alca: float, num_divisoes: int, num_pontos_circ: int) -> tuple:
#         vertices = {}
#         faces = []
#         arestas = {}

#         # Vértices do corpo (base inferior e superior)
#         for i in range(num_divisoes):
#             angulo = 2 * np.pi * i / num_divisoes
#             x = raio_base * np.cos(angulo)
#             y = raio_base * np.sin(angulo)
#             vertices[f"Vbase_inf{i + 1}"] = [x, y, 0]
#             vertices[f"Vbase_sup{i + 1}"] = [x, y, altura]

#         # Faces laterais do corpo
#         for i in range(num_divisoes):
#             if i == num_divisoes - 1:
#                 faces.append([f"Vbase_inf{i + 1}", "Vbase_inf1", "Vbase_sup1", f"Vbase_sup{i + 1}"])
#             else:
#                 faces.append([f"Vbase_inf{i + 1}", f"Vbase_inf{i + 2}", f"Vbase_sup{i + 2}", f"Vbase_sup{i + 1}"])

#         # Base superior e inferior
#         faces.append([f"Vbase_inf{i + 1}" for i in range(num_divisoes)])
#         faces.append([f"Vbase_sup{i + 1}" for i in range(num_divisoes)])

#         # Construir a alça usando a classe Cano
#         p0_handler = np.array([raio_base * 1.1, 0, altura * 0.25])  # Ponto mais afastado da caneca
#         p1_handler = np.array([raio_base * 1.1, 0, altura * 0.75])  # Ponto mais afastado no topo
#         arc_t1_handler = [raio_base * 0.8, 0, 0]  # Controle da curva da alça
#         arc_t2_handler = [-raio_base * 0.8, 0, 0]

#         # Criando a alça como um objeto Cano
#         cano_alca = Cano(P1=p0_handler, P2=p1_handler, T1=np.array(arc_t1_handler), T2=np.array(arc_t2_handler), raio=raio_alca, num_divisoes=num_divisoes // 2, num_pontos_circ=num_pontos_circ)

#         # Adicionar vértices, arestas e faces da alça do cano
#         vertices.update(cano_alca.vertices)
#         faces.extend(cano_alca.faces)
#         arestas.update(cano_alca.arestas)

#         # Gerar arestas com base nos vértices do corpo
#         arestas.update(self.constroi_arestas_caneca(num_divisoes))

#         return vertices, faces, arestas

#     @staticmethod
#     def constroi_arestas_caneca(num_divisoes: int) -> Dict[str, tuple]:
#         arestas = {}
#         for i in range(num_divisoes):
#             if i == num_divisoes - 1:
#                 arestas[f"Aresta{i + 1}"] = (f"Vbase_inf{i + 1}", "Vbase_inf1")
#                 arestas[f"Aresta{i + 1 + num_divisoes}"] = (f"Vbase_sup{i + 1}", "Vbase_sup1")
#             else:
#                 arestas[f"Aresta{i + 1}"] = (f"Vbase_inf{i + 1}", f"Vbase_inf{i + 2}")
#                 arestas[f"Aresta{i + 1 + num_divisoes}"] = (f"Vbase_sup{i + 1}", f"Vbase_sup{i + 2}")
#             arestas[f"Aresta{i + 1 + 2 * num_divisoes}"] = (f"Vbase_inf{i + 1}", f"Vbase_sup{i + 1}")
#         return arestas
