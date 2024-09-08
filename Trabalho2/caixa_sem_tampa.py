from solido import Solido


def constroi_vertices_caixa(lado: float, altura: float):
    vertices = dict()

    vertices["V1"] = [-lado / 2, -lado / 2, 0]
    vertices["V2"] = [lado / 2, -lado / 2, 0]
    vertices["V3"] = [-lado / 2, lado / 2, 0]
    vertices["V4"] = [lado / 2, lado / 2, 0]

    vertices["V5"] = [-lado / 2, -lado / 2, altura]
    vertices["V6"] = [lado / 2, -lado / 2, altura]
    vertices["V7"] = [-lado / 2, lado / 2, altura]
    vertices["V8"] = [lado / 2, lado / 2, altura]

    return vertices


def constroi_arestas_caixa():
    arestas = dict()

    arestas["A1"] = ("V1", "V2")
    arestas["A2"] = ("V2", "V4")
    arestas["A3"] = ("V4", "V3")
    arestas["A4"] = ("V3", "V1")

    arestas["A5"] = ("V5", "V6")
    arestas["A6"] = ("V6", "V8")
    arestas["A7"] = ("V8", "V7")
    arestas["A8"] = ("V7", "V5")

    arestas["A9"] = ("V1", "V5")
    arestas["A10"] = ("V2", "V6")
    arestas["A11"] = ("V3", "V7")
    arestas["A12"] = ("V4", "V8")

    return arestas

def constroi_faces_caixa():
    faces = []

    faces.append(["V1", "V2", "V4", "V3"])
    faces.append(["V1", "V2", "V6", "V5"])
    faces.append(["V2", "V4", "V8", "V6"])
    faces.append(["V1", "V3", "V7", "V5"])
    faces.append(["V3", "V4", "V8", "V7"])

    return faces

class CaixaSemTampa(Solido):

    def __init__(
            self,
            lado: float,
            altura: float,
            titulo: str = "Caixa Sem Tampa",
            cor: str = "brown"):
        super().__init__(
            constroi_vertices_caixa(lado, altura),
            constroi_arestas_caixa(),
            constroi_faces_caixa(),
            titulo,
            cor
        )
