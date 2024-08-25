import matplotlib as mpl
import matplotlib.pyplot as plt
from math import floor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

n=2 #coeficiente de resolução
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
  fig = plt.figure(figsize=(7, 7))
  plt.plot(listxp,listyp,'bs')
  plt.fill_between(listxp,listyp,color='white')
  
  
  ####################
  #(x1,y1) = (12,7)
  #(x2,y2) = (10,12)

  #linha topo
  #(x1,y1) = (4,12)
  #(x2,y2) = (10,12)
  list3=[4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
  list4=[12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5]
  plt.plot(list3,list4,'bs')
  plt.fill_between(list3,list4,color='yellow')

  #linha de baixo
  #(x1,y1) = (4,3)
  #(x2,y2) = (10,3)
  list1=[4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
  list2= [3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5]
  plt.plot(list1,list2,'bs')
  plt.fill_between(list1,list2,color='white')
  


  #coluna direita 1
  #(x1,y1) = (2,7)
  #(x1,y1) = (4,12)
  list7=[1.5, 2.5, 2.5, 3.5, 3.5, 4.5]
  list8= [8.5, 9.5, 10.5, 10.5, 11.5, 12.5]
  plt.plot(list7,list8,'bs')
  plt.fill_between(list7,list8,color='yellow')
  
  #coluna direita 2
  #(x1,y1) = (4,3)
  #(x1,y1) = (2,7)
  list5= [4.5, 3.5, 3.5, 2.5, 2.5, 1.5]
  list6= [3.5, 4.5, 5.5, 5.5, 6.5, 7.5]
  plt.plot(list5,list6,'bs')
  plt.fill_between(list5,list6,color='white')



  #coluna esquerda 1
  #(x1,y1) = (11,7)
  #(x1,y1) = (12,11)
  list11= [10.5, 11.5, 11.5, 12.5, 12.5, 13.5]
  list12= [12.5, 11.5, 10.5, 10.5, 9.5, 8.5]
  plt.plot(list11,list12,'bs')
  plt.fill_between(list11,list12,color='yellow')
  
  #coluna esquerda 2
  #(x1,y1) = (10,3)
  #(x1,y1) = (12,7)
  list9= [10.5, 11.5, 11.5, 12.5, 12.5, 13.5]
  list10= [3.5, 4.5, 5.5, 5.5, 6.5, 7.5]
  plt.plot(list9,list10,'bs')
  plt.fill_between(list9,list10,color='white')
  
      

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
