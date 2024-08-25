import numpy as np


class Resolucao:
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura


class Imagem:
    def __init__(self) -> None:
        pass

    def criar_imagem_geometrica(imagem, todos_os_pontos) -> any:
        for pontos in todos_os_pontos:
            eixo_x = []
            eixo_y = []
            for ponto in pontos:
                eixo_x.append(int(ponto[0]))
                eixo_y.append(int(ponto[1]))
            imagem[eixo_y, eixo_x] = [255, 0, 0]
        return imagem

    def criar_imagem_reta(imag, pontos) -> any:
        eixo_x = []
        eixo_y = []
        for ponto in pontos:
            eixo_x.append(int(ponto[0]))
            eixo_y.append(int(ponto[1]))
        imag[eixo_y, eixo_x] = [255, 0, 0]
        return imag
