import matplotlib as mpl
import matplotlib.pyplot as plt
from math import floor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

n=3 #coeficiente de resolução
resolucao = 20*n
X1 = 0*n
Y1 = 0*n
X2 = 0*n
Y2 = 0*n
X = X1
Y = Y1
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
  fig = plt.figure(figsize=(10, 10))
  plt.plot(listxp,listyp,'bs')
  plt.fill_between(listxp,listyp,color='blue')
  
  ####################
  #(x1,y1) = (0,0)
  #(x2,y2) = (7,14)
  list1= [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.5]
  list2= [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5]
  plt.plot(list1,list2,'bs')
  plt.fill_between(list1,list2,color='blue')

  #(x1,y1) = (0,0)
  #(x2,y2) = (14,0)
  list3=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5]
  list4= [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
  plt.plot(list3,list4,'bs')
  plt.fill_between(list3,list4,color='blue')
  

  #(x1,y1) = (14,0)
  #(x1,y1) = (7,14)
  list5= [14.5, 14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 10.5, 10.0, 9.5, 9.0, 8.5, 8.0, 7.5]
  list6= [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5]
  plt.plot(list5,list6,'bs')
  plt.fill_between(list5,list6,color='blue')
  

  #####################
  
  plt.ylabel('Eixo Y')
  plt.xlabel('Eixo X')
  plt.grid(True)
  plt.xticks(range(0, resolucao+1,1))
  plt.yticks(range(0, resolucao+1,1))
  plt.show()
  plt.title(' n={} e Res={}x{}'.format(n,resolucao,resolucao))
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
