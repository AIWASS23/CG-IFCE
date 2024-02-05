#Grupo: Diogo Conde Soler Teixeira dos Santos
import math
import array

def mapP5 (valor, a, b, c, d):
    return (valor-a)/(b-a)*(d-c)+c

def parabola(raio=50, n=50):
    vertex=array.array('f')
    for i in range(raio):
        x=mapP5(i, 0, raio, 0, 2)
        for j in range(n):
            #mapP5(j, 0, n, 0, 2*math.pi)
            phi = j*2*math.pi/n # de 0 quando j=0 a 2 pi quando j=n
            Qx = x*math.cos(phi)
            Qy = x**2
            Qz = x*math.sin(phi)
            vertex.append(Qx)
            vertex.append(Qy)
            vertex.append(Qz)
    return vertex