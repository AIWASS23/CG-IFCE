import matplotlib as mpl
import matplotlib.pyplot as plt
from math import floor
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

n=4 #coeficiente de resolução
resolucao = 20*n
X1 = 10*n
Y1 = 3*n
X2 = 12*n
Y2 = 7*n
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

  #linha topo
  #(x1,y1) = (4,12)
  #(x2,y2) = (10,12)
  list3=[16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5]
  list4=[48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5, 48.5]
  plt.plot(list3,list4,'bs')
  plt.fill_between(list3,list4,color='yellow')

  #linha de baixo
  #(x1,y1) = (4,3)
  #(x2,y2) = (10,3)
  list1=[16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5]
  list2= [12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5]
  plt.plot(list1,list2,'bs')
  plt.fill_between(list1,list2,color='white')

  #lado esquerdo
  #(x1,y1) = (2,7)
  #(x1,y1) = (4,12)
  list7=[8.5, 8.5, 8.5, 9.5, 9.5, 10.5, 10.5, 10.5, 11.5, 11.5, 12.5, 12.5, 12.5, 13.5, 13.5, 14.5, 14.5, 14.5, 15.5, 15.5, 16.5]
  list8= [28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5]
  plt.plot(list7,list8,'bs')
  plt.fill_between(list7,list8,color='yellow')

  #lado esquerdo
  #(x1,y1) = (4,3)
  #(x1,y1) = (2,7)
  list5= [16.5, 15.5, 15.5, 14.5, 14.5, 13.5, 13.5, 12.5, 12.5, 11.5, 11.5, 10.5, 10.5, 9.5, 9.5, 8.5, 8.5]
  list6= [12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5]
  plt.plot(list5,list6,'bs')
  plt.fill_between(list5,list6,color='white')
  
  #lado direito
  #(x1,y1) = (12,7)
  #(x2,y2) = (10,12)
  list11=[48.5, 47.5, 47.5, 46.5, 46.5, 46.5, 45.5, 45.5, 44.5, 44.5, 44.5, 43.5, 43.5, 42.5, 42.5, 42.5, 41.5, 41.5, 40.5, 40.5, 40.5]
  list12=[28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5]
  plt.plot(list11,list12,'bs')
  plt.fill_between(list11,list12,color='yellow')

  #lado direito
  #(x1,y1) = (10,3)
  #(x1,y1) = (12,7)
  list9= [40.5, 40.5, 41.5, 41.5, 42.5, 42.5, 43.5, 43.5, 44.5, 44.5, 45.5, 45.5, 46.5, 46.5, 47.5, 47.5, 48.5]
  list10= [12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5]
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
