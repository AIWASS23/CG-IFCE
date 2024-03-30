import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(P1, P2, T1, T2, num_points=100):
    t = np.linspace(0, 1, num_points)
    H = np.array([[2, -2, 1, 1],
                  [-3, 3, -2, -1],
                  [0, 0, 1, 0],
                  [1, 0, 0, 0]])
    
    points = np.array([P1, P2, T1, T2])
    curve = np.dot(np.dot(np.array([t**3, t**2, t, np.ones_like(t)]).T, H), points)
    
    return curve

# Função para rasterizar a curva de Hermite
def rasterize_curve(curve):
    rasterized_curve = []
    for i in range(len(curve) - 1):
        x0, y0 = curve[i]
        x1, y1 = curve[i + 1]
        
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        
        if dx >= dy:
            steps = dx
        else:
            steps = dy
        
        x_increment = (x1 - x0) / steps
        y_increment = (y1 - y0) / steps
        
        for j in range(int(steps)):
            rasterized_curve.append((round(x0), round(y0)))
            x0 += x_increment
            y0 += y_increment
    
    return rasterized_curve

# Definição dos pontos de controle e vetores de tangentes
P1 = np.array([-0.5, -0.5])
P2 = np.array([0.5, 0.5])
T1 = np.array([1, 0])
T2 = np.array([0, 1])

# Gerar curvas de Hermite com diferentes configurações
curve1 = hermite_curve(P1, P2, T1, T2)
curve2 = hermite_curve(P1, P2, T1, T2, num_points=50)
curve3 = hermite_curve(P1, P2, T1, T2, num_points=200)

# Rasterizar as curvas
rasterized_curve1 = rasterize_curve(curve1)
rasterized_curve2 = rasterize_curve(curve2)
rasterized_curve3 = rasterize_curve(curve3)

# Plotar as curvas rasterizadas
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(*zip(*rasterized_curve1), color='blue')
plt.title('Curva de Hermite - 100 pontos')

plt.subplot(1, 3, 2)
plt.plot(*zip(*rasterized_curve2), color='red')
plt.title('Curva de Hermite - 50 pontos')

plt.subplot(1, 3, 3)
plt.plot(*zip(*rasterized_curve3), color='green')
plt.title('Curva de Hermite - 200 pontos')

plt.tight_layout()
plt.show()
