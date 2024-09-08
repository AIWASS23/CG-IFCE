import numpy as np
from caixa_sem_tampa import CaixaSemTampa
from caneca import Caneca
from cano import Cano
from cone import Cone
from tronco import TroncoDeCone
from plotar_solido import plota_solidos

# Definição dos sólidos
cone = Cone(raio=1.0, altura=2.0, cor="red")
tronco = TroncoDeCone(raio_base_inferior=2.0, raio_base_superior=1.0, altura=2.0)
caixa = CaixaSemTampa(lado=5.0, altura=1.0)
cano = Cano(P1=np.array([0, 3, 0]), P2=np.array([3, 0, 0]), T1=np.array([5, 0, 0]), T2=np.array([0, 5, 0]), raio=1.0)
caneca = Caneca(raio_base=1.0, altura=2.0, raio_alca=1.0)

cone.adiciona_nos_eixos(5, 5, 5)  # Octante I (+, +, +)
cano.adiciona_nos_eixos(3, 3, 3)  # Octante I (+, +, +)

tronco.adiciona_nos_eixos(-5, 5, 5)  # Octante II (-, +, +)
caneca.adiciona_nos_eixos(-3, 3, 3)  # Octante II (-, +, +)

cone.translacao(4, 4, 4)
cone.rotacao(60, 'x')
cone.escala(1.5, 1.5, 1.5)  

cano.translacao(2, 2, 2)
cano.rotacao(60, 'x')
cone.escala(0.3, 0.4, 0.5)

tronco.translacao(-3, 3, 3)
tronco.escala(0.8, 0.8, 0.8)
tronco.rotacao(30, 'x')

caneca.translacao(-3, 3, 3)
caneca.escala(0.8, 0.8, 0.8)
caneca.cisalhamento(fator_xy=0.5, fator_xz=0.2)
caneca.rotacao(30, 'z')

solidos = [cone, cano, tronco, caneca]

if __name__ == '__main__':
    plota_solidos(solidos, titulo="Sólidos no SCM")
