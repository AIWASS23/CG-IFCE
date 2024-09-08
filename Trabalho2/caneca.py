import numpy as np
from solido import Solido


# def constroi_vertices_caneca(raio_base: float, altura: float, raio_alca: float, num_divisoes: int = 20):
#     vertices = dict()

#     for i in range(num_divisoes):
#         angulo = 2 * np.pi * i / num_divisoes
#         x = raio_base * np.cos(angulo)
#         y = raio_base * np.sin(angulo)
#         vertices[f"Vbase_inf{i + 1}"] = [x, y, 0]
#         vertices[f"Vbase_sup{i + 1}"] = [x, y, altura]

#     for i in range(num_divisoes // 2):
#         angulo = np.pi * i / (num_divisoes // 2 - 1)
#         x = raio_alca * np.cos(angulo) + raio_base + raio_alca
#         z = raio_alca * np.sin(angulo) + altura / 2
#         vertices[f"Valca{i + 1}"] = [x, 0, z]

#     return vertices

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



# def constroi_arestas_caneca(num_divisoes: int = 20):
#     arestas = dict()

#     for i in range(num_divisoes):
#         if i == num_divisoes - 1:
#             arestas[f"Acorpo{i + 1}"] = (f"Vbase_inf{i + 1}", "Vbase_inf1")
#             arestas[f"Acorpo{i + 1 + num_divisoes}"] = (f"Vbase_sup{i + 1}", "Vbase_sup1")
#         else:
#             arestas[f"Acorpo{i + 1}"] = (f"Vbase_inf{i + 1}", f"Vbase_inf{i + 2}")
#             arestas[f"Acorpo{i + 1 + num_divisoes}"] = (f"Vbase_sup{i + 1}", f"Vbase_sup{i + 2}")
#         arestas[f"Acorpo{i + 1 + 2 * num_divisoes}"] = (f"Vbase_inf{i + 1}", f"Vbase_sup{i + 1}")

#     for i in range(num_divisoes // 2 - 1):
#         arestas[f"Aalca{i + 1}"] = (f"Valca{i + 1}", f"Valca{i + 2}")

#     arestas["Aconector1"] = ("Vbase_sup1", "Valca1")
#     arestas["Aconector2"] = (f"Vbase_sup{num_divisoes // 2}", f"Valca{num_divisoes // 2}")

#     return arestas

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


# def constroi_faces_caneca(num_divisoes: int = 20):
#     faces = dict()
#     for i in range(num_divisoes):
#         if i == num_divisoes - 1:
#             faces[f"Fcorpo{i + 1}"] = (f"Vbase_inf{i + 1}", "Vbase_inf1", "Vbase_sup1", f"Vbase_sup{i + 1}")
#         else:
#             faces[f"Fcorpo{i + 1}"] = (f"Vbase_inf{i + 1}", f"Vbase_inf{i + 2}", f"Vbase_sup{i + 2}", f"Vbase_sup{i + 1}")

#     faces["Fbase_inf"] = tuple(f"Vbase_inf{i + 1}" for i in range(num_divisoes))
#     faces["Fbase_sup"] = tuple(f"Vbase_sup{i + 1}" for i in range(num_divisoes))

#     # Ajustar faces da alça (garantir que todos os vértices referenciados existam)
#     if num_divisoes // 2 > 1:
#         for i in range(num_divisoes // 2 - 1):
#             faces[f"Falca{i + 1}"] = (f"Valca{i + 1}", f"Valca{i + 2}", f"Vbase_sup{num_divisoes // 2}", "Vbase_sup1")

#     return faces

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

