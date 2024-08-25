# Responsável pelo sistema de matrizes
import numpy as np
# Responsável por transformar as matrizes em imagens
from PIL import Image
# Responsável por limpar a tela
import os


# C L A S S E S

# Classe referente ao segmento de reta
class segreta:
  # Coordenada do ponto inicial
  Xi = 0
  Yi = 0
  # Coordenada do ponto final
  Xf = 0
  Yf = 0
  # Id da reta é sua cor em RGB
  id = [3]

  def __init__(self, Xi, Yi, Xf, Yf, id):
    self.Xi = Xi
    self.Yi = Yi   
    self.Xf = Xf
    self.Yf = Yf
    self.id = id

  def desenhaSegreta(self, matriz):
    # Determina as dimensões da matriz
    matriz_altura = matriz.shape[0]-1
    matriz_largura = matriz.shape[1]-1

    # Verifica a reta para escolher o método de varredura correto
    if( (self.Xi != self.Xf) and (self.Yi != self.Yf) ):
      coef_ang = (self.Yf - self.Yi)/(self.Xf - self.Xi)

      if( abs(coef_ang) < 1):
        # Percorre a matriz de cima pra baixo varrendo linha por linha
        matriz = desenhaYM(matriz, self, coef_ang, matriz_altura, matriz_largura)

      if( abs(coef_ang) >= 1 ):
        # Percorre a matriz da esquerda pra direita varrendo coluna por coluna
        matriz = desenhaXM(matriz, self, coef_ang, matriz_altura, matriz_largura)

    else:

      if(self.Xi == self.Xf):
        # Desenha uma linha vertical
        matriz = desenhaY(matriz, self, matriz_altura, matriz_largura)
      
      if(self.Yi == self.Yf):
        # Desenha uma linha horizontal
        matriz = desenhaX(matriz, self, matriz_altura, matriz_largura)

    return matriz


# F U N Ç Õ E S    

# Função para limpar a tela
def cls():
  os.system('cls' if os.name=='nt' else 'clear')



# Função para definir resolução da imagem
# e criar uma matriz preenchida com 0
# que respresentará o conteúdo da imagem
def definir_matriz(resY, resX):
  matriz = np.zeros((resY, resX, 3), dtype=np.uint8)
  return matriz



# Desenha segmentos de reta onde coeficiente angular é <= 1
# Desenha por linhas
def desenhaXM(matriz, segreta, coef_ang, matriz_altura, matriz_largura):
  a = segreta.Yi
  b = segreta.Yf
  # Inverte as extremidades se a coordenada
  # final for menor que a inicial para
  # evitar problemas no loop
  if(a > b):
    a, b = b, a
  for i in range( round(a * matriz_altura) , round(b * matriz_altura) ):
    matriz[i][ round( (i-segreta.Yi*matriz_altura)/coef_ang + segreta.Xi*matriz_largura) ] = segreta.id
  return matriz



# Desenha segmentos de reta onde coeficiente angular é > 1
# Desenha por colunas
def desenhaYM(matriz, segreta, coef_ang, matriz_altura, matriz_largura):
  a = segreta.Xi
  b = segreta.Xf
  # Inverte as extremidades se a coordenada
  # final for menor que a inicial para
  # evitar problemas no loop
  if(a > b):
    a, b = b, a
  for j in range( round(a * matriz_largura) , round(b * matriz_largura)):
    matriz[ round((j - segreta.Xi*matriz_largura)*coef_ang + segreta.Yi*matriz_altura) ][j] = segreta.id
  return matriz



# Desenha segmentos de reta verticais
def desenhaY(matriz, segreta, matriz_altura, matriz_largura):
  a = segreta.Yi
  b = segreta.Yf
  # Inverte as extremidades se a coordenada
  # final for menor que a inicial para
  # evitar problemas no loop
  if(a > b):
    a, b = b, a
  for i in range( round(a * matriz_altura) , round(b * matriz_altura) ):
    matriz[i][round(segreta.Xi * matriz_largura)] = segreta.id
  return matriz



# Desenha segmentos de reta horizontais
def desenhaX(matriz, segreta, matriz_altura, matriz_largura):
  a = segreta.Xi
  b = segreta.Xf
  # Inverte as extremidades se a coordenada
  # final for menor que a inicial para
  # evitar problemas no loop
  if(a > b):
    a, b = b, a
  for j in range( round(a * matriz_largura) , round(b * matriz_largura) ):
    matriz[round(segreta.Yi * matriz_altura)][j] = segreta.id
  return matriz



# Função principal
if __name__ == '__main__':
  
  # Lista de objetos da classe segreta com suas respectivas cores em RGB, vermelho, verde e azul
  seg_retas = [segreta(float(input("Primeira Reta\nXi: ")),float(input("Yi: ")),float(input("\nXf: ")),float(input("Yf: ")),[255,0,0]), segreta(float(input("\n\nSegunda Reta\nXi: ")),float(input("Yi: ")),float(input("\nXf: ")),float(input("Yf: ")),[0,255,0]),segreta(float(input("\n\nTerceira Reta\nXi: ")),float(input("Yi: ")),float(input("\nXf: ")),float(input("Yf: ")),[0,0,255])]

  # Define as matrizes e suas resoluções, no caso três
  matriz1 = definir_matriz(10,10)
  matriz2 = definir_matriz(500,500)
  matriz3 = definir_matriz(1000,1000)

  # Desenha as 3 retas nas 3 matrizes (10x10, 500x500, 1000x1000)
  for i in range(3):
    matriz1 = seg_retas[i].desenhaSegreta( matriz1 )
    matriz2 = seg_retas[i].desenhaSegreta( matriz2 )
    matriz3 = seg_retas[i].desenhaSegreta( matriz3 )

  # Tranforma as matrizes em imagem do tipo .png
  img = Image.fromarray( (  matriz1  ) [::-1], 'RGB')
  img.save('matriz1.png')
  img = Image.fromarray( (  matriz2  ) [::-1], 'RGB')
  img.save('matriz2.png')
  img = Image.fromarray( (  matriz3  ) [::-1], 'RGB')
  img.save('matriz3.png')
  
  # Loop para teste de algoritmo
  #while(True):
  #  segreta1 = segreta(float(input("Xi: ")),float(input("Yi: ")),float(input("Xf: ")),float(input("Yf: ")),[255,255,255])
  #  img = Image.fromarray( (  segreta1.desenhaSegreta( definir_matriz(1000,1000) )  ) [::-1], 'RGB')
  #  del segreta1
  #  img.save('matriz1.png')
  #  img.show()
  #  cls()
  
