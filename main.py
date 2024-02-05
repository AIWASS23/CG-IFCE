import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

def translacao(img, tx, ty):
    l, c = img.size
    new_img = Image.new("L", (l*2, c*2))

    m = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0,  1]])

    for x in range(l):
        for y in range(c):
            pxl = img.getpixel((x, y))
            v = [x, y, 1]

            new_x = int(m[0, 0]* v[0] + m[0, 1]* v[1] + m[0, 2]* v[2])
            new_y = int(m[1, 0]* v[0] + m[1, 1]* v[1] + m[1, 2]* v[2])

            if 0 <= new_x < l*2 and 0 <= new_y < c*2:
                new_img.putpixel((new_x, new_y), pxl)

    return new_img

def escala(img, sx, sy):
    l, c = img.size
    new_img = Image.new("L", (l*2, c*2))

    for x in range(l*2):
        for y in range(c*2):
            new_img.putpixel((x, y), (255))

    m = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])

    for x in range(l):
        for y in range(c):
            pxl = img.getpixel((x, y))
            v = [x, y, 1]

            new_x = int(m[0, 0]* v[0] + m[0, 1]* v[1] + m[0, 2]* v[2])
            new_y = int(m[1, 0]* v[0] + m[1, 1]* v[1] + m[1, 2]* v[2])

            if 0 <= new_x < l*2 and 0 <= new_y < c*2:
                new_img.putpixel((new_x, new_y), pxl)

    return new_img

def rotacao(img, ang, tx, ty):
    l, c = img.size
    new_img = Image.new("L", (l*2, c*2))

    linha, coluna = new_img.size
    ang = math.radians(ang)

    m = np.array([[math.cos(ang), -math.sin(ang), 0 + tx],
                  [math.sin(ang), math.cos(ang), 0 + ty],
                  [0, 0, 1]])

    for x in range(l):
        for y in range(c):
            pxl = img.getpixel((x, y))
            v = [x, y, 1]

            new_x = int(m[0, 0]* v[0] + m[0, 1]* v[1] + m[0, 2]* v[2])
            new_y = int(m[1, 0]* v[0] + m[1, 1]* v[1] + m[1, 2]* v[2])

            if 0 <= new_x < l*2 and 0 <= new_y < c*2:
                new_img.putpixel((new_x, new_y), pxl)

    return new_img

def espelhamento(img, op):
    l, c = img.size
    new_img = Image.new("L", (l, c))

    if op == 1:
        m = np.array([[-1, 0, 0],
                      [ 0, 1, 0],
                      [ 0, 0, 1]])
    if op == 2:
        m = np.array([[1,  0, 0],
                      [0, -1, 0],
                      [0,  0, 1]])
    for x in range(l):
        for y in range(c):
            pxl = img.getpixel((x, y))
            v = [x, y, 1]

            new_x = int(m[0, 0]* v[0] + m[0, 1]* v[1] + m[0, 2]* v[2])
            new_y = int(m[1, 0]* v[0] + m[1, 1]* v[1] + m[1, 2]* v[2])

            new_img.putpixel((new_x, new_y), pxl)
    return new_img

img = Image.open('image/gray.jpg')

print("Escolha um: ")
print('1 - Translação')
print('2 - Escala')
print('3 - Rotação')
print('4 - Espelhamento')
a = int(input("Digite aqui: "))

if a == 1:
    img_ori = translacao(img, 0, 0)
    tx = int(input('Tx: '))
    ty = int(input('Ty: '))
    img_trans = translacao(img, tx, ty)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(img_ori, cmap='gray')
    ax[1].imshow(img_trans, cmap='gray')

    img_ori.save('image/antes_trans.jpg')
    img_trans.save('image/depois_trans.jpg')

    plt.show()
if a == 2:
    img_ori = escala(img, 1, 1)
    sx = float(input('Sx: '))
    sy = float(input('Sy: '))
    img_esc = escala(img, sx, sy)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(img_ori, cmap='gray')
    ax[1].imshow(img_esc, cmap='gray')
    plt.show()

    img_ori.save('image/antes_esc.jpg')
    img_esc.save('image/depois_esc.jpg')

if a == 3:
    img_ori = rotacao(img, 0, 0, 0)
    ang = float(input('Angulo: '))
    tx = float(input('Tx: '))
    ty = float(input('Ty: '))
    img_rot = rotacao(img, ang, tx, ty)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(img_ori, cmap='gray')

    ax[1].imshow(img_rot, cmap='gray')
    plt.show()

    img_ori.save('image/antes_rot.jpg')
    img_rot.save('image/depois_rot.jpg')

if a == 4:
    print('1 - Espelhamento Vertical')
    print('2 - Espelhamento Hoizontal')
    b = int(input('Digite aqui: '))

    img_esp = espelhamento(img, b)
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(img, cmap='gray')
    ax[1].imshow(img_esp, cmap='gray')
    plt.show()
    if b == 1:
        img_esp.save('image/espelhamento_vet.jpg')
    if b == 2:
        img_esp.save('image/espelhamento_hor.jpg')