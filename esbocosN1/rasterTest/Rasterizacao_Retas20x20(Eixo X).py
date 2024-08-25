import matplotlib as mpl
import matplotlib.pyplot as plt
from math import floor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#inicicialização do algoritimo 

n=1 #coeficiente de resolução
resolucao = 20*n
X1 = 0*n
Y1 = 5*n
X2 = 20*n
Y2 = 5*n
X = X1
Y = Y1

#calculando a variação de detaltaX e deltaY
if(X2-X1!=0):
  deltaX= (X2-X1)
else:
  deltaX=0

if(Y2-Y1!=0):
  deltaY= (Y2-Y1)
else:
  deltaY=0


if deltaX==0:
  M=0
else:
  M = deltaY/deltaX
B= Y-M*X
listxp = []
listyp=[]

def porduz_fragmento(x,y):
  xm = floor(x)
  ym = floor(y)
  listxp.append(xm +0.5)
  listyp.append(ym +0.5)

def plot():
  fig = plt.figure(figsize=(10, 7))
  plt.plot(listxp,listyp,'bs')
  

  plt.ylabel('Eixo Y')
  plt.xlabel('Eixo X')
  plt.grid(True)
  plt.xticks(range(0, resolucao+1,1))
  plt.yticks(range(0, resolucao+1,1))
  plt.show()
  plt.title('ΔX={}, ΔY={}, n={} e Res={}x{}'.format(deltaX,deltaY,n,resolucao,resolucao))
  fig.savefig('graph.png')
  print(listxp)
  print(listyp)


porduz_fragmento(X,Y)
if(abs(deltaX)>abs(deltaY)):
  while(X < X2):
    X=X+1
    Y=M*X + B
    porduz_fragmento(X,Y)
else:
  while(Y < Y2):
    Y=Y+1
    if M==0:
      X=X2
    else:
      X=(Y-B)/M
    porduz_fragmento(X,Y)
plot()
