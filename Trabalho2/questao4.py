import numpy as np
from matplotlib import pyplot as plt
from caixa_sem_tampa import CaixaSemTampa
from caneca import Caneca
from cano import Cano
from cone import Cone
from tronco import TroncoDeCone

def matriz_projecao_perspectiva(fov: float, aspect: float, near: float, far: float):
    fov_rad = np.radians(fov)
    f = 1 / np.tan(fov_rad / 2)
    z_range = near - far

    return np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / z_range, (2 * far * near) / z_range],
        [0, 0, -1, 0]
    ], dtype=float)

def aplica_projecao(solidos, P):
    for solido in solidos:
        for chave_vertice in solido.vertices:  
            vertice = solido.vertices[chave_vertice]  
            vertice = np.array(vertice, dtype=float) 
            vertice_projetado = np.dot(P, np.append(vertice, 1)) 
            print(f"Vértice projetado: {vertice_projetado}")

def verifica_vertices(solidos):
    for solido in solidos:
        for i, vertice in enumerate(solido.vertices):
            if not isinstance(vertice, (list, np.ndarray)) or not all(isinstance(coord, (int, float)) for coord in vertice):
                print(f"Erro: Vértice inválido no sólido {solido}: {vertice}")

def plot_faces(ax, solido):
    if isinstance(solido.faces, dict):
        faces = solido.faces.values()
    else:
        faces = solido.faces

    for face in faces:
        face_vertices = [solido.vertices[vertex_index] for vertex_index in face]
        face_vertices.append(face_vertices[0])
        x = [v[0] for v in face_vertices]
        y = [v[1] for v in face_vertices]
        ax.fill(x, y, color=solido.cor, alpha=0.5)

fov = 200.0  # Campo de visão em graus
aspect = 3.0  # Proporção largura/altura
near = 10.0  # Distância do plano de recorte próximo
far = 100.0  # Distância do plano de recorte distante
P = matriz_projecao_perspectiva(fov, aspect, near, far)

# Definição dos sólidos
cone = Cone(raio=1.0, altura=2.0, cor="red")
tronco = TroncoDeCone(raio_base_inferior=2.0, raio_base_superior=1.0, altura=2.0)
caixa = CaixaSemTampa(lado=4.0, altura=1.0)
cano = Cano(P1=np.array([0, 3, 0]), P2=np.array([3, 0, 0]), T1=np.array([5, 0, 0]), T2=np.array([0, 5, 0]), raio=1.0)
caneca = Caneca(raio_base=1.0, altura=2.0, raio_alca=1.0)

# Adiciona deslocamentos para evitar sobreposições
cone.adiciona_nos_eixos(5, 0, 0)
cano.adiciona_nos_eixos(-8, 0, 0)
tronco.adiciona_nos_eixos(0, 5, 0)
caneca.adiciona_nos_eixos(0, -5, 0)
caixa.adiciona_nos_eixos(0, 0, 5)

solidos = [cone, cano, tronco, caneca, caixa]

if __name__ == '__main__':
    aplica_projecao(solidos, P)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Projeção 2D dos Sólidos")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    
    for solido in solidos:
        plot_faces(ax, solido)
        for key, value in solido.arestas.items():
            pontos = [solido.vertices[value[0]], solido.vertices[value[1]]]
            x = [pontos[0][0], pontos[1][0]]
            y = [pontos[0][1], pontos[1][1]]
            ax.plot(x, y, color=solido.cor)

    plt.savefig("projecao2D.png")
    plt.show()
