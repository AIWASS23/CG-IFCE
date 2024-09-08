import numpy as np
from caixa_sem_tampa import CaixaSemTampa
from caneca import Caneca
from cano import Cano
from cone import Cone
from plotar_solido import plota_solido
from tronco import TroncoDeCone

cone = Cone(
    raio=2.0,
    altura=4.0,
    cor = "red"
)

tronco = TroncoDeCone(
    raio_base_inferior=4.0,
    raio_base_superior=2.0,
    altura=4.0
)

caixa = CaixaSemTampa(
    lado=5.0,
    altura=2.0
)

cano = Cano(
    P1=np.array([-9, -2, -9]),
    P2=np.array([9, 9, 0]),
    T1=np.array([-4, 2, -4]),
    T2=np.array([10, 5, 0]),
    raio=1.0
)

# cano1, cano1_faceColor, cano1_edgeColor = create_cano([-9, -2, -9], [10, 10, 0], [-4, -2, -4], [10, 5, 0], radius=0.5)


caneca = Caneca(
    raio_base=2.0,
    altura=4.0,
    raio_alca=0.5
)

if __name__ == '__main__':
    #plota_solido(caixa, com_pontos=False, com_arestas=True, com_eixos=True, com_faces=True)
    #plota_solido(tronco, com_pontos=False, com_arestas=True, com_eixos=True, com_faces=False)
    #plota_solido(cone, com_pontos=True, com_arestas=False, com_eixos=True, com_faces=False)
    #plota_solido(cano, com_pontos=False, com_arestas=False, com_eixos=True, com_faces=True)
    plota_solido(caneca, com_pontos=False, com_arestas=False, com_eixos=True, com_faces=True)
