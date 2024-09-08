import os
from typing import List
from matplotlib import pyplot as plt
from solido import Solido
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plota_faces_caneca(solido: Solido, ax) -> None:
    for face_name, face in solido.faces.items():
        try:
            x = [solido.vertices[vertice][0] for vertice in face]
            y = [solido.vertices[vertice][1] for vertice in face]
            z = [solido.vertices[vertice][2] for vertice in face]
            verts = [list(zip(x, y, z))]
            ax.add_collection3d(Poly3DCollection(verts, color=solido.cor, alpha=0.5, linewidths=1, edgecolors='r'))
        except KeyError as e:
            print(f"Erro ao acessar o vértice {e} para a face {face_name}")


def plota_faces(solido: Solido, ax) -> None:
    for face in solido.faces:
        x = [solido.vertices[vertice][0] for vertice in face]
        y = [solido.vertices[vertice][1] for vertice in face]
        z = [solido.vertices[vertice][2] for vertice in face]
        verts = [list(zip(x, y, z))]
        ax.add_collection3d(Poly3DCollection(verts, color=solido.cor, alpha=0.5, linewidths=1, edgecolors='r'))


def inicia_grafico():
    fig = plt.figure(constrained_layout=True)
    ax = fig.add_subplot(111, projection='3d')
    return fig, ax


def plota_pontos(solido: Solido, ax) -> None:
    for nome, vertice in solido.vertices.items():
        ax.scatter(vertice[0], vertice[1], vertice[2], c=solido.cor)
        ax.text(vertice[0], vertice[1], vertice[2], nome, size=12, zorder=1, color='k')


def plota_arestas(solido: Solido, ax) -> None:
    for key, value in solido.arestas.items():
        pontos = [solido.vertices[value[0]], solido.vertices[value[1]]]
        x = [pontos[0][0], pontos[1][0]]
        y = [pontos[0][1], pontos[1][1]]
        z = [pontos[0][2], pontos[1][2]]
        ax.plot(x, y, z, color=solido.cor)


def plota_eixos(ax) -> None:
    ax.plot([40, -40], [0, 0], [0, 0], color='black', linestyle='dashed', linewidth=1)
    ax.plot([0, 0], [40, -40], [0, 0], color='black', linestyle='dashed', linewidth=1)
    ax.plot([0, 0], [0, 0], [40, -40], color='black', linestyle='dashed', linewidth=1)


def plota_solido(
        solido: Solido,
        com_arestas=True,
        com_pontos=False,
        com_faces=False,
        com_eixos=True) -> None:

    fig, ax = inicia_grafico()
    nome_imagem = solido.titulo

    if com_pontos:
        plota_pontos(solido, ax)
        nome_imagem = nome_imagem + "ComPontos"

    if com_arestas:
        plota_arestas(solido, ax)
        nome_imagem = nome_imagem + "ComArestas"

    if com_faces:
        if solido.titulo.lower() == "caneca":  
            plota_faces_caneca(solido, ax)  
            nome_imagem = nome_imagem + "ComFaces"
        else:
            plota_faces(solido, ax)  
            nome_imagem = nome_imagem + "ComFaces"

    if com_eixos:
        plota_eixos(ax)
        nome_imagem = nome_imagem + "ComEixos"

    ax.set_title(solido.titulo)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    directory = "images/"
    if not os.path.exists(directory):
        os.makedirs(directory)


    plt.savefig(os.path.join(directory, nome_imagem + ".png"))
    plt.show()


def plota_solidos(
        solidos: List[Solido],
        com_arestas=False,
        com_pontos=False,
        com_faces=True,
        com_eixos=False,
        titulo: str = "image", tem_volume_visao=False) -> None:

    fig, ax = inicia_grafico()
    nome_imagem = titulo

    for solido in solidos:
        if com_pontos:
            plota_pontos(solido, ax)
            nome_imagem = nome_imagem + "ComPontos"

        if com_arestas:
            plota_arestas(solido, ax)
            
        if com_faces:
            if solido.titulo.lower() == "caneca":  
                plota_faces_caneca(solido, ax)  
                nome_imagem = nome_imagem + "ComFaces"
            else:
                plota_faces(solido, ax)
                nome_imagem = nome_imagem + "ComFaces"

    if com_eixos:
        plota_eixos(ax)
        nome_imagem = nome_imagem + "ComEixos"

    ax.set_title(titulo)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    if tem_volume_visao:
        ax.set_xlim(0, 6)
        ax.set_ylim(-6, 0)
        ax.set_zlim(0, 6)
    else:
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.set_zlim(-6, 6)

    directory = "images/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(os.path.join(directory, nome_imagem + ".png"))
    plt.show()
