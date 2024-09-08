
import numpy as np
import math
import cv2

# limites da window
x_min_w = -1
y_min_w = -1
x_max_w = 1
y_max_w = 1

# limites da viewport

x_min_v = 0
y_min_v = 0
x_max_v = 500
y_max_v = 500

white = (255, 255, 255)


def get_input(nome):
    variavel = 0

    while True:
        try:
            variavel = float(input(f"{nome}: "))
            break
        except TypeError:
            print("O valor informado é inválido")
            continue

    return variavel


def multiplica_pontos(pontos, matriz):

    return np.array([matriz.dot(ponto) for ponto in pontos])


def mostra_pontos(pontos):
    [print(ponto) for ponto in pontos]


def normaliza_pontos(pontos):

    for i in range(len(pontos)):
        pontos[i] = pontos[i] / pontos[i][3]

    return pontos


def mapear_pontos(mat):

    pontos = []

    for ponto in mat:
        px = (((ponto[0] - x_min_w) * (x_max_v - x_min_v)) / (x_max_w - x_min_w)) + x_min_v
        py = (((ponto[1] - y_min_w) * (y_max_v - y_min_v)) / (y_max_w - y_min_w)) + y_min_v

        pontos.append(tuple((int(px), int(py))))

    return pontos


def desenha_linha(img, p1, p2):

    try:
        c1 = 0 <= p1[0] <= 400
        c2 = 0 <= p1[1] <= 400

        c3 = 0 <= p2[0] <= 400
        c4 = 0 <= p2[1] <= 400

        if (c1 and c2) or (c3 and c4):
            cv2.line(img, (p1[0], p1[1]), (p2[0], p2[1]), white, 3)

    except:
        print("Fora da tela")


def desenha_piramide(pontos):
    canvas = np.zeros((400, 400, 3), dtype="uint8")

    desenha_linha(canvas, pontos[0], pontos[1])
    desenha_linha(canvas, pontos[0], pontos[2])
    desenha_linha(canvas, pontos[0], pontos[3])
    desenha_linha(canvas, pontos[0], pontos[4])
    desenha_linha(canvas, pontos[1], pontos[2])
    desenha_linha(canvas, pontos[1], pontos[3])
    desenha_linha(canvas, pontos[2], pontos[4])
    desenha_linha(canvas, pontos[3], pontos[4])

    cv2.imshow("Pipeline", canvas)


def rotacao_x(angulo):
    angx = math.radians(angulo)

    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(angx), -math.sin(angx), 0],
        [0, math.sin(angx), math.cos(angx), 0],
        [0, 0, 0, 1]
    ])


def rotacao_y(angulo):
    angy = math.radians(angulo)

    return np.array([
        [math.cos(angy), 0, math.sin(angy), 0],
        [0, 1, 0, 0],
        [-math.sin(angy), 0, math.cos(angy), 0],
        [0, 0, 0, 1]
    ])


def rotacao_z(angulo):
    angz = math.radians(angulo)

    return np.array([
        [math.cos(angz), -math.sin(angz), 0, 0],
        [math.sin(angz), math.cos(angz), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def projecao_perspectiva():
    fovy = math.radians(80.0)
    aspect = 1.0
    z_near = 0.1
    z_far = 100

    a = 1 / (math.tan(fovy / 2) * aspect)
    b = 1 / (math.tan(fovy / 2))
    c = (z_far + z_near) / (z_near - z_far)
    d = (2 * (z_far * z_near)) / (z_near - z_far)

    return np.array([
        [a, 0, 0, 0],
        [0, b, 0, 0],
        [0, 0, c, d],
        [0, 0, -1, 0]
    ])


# def projecao_paralela(*mat):
#     pontos_x = []
#     pontos_y = []
#     pontos_z = []
#
#     for ponto in mat:
#         pontos_x.append(ponto[0])
#         pontos_y.append(ponto[1])
#         pontos_z.append(ponto[2])
#
#     top = -2#min(pontos_y)
#     bottom = 2#max(pontos_y)
#     right = 2#max(pontos_x)
#     left = -2#min(pontos_x)
#
#     z_near = 0.01#max(pontos_z)
#     z_far = 100#min(pontos_z)
#
#     a = 2 / (right - left)
#     b = 2 / (top - bottom)
#     c = -(2 / (z_far - z_near))
#     d = -((z_far + z_near) / (z_far - z_near))
#     e = -((top + bottom) / (top - bottom))
#     f = -((right + left) / (right - left))
#
#     return np.array([
#         [a, 0, 0, f],
#         [0, b, 0, e],
#         [0, 0, c, d],
#         [0, 0, 0, 1]
#     ])


# 1) Modelagem do objeto - piramide
piramide = np.array([
    [0, 0, -0.5, 1],
    [-0.5, -0.5, 0, 1],
    [0.5, -0.5, 0, 1],
    [-0.5, 0.5, 0, 1],
    [0.5, 0.5, 0, 1]
])

projecao_atual = projecao_perspectiva()

mat_identidade = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

tx_obj = 0
ty_obj = 0
tz_obj = 0

obj_ang_x = 70
obj_ang_y = 0
obj_ang_z = 0

sx = 1
sy = 1
sz = 1

tx_cam = 0
ty_cam = 0
tz_cam = -2

cam_ang_x = 0
cam_ang_y = -10
cam_ang_z = 0

print("\nCoordenadas do modelo")
mostra_pontos(piramide)

while True:
    # a. Matriz de transformação do modelo
    translacao = np.array([
        [1, 0, 0, tx_obj],
        [0, 1, 0, ty_obj],
        [0, 0, 1, tz_obj],
        [0, 0, 0, 1]
    ])

    # rotacao em x
    rot_x = rotacao_x(obj_ang_x)

    # rotacao em y
    rot_y = rotacao_y(obj_ang_y)

    # rotacao em z
    rot_z = rotacao_z(obj_ang_z)

    rotacao = rot_z.dot(rot_y.dot(rot_x))

    # escala
    escala = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

    matrizModelo = escala.dot(rotacao.dot(translacao))

    # 2) Coordenadas do mundo
    coordenadas_mundo = multiplica_pontos(piramide, matrizModelo)

    print("\nCoordenadas do mundo")
    mostra_pontos(coordenadas_mundo)

    # Translação da câmera
    translacaoCam = np.array([
        [1, 0, 0, -tx_cam],
        [0, 1, 0, -ty_cam],
        [0, 0, 1, -tz_cam],
        [0, 0, 0, 1]
    ])

    # rotação da câmera
    rot_x_cam = rotacao_x(-cam_ang_x)

    # rotacao em y
    rot_y_cam = rotacao_y(-cam_ang_y)

    rot_z_cam = rotacao_z(-cam_ang_z)

    cam_rot = rot_z_cam.dot(rot_y_cam.dot(rot_x_cam))

    matrizVisualizacao = cam_rot.dot(translacaoCam)

    # 3) Coordenadas de visualização
    coordenadas_visualizacao = multiplica_pontos(coordenadas_mundo, matrizVisualizacao)

    print("\nCoordenadas de visualização")
    mostra_pontos(coordenadas_visualizacao)

    # c. Matriz de projeção
    # projeção perspectiva
    matriz_projecao = projecao_atual

    # 4) Coordenadas de projeção
    coordenadas_projecao = multiplica_pontos(coordenadas_visualizacao, matriz_projecao)
    coordenadas_projecao = normaliza_pontos(coordenadas_projecao)

    print("\nCoordenadas de projeção")
    mostra_pontos(coordenadas_projecao)

    # d. Mapeamento
    print("\nMapeamento\n")

    pontos_mapeados = mapear_pontos(coordenadas_projecao)
    mostra_pontos(pontos_mapeados)

    desenha_piramide(pontos_mapeados)

    print("\n\nPipeline de visualização 3D\n")

    print("Opções:\n"
          "1. Manipular o objeto\n"
          "2. Manipular a câmera\n"
          "3. Modificar projeção\n"
          "4. Modificar mapeamento\n"
          "5. Sair\n")

    key = cv2.waitKey(0)

    if key == 49:
        print("Manipular o objeto:\n"
              "1. Translação\n"
              "2. Escala\n"
              "3. Rotação em X\n"
              "4. Rotação em Y\n"
              "5. Rotação em Z\n"
              "6. Voltar\n")

        key = cv2.waitKey(0)

        if key == 49:
            print(f"Translação atual x:{tx_obj}, y:{ty_obj}, z:{tz_obj}")
            tx_obj = get_input("Translação em X")
            ty_obj = get_input("Translação em Y")
            tz_obj = get_input("Translação em Z")

        elif key == 50:
            print(f"Escala atual x:{sx}, y:{sy}, z:{sz}")
            sx = get_input("Escala em X")
            sy = get_input("Escala em Y")
            sz = get_input("Escala em Z")

        elif key == 51:
            print(f"Ângulo atual x: {obj_ang_x}")
            obj_ang_x = get_input("Ângulo em X")

        elif key == 52:
            print(f"Ângulo atual y: {obj_ang_y}")
            obj_ang_y = get_input("Ângulo em Y")

        elif key == 53:
            print(f"Ângulo atual z: {obj_ang_z}")
            obj_ang_z = get_input("Ângulo em Z")

    elif key == 50:
        print("Manipular a câmera:\n"
              "1. Translação\n"
              "2. Rotação em X\n"
              "3. Rotação em Y\n"
              "4. Rotação em Z\n"
              "5. Voltar\n")

        key = cv2.waitKey(0)

        if key == 49:
            print(f"Translação atual x:{tx_cam}, y:{ty_cam}, z:{tz_cam}")
            tx_cam = get_input("Translação em X")
            ty_cam = get_input("Translação em Y")
            tz_cam = get_input("Translação em Z")

        elif key == 50:
            print(f"Ângulo atual x: {cam_ang_x}")
            cam_ang_x = get_input("Ângulo em X")

        elif key == 51:
            print(f"Ângulo atual y: {cam_ang_y}")
            cam_ang_y = get_input("Ângulo em Y")

        elif key == 52:
            print(f"Ângulo atual z: {cam_ang_z}")
            cam_ang_z = get_input("Ângulo em Z")

    elif key == 51:
        print("Modificar projeção:\n"
              "1. Projeção perspectiva\n"
              "2. Projeção paralela\n"
              "3. Voltar\n")

        key = cv2.waitKey(0)

        if key == 49:
            projecao_atual = projecao_perspectiva()

        elif key == 50:
            print("Não funciona :(")

    elif key == 52:
        print("Modificar mapeamento:\n"
              "1. Window\n"
              "2. Viewport\n"
              "3. Voltar\n")

        key = cv2.waitKey(0)

        if key == 49:
            print(f"Valores atuais: \n"
                  f"x_min_w: {x_min_w}\n"
                  f"x_max_w: {x_max_w}\n"
                  f"y_min_w: {y_min_w}\n"
                  f"y_max_w: {y_max_w}\n")

            x_min_w = get_input("Valor para x_min_w")
            x_max_w = get_input("Valor para x_max_w")
            y_min_w = get_input("Valor para y_min_w")
            y_max_w = get_input("Valor para y_max_w")

        elif key == 50:
            print(f"Valores atuais: \n"
                  f"x_min_v: {x_min_v}\n"
                  f"x_max_v: {x_max_v}\n"
                  f"y_min_v: {y_min_v}\n"
                  f"y_max_v: {y_max_v}\n")

            x_min_v = get_input("Valor para x_min_v")
            x_max_v = get_input("Valor para x_max_v")
            y_min_v = get_input("Valor para y_min_v")
            y_max_v = get_input("Valor para y_max_v")

    elif key == 53:
        break

