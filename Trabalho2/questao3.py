from typing import List
import numpy as np
from numpy import ndarray
from caixa_sem_tampa import CaixaSemTampa
from caneca import Caneca
from cano import Cano
from cone import Cone
from plotar_solido import plota_solidos
from solido import Solido
from tronco import TroncoDeCone

# Definição dos sólidos
cone = Cone(raio=1.0, altura=2.0, cor="red")
tronco = TroncoDeCone(raio_base_inferior=2.0, raio_base_superior=1.0, altura=2.0)
caixa = CaixaSemTampa(lado=4.0, altura=1.0)
cano = Cano(P1=np.array([0, 3, 0]), P2=np.array([3, 0, 0]), T1=np.array([5, 0, 0]), T2=np.array([0, 5, 0]), raio=1.0)
caneca = Caneca(raio_base=1.0, altura=2.0, raio_alca=1.0)

cone.adiciona_nos_eixos(5, 5, 5)
cano.adiciona_nos_eixos(4, 4, 4)  
tronco.adiciona_nos_eixos(3, 3, 3)  
caneca.adiciona_nos_eixos(2, 2, 2)
caixa.adiciona_nos_eixos(1, 1, 1) 

solidos = list()
solidos.append(cone)
solidos.append(cano)
solidos.append(tronco)
solidos.append(caneca)
solidos.append(caixa)

def centro_de_massa_dos_solidos(solidos: List[Solido]) -> ndarray:
    centro_de_massa = np.array([0.0, 0.0, 0.0])

    for solido in solidos:
        centro_de_massa += np.array(solido.centro_de_massa())
    centro_de_massa /= len(solidos)
    return centro_de_massa

cm_solidos = centro_de_massa_dos_solidos(solidos)

# Foi escolhido o octante V (+, +, -)
# Parâmetros Extrínsecos da Câmera
# Ponto de origem, em relação ao SCM, da câmera

origem_camera = np.array([5, 4, -1])
# n, v e u devem ser normalizados
n = (cm_solidos - origem_camera)
n_norm = np.sqrt(sum(n ** 2))

up = np.array([0, 1, 0])  # vetor up, que indica a direção a ser usada como direção vertical da imagem

v = up - (np.dot(up, n) / n_norm ** 2) * n

n = n / n_norm  # normalizando o vetor n
v = v / np.sqrt(sum(v ** 2))  # normalizando o vetor v

u = np.cross(v, n)  # como v e n estão normalizados, u também está normalizado

# A matriz de translação é obtida como a matriz que leva a posição da câmera p = (xc, yc, zc) para a origem
T = np.matrix([
    [1, 0, 0, -origem_camera[0]],
    [0, 1, 0, -origem_camera[1]],
    [0, 0, 1, -origem_camera[2]],
    [0, 0, 0, 1]
])

# Matriz de rotação do Sistema de Coordenadas do Mundo para o da Câmera
R = np.matrix([
    [u[0], u[1], u[2], 0],
    [v[0], v[1], v[2], 0],
    [n[0], n[1], n[2], 0],
    [0, 0, 0, 1]
])

V = R * T


# # Multiplicação dos sólidos pela matriz V, agora todos os sólidos estão no SCC
# cone.multiplicacao_por_matriz(V)
# tronco.multiplicacao_por_matriz(V)
# caixa.multiplicacao_por_matriz(V)
# cano.multiplicacao_por_matriz(V)

# if __name__ == '__main__':
#     plota_solidos(solidos, titulo="Sólidos no SCC", tem_volume_visao=True)

if __name__ == '__main__':
    # Visualiza o estado original dos sólidos
    plota_solidos(solidos, titulo="Sólidos no SCM", tem_volume_visao=False)
    
    # Aplica a transformação SCC
    for solido in solidos:
        solido.multiplicacao_por_matriz(V)
    
    # Visualiza o estado transformado dos sólidos
    plota_solidos(solidos, titulo="Sólidos no SCC", tem_volume_visao=True)