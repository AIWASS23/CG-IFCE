#Grupo: Diogo Conde Soler Teixeira dos Santos
import math
import array

def mapP5 (valor, a, b, c, d):
    return (valor-a)/(b-a)*(d-c)+c

def rosquinha(raio=1, m=50, n=50, dx=3):
    vertex=array.array('f')
    for i in range(m):
        theta = mapP5(i, 0, m, 0, 2*math.pi) # de menos pi/2 quando i=0 a pi/2 quando i=m
        for j in range(n):
            phi = mapP5(j, 0, n, 0, 2*math.pi) #phi = j*2*math.pi/n # de 0 quando j=0 a 2 pi quando j=n 
            Qy = raio*math.sin(theta)
            raio2 = dx+raio*math.cos(theta)
            Qx = raio2*math.cos(phi)
            Qz = raio2*math.sin(phi)
            vertex.append(Qx)
            vertex.append(Qy)
            vertex.append(Qz)
    return vertex