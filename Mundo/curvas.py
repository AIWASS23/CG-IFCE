import numpy as np
import matplotlib.pyplot as plt

#Gerando uma curva de Hermite
def gerar_curva_hermite(t, P0, T0, P1, T1):
    return (2*t**3 - 3*t**2 + 1)*P0 + (t**3 - 2*t**2 + t)*T0 + (-2*t**3 + 3*t**2)*P1 + (t**3 - t**2)*T1 #Equação da curva de Hermite

#Gerando uma curva de Bézier cúbica
def gerar_curva_bezier(t, P0, P1, P2, P3):
    return (1-t)**3*P0 + 3*(1-t)**2*t*P1 + 3*(1-t)*t**2*P2 + t**3*P3 #Equação da curva de Bézier

#Gerando pontos 3D aleatórios
def ponto3d_aleatorio(escala=1):
    return np.array([np.random.uniform(-escala, escala),
                     np.random.uniform(-escala, escala),
                     np.random.uniform(-escala, escala)]) #Retorna um ponto 3D aleatório

# Gerando um circuito
def gerar_circuito():
    P0 = np.array([0, 0, 0])  # Início
    #Primeira curva de Bézier
    P1 = ponto3d_aleatorio()
    P2 = ponto3d_aleatorio()
    P3 = ponto3d_aleatorio()
    bezier_1 = [gerar_curva_bezier(t, P0, P1, P2, P3) for t in np.linspace(0, 1, 50)] 
    
    #Primeira curva de Hermite
    T0 = ponto3d_aleatorio(escala=0.5)
    P4 = ponto3d_aleatorio()
    T1 = ponto3d_aleatorio(escala=0.5)
    hermite_1 = [gerar_curva_hermite(t, P3, T0, P4, T1) for t in np.linspace(0, 1, 50)]
    
    #Segunda curva de Bézier
    P5 = ponto3d_aleatorio()
    P6 = ponto3d_aleatorio()
    P7 = ponto3d_aleatorio()
    bezier_2 = [gerar_curva_bezier(t, P4, P5, P6, P7) for t in np.linspace(0, 1, 50)] 
    
    #Segunda curva de Hermite
    T2 = ponto3d_aleatorio(escala=0.5)
    P8 = np.array([0, 0, 0])  # Fim
    T3 = ponto3d_aleatorio(escala=0.5) 
    hermite_2 = [gerar_curva_hermite(t, P7, T2, P8, T3) for t in np.linspace(0, 1, 50)] 
    
    return np.vstack([bezier_1, hermite_1, bezier_2, hermite_2]) #Retorna o circuito

#Plot 3d
def circuito_plot(pontos):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') #Adiciona um subplot 3D
    ax.plot(pontos[:, 0], pontos[:, 1], pontos[:, 2], '-o', markersize=3) 
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show() 

#Gerando o circuito
circuito = gerar_circuito()
circuito_plot(circuito)