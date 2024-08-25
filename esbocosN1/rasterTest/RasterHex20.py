import matplotlib.pyplot
from math import floor

coeficiente = 1 #coeficiente de resolução
resolucao = 20 * coeficiente
X1 = 0 * coeficiente
Y1 = 0 * coeficiente
X2 = 0 * coeficiente
Y2 = 0 * coeficiente
X = X1
Y = Y1

if(X2 - X1 != 0):
    deltaX = (X2 - X1)
else:
    deltaX = 0


if(Y2 - Y1 != 0):
    deltaY= (Y2-Y1)
else:
    deltaY=0


if deltaX == 0:
    M=0
else:
    M = deltaY/deltaX

B = Y - M*X
listxp = []
listyp = []

def porduzirFragmento(x,y):
    xm = floor(x)
    ym = floor(y)
    listxp.append(xm + 0.5)
    listyp.append(ym + 0.5)

def plot():
  fig = matplotlib.pyplot.figure(figsize=(7, 7))
  matplotlib.pyplot.plot(listxp,listyp,'bs')
  matplotlib.pyplot.fill_between(listxp,listyp,color='white')
  
  list3=[4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
  list4=[12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5]
  matplotlib.pyplot.plot(list3,list4,'bs')
  matplotlib.pyplot.fill_between(list3,list4,color='yellow')

 
  list1=[4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
  list2= [3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5]
  matplotlib.pyplot.plot(list1,list2,'bs')
  matplotlib.pyplot.fill_between(list1,list2,color='white')
  


  #coluna direita 1
  #(x1,y1) = (2,7)
  #(x1,y1) = (4,12)
  list7=[1.5, 2.5, 2.5, 3.5, 3.5, 4.5]
  list8= [8.5, 9.5, 10.5, 10.5, 11.5, 12.5]
  matplotlib.pyplot.plot(list7,list8,'bs')
  matplotlib.pyplot.fill_between(list7,list8,color='yellow')
  
  #coluna direita 2
  #(x1,y1) = (4,3)
  #(x1,y1) = (2,7)
  list5= [4.5, 3.5, 3.5, 2.5, 2.5, 1.5]
  list6= [3.5, 4.5, 5.5, 5.5, 6.5, 7.5]
  matplotlib.pyplot.plot(list5,list6,'bs')
  matplotlib.pyplot.fill_between(list5,list6,color='white')



  #coluna esquerda 1
  #(x1,y1) = (11,7)
  #(x1,y1) = (12,11)
  list11= [10.5, 11.5, 11.5, 12.5, 12.5, 13.5]
  list12= [12.5, 11.5, 10.5, 10.5, 9.5, 8.5]
  matplotlib.pyplot.plot(list11,list12,'bs')
  matplotlib.pyplot.fill_between(list11,list12,color='yellow')
  
  #coluna esquerda 2
  #(x1,y1) = (10,3)
  #(x1,y1) = (12,7)
  list9= [10.5, 11.5, 11.5, 12.5, 12.5, 13.5]
  list10= [3.5, 4.5, 5.5, 5.5, 6.5, 7.5]
  matplotlib.pyplot.plot(list9,list10,'bs')
  matplotlib.pyplot.fill_between(list9,list10,color='white')
  
      

  #####################
  
  matplotlib.pyplot.ylabel('Eixo Y')
  matplotlib.pyplot.xlabel('Eixo X')
  matplotlib.pyplot.grid(True)
  matplotlib.pyplot.xticks(range(0, resolucao+1,1))
  matplotlib.pyplot.yticks(range(0, resolucao+1,1))
  matplotlib.pyplot.show()
  matplotlib.pyplot.title(' n={} e Res={}x{}'.format(coeficiente,resolucao,resolucao))
  fig.savefig('graph.png')
  print(listxp)
  print(listyp)


porduzirFragmento(X,Y)
if(abs(deltaX)>abs(deltaY)):
  while(X < X2):
    X=X+1
    Y=M*X + B
    porduzirFragmento(X,Y)
else:
  while(Y < Y2):
    Y=Y+1
    if M==0:
      X=X2
    else:
      X=(Y-B)/M
    porduzirFragmento(X,Y)
plot()
