import math
import array

def mapP5 (valor, a, b, c, d):
    return (valor-a)/(b-a)*(d-c)+c

def esfera(raio=1, m=50, n=50):
    vertex=array.array('f')
    for i in range(m):
        #mapP5(i, 0, m, -math.pi/2, math.pi/2)
        theta = i/m*math.pi-math.pi/2 # de menos pi/2 quando i=0 a pi/2 quando i=m
        for j in range(n):
            #mapP5(j, 0, n, 0, 2*math.pi)
            phi = j*2*math.pi/n # de 0 quando j=0 a 2 pi quando j=n
            Qx = raio*math.cos(theta)*math.cos(phi)
            Qy = raio*math.sin(theta)
            Qz = raio*math.cos(theta)*math.sin(phi)
            vertex.append(Qx)
            vertex.append(Qy)
            vertex.append(Qz)
    return vertex  