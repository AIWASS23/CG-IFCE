from tkinter.constants import X
import matplotlib.pyplot as plt
import numpy as np
import math


def trans(xi,yi,tx,ty):
    # xi[] - vetor ccom cordenadas x de entrada / yi [] - coordenadas y de entrada / tx - translação no eixo x / ty - translação no eixo y
    
    pontox = []
    pontoy = []

    for c in range(0,len(xi)):
        pontox.append(xi[c] + tx)
        pontoy.append(yi[c] + ty)

     #plotar inicial
    plt.title("Antes da translação")
    plt.plot(xi, yi,'bs')
    plt.xticks(np.arange(min(xi), max(pontox)+1))
    plt.yticks(np.arange(min(yi), max(pontoy)+1))
    plt.show()

    #plotarfinal
    plt.title("Imagem com translação")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(xi), max(pontox)+1))
    plt.yticks(np.arange(min(yi), max(pontoy)+1))
    plt.show()

    return pontox,pontoy #retorna vetores x, y com translação

def transinv(xi,yi,tx,ty):
    
    # xi[]- vetor com coordenadas x de entrada / yi[] - vetor com coordenadas y de entrada / tx - translação no eixo x / ty - translação no eixo y
    
    pontox = []
    pontoy = []

    for c in range(0,len(xi)):
        pontox.append(xi[c] - tx)
        pontoy.append(yi[c] - ty)

    return pontox,pontoy #retorna vetores com transformada inversa dos pontos x e y

def escala(xi,yi,sx,sy):
    #xi[] - vetor de entrada pontos x
    #yi[] - vetor de entrada ponto y
    #sx - escala aplicada em x
    #sy - escala aplicada em y

    #translação inversa em relação ao primeiro ponto
    tx = xi[0] #valor da translação em x
    ty = yi[0] #valor da translação em y
    xin,yin = transinv(xi,yi,tx,ty) #realiza a translação inversa em todos os pontos
    
    #escala
    escx = []
    escy = []

    for c in range(0,len(xin)):
        escx.append(xin[c] * sx)
        escy.append(yin[c] * sy)

    

    #translação
    xfin, yfin = trans(escx,escy,tx,ty)
   
        
    #plotar inicial
    plt.title("Imagem sem escala")
    plt.plot(xi, yi,'bs')
    plt.xticks(np.arange(min(xi), max(xfin)+1))
    plt.yticks(np.arange(min(yi), max(yfin)+1))
    plt.show()

    #plotarfinal
    plt.title("Imagem com escala aplicada")
    plt.plot(xfin, yfin,'bs')
    plt.xticks(np.arange(min(xi), max(xfin)+1))
    plt.yticks(np.arange(min(yi), max(yfin)+1))
    plt.show()

    return xfin,yfin

def rotacao(xi,yi,ang):
    
    # xi[]- vetor com coordenadas x de entrada / yi[] - vetor com coordenadas y de entrada / ang - angulo de rotação
    
    pontox = []
    pontoy = []

    for c in range(0,len(xi)):
        pontox.append((xi[c]* math.cos(math.radians(ang))) + (yi[c] * - math.sin(math.radians(ang))))
        pontoy.append((xi[c] * math.sin(math.radians(ang))) + (yi[c] *  math.cos(math.radians(ang))))

    #plotarfinal
    plt.title("Rotacao")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()


    return pontox,pontoy #retorna vetores com a rotacao dos pontos x e y

def reflexaox(xi,yi):
     # xi[] - vetor ccom cordenadas x de entrada / yi [] - coordenadas y de entrada /
    
    pontox = []
    pontoy = []

    for c in range(0,len(xi)):
        pontox.append(xi[c] * -1)
        pontoy.append(yi[c])

    
    #plotar inicial
    plt.title("Original")
    plt.plot(xi, yi,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    #plotarfinal
    plt.title("Reflexão eixo x")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    return pontox,pontoy #retorna vetores x, y com reflexão

def reflexaoy(xi,yi):
     # xi[] - vetor ccom cordenadas x de entrada / yi [] - coordenadas y de entrada /
    
    pontox = []
    pontoy = []

    for c in range(0,len(xi)):
        pontox.append(xi[c])
        pontoy.append(yi[c] * -1)

    
    #plotar inicial
    plt.title("Original")
    plt.plot(xi, yi,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    #plotarfinal
    plt.title("Reflexão eixo x")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    return pontox,pontoy #retorna vetores x, y com reflexão

def reflexaoxy(xi,yi):
     # xi[] - vetor ccom cordenadas x de entrada / yi [] - coordenadas y de entrada /
    
    pontox = []
    pontoy = []

    for c in range(0,len(xi)):
        pontox.append(xi[c] * -1)
        pontoy.append(yi[c] * -1)

    
    #plotar inicial
    plt.title("Original")
    plt.plot(xi, yi,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    #plotarfinal
    plt.title("Reflexão eixo x")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    return pontox,pontoy #retorna vetores x, y com reflexão

def dda(x1,y1,x2,y2):
  
    #inicio
    dx = x2 - x1
    dy = y2 - y1

    if(abs(dx)>abs(dy)):
        passos = abs(dx)
    else:
        passos = abs(dy)
  
    
    xinc = dx/passos
    yinc = dy/passos
    x = x1
    y = y1

    pontox = [x]
    pontoy = [y]

    for c in range(1,passos):
        x = x + xinc
        y = y + yinc
        pontox.append(x)
        pontoy.append(y)

    #plotarfinal
    plt.title("DDA")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()

    return pontox,pontoy

def bressreta(x1,y1,x2,y2):
    
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    p = 2*dy-dx
    
    const1 = 2*dy
    const2 = 2*(dy-dx)
    x = x1
    y = y1

    pontox = [x]
    pontoy = [y]
  
    while(x<x2):
        x = x + 1
        print("valor de x",x)
        if(p<0):
            p = p + const1
        else:
            p = p+const2
            y = y+1
        pontox.append(x)
        pontoy.append(y)
    

    #plotarfinal
    plt.title("Bresseham")
    plt.plot(pontox, pontoy,'bs')
    plt.xticks(np.arange(min(pontox), max(pontox)+1))
    plt.yticks(np.arange(min(pontoy), max(pontoy)+1))
    plt.show()
    return pontox,pontoy

def bresscirc(xc,yc,r):
    def plotcirc(x,y):
        xp = []
        yp = []
        xp.append(xc+x)
        yp.append(yc+y)
        xp.append(xc-x)
        yp.append(yc+y)
        xp.append(xc+x)
        yp.append(yc-y)
        xp.append(xc-x)
        yp.append(yc-y)
        xp.append(xc+y)
        yp.append(yc+x)
        xp.append(xc-y)
        yp.append(yc+x)
        xp.append(xc+y)
        yp.append(yc-x)
        xp.append(xc-y)
        yp.append(yc-x)

        return xp,yp

    x = 0
    y=r
    p=3-2*r
    xpontos = []
    ypontos = []
    xp,yp = plotcirc(x,y)
    xpontos = xpontos + xp
    ypontos = ypontos + yp

    while(x<y):
        if(p<0):
            p = p + 4*x + 6
        else:
            p = p + 4*(x-y)+10
            y = y-1
        x = x+1
        xp,yp = plotcirc(x,y)
        xpontos = xpontos + xp
        ypontos = ypontos + yp

    #plotarfinal
    plt.title("Circuferencia")
    plt.plot(xpontos, ypontos,'bs')
    plt.xticks(np.arange(min(xpontos), max(ypontos)+1))
    plt.yticks(np.arange(min(xpontos), max(ypontos)+1))
    plt.show()
    return xpontos,ypontos

def cohensutherland(x1,y1,x2,y2,xmin,ymin,xmax,ymax):
    def region_code(x,y):
        codigo = 0
        if(x<xmin):
            codigo = codigo + 1;
        if(x>xmax):
             codigo = codigo + 2;
        if(y<ymin):
             codigo = codigo + 4;
        if(y>ymax):
             codigo = codigo + 8;

        return codigo

    aceite=False
    feito=False
    cfora = -1
    xint = -1
    yint = -1

    while(feito==False):
        c1=region_code(x1,y1)
        c2=region_code(x2,y2)
        print(c1)
        print(c2)
        
        if(c1==0 and c2==0):
            aceite=True
            feito=True
        elif(c1 != 0 and c2 != 0):
            feito=True
        else:
            if(c1!=0):
                cfora=c1
            else:
                cfora=c2
    
            if(cfora==1 or cfora==3 or cfora==5 or cfora==7 or cfora==9 or cfora==11 or cfora==13 or cfora==15):
                xint=xmin
                yint=y1+(y2-y1)*(xmin-x1)/(x2-x1)
            elif(cfora==2 or cfora ==3 or cfora==6 or cfora ==7 or cfora ==10 or cfora==11 or cfora==14 or cfora==15):
                xint = xmax
                yint = y1+(y2-y1)*(xmax-x1)/(x2-x1)
            elif(cfora == 4 or cfora==5 or cfora==6 or cfora==7 or cfora==12 or cfora==13 or cfora==14 or cfora==15):
                yint=ymin
                xint=x1+(x2-x1)*(ymin-y1)/(y2-y1)
            elif(cfora==8 or cfora==9 or cfora==10 or cfora ==11 or cfora==12 or cfora==13 or cfora==14 or cfora==15):
                yint=ymax
                xint=x1+(x2-x1)*(ymax-y1)/(y2-y1)
            if(c1==cfora):
                x1 = xint
                y1 = yint
            else:
                x2=xint
                y2=yint
    
    print(x1,y1,x2,y2)
    print(aceite)
    if(aceite==True):
        bressreta(x1,y1,x2,y2)
        
    return x1,y1,x2,y2

def liangbarski(x1,y1,x2,y2,xjmin,yjmin,xjmax,yjmax):
    def clipset(p,q,u1,u2):
        result = True
        if(p<0.0):
            r=q/p
            if(r>u2):
                result = False
            elif(r>u1):
                u1=r
        elif(p>0.0):
            r=q/p
            if(r<u1):
                result=False
            elif(r<u2):
                u2=r
        elif(q<0.0):
            result=False
        
        return result
    
    u1=0.0
    u2=1.0
    dx=x2-x1
    dy=y2-y1
    if(clipset(-dx,x1-xjmin,u1,u2)):
        if(clipset(dx,xjmax-x1,u1,u2)):
            if(clipset(-dy,y1-yjmin,u1,u2)):
                if(clipset(dy,yjmax-y1,u1,u2)):
                    if(u2<1.0):
                        x2=x1+u2*dx
                        y2=y1+u2*dy
                    if(u1>0.0):
                        x1=x1+u1*dx
                        y1=y1+u1*dy
                    bressreta(x1,y1,x2,y2)
                


def default():
    print("Value default")

def sair():
    exit()

#chamadas de funções usuario
def chamatranslacao():
    sair = False
    x = []
    y = []

    while(sair!=True):
        xi = int(input('Digite a coordenada do eixo x: '))
        yi = int(input('Digite a coordenada do eixo y: '))
        x.append(xi)
        y.append(yi)
        teste = int(input("Deseja adicionar um novo ponto? 1 - SIM / 2 = NÃO"))
        if(teste==2):
            sair=True
        print(x,y)       
    tx= int(input("Qual os valor de translação no eixo x: "))
    ty= int(input("Qual os valor de translação no eixo ty: "))

    trans(x,y,tx,ty)

def chamaescala():
    sair = False
    x = []
    y = []

    while(sair!=True):
        xi = int(input('Digite a coordenada do eixo x: '))
        yi = int(input('Digite a coordenada do eixo y: '))
        x.append(xi)
        y.append(yi)
        teste = int(input("Deseja adicionar um novo ponto? 1 - SIM / 2 = NÃO"))
        if(teste==2):
            sair=True
        print(x,y)       
    sx= int(input("Qual os valor de escala no eixo x: "))
    sy= int(input("Qual os valor de escala no eixo ty: "))

    escala(x,y,sx,sy)

def chamarotacao():
    sair = False
    x = []
    y = []

    while(sair!=True):
        xi = int(input('Digite a coordenada do eixo x: '))
        yi = int(input('Digite a coordenada do eixo y: '))
        x.append(xi)
        y.append(yi)
        teste = int(input("Deseja adicionar um novo ponto? 1 - SIM / 2 = NÃO"))
        if(teste==2):
            sair=True
        print(x,y)       
    ang= int(input("Qual o angulo de rotação: "))

    rotacao(x,y,ang)

def chamareflexaox():
    sair = False
    x = []
    y = []

    while(sair!=True):
        xi = int(input('Digite a coordenada do eixo x: '))
        yi = int(input('Digite a coordenada do eixo y: '))
        x.append(xi)
        y.append(yi)
        teste = int(input("Deseja adicionar um novo ponto? 1 - SIM / 2 = NÃO"))
        if(teste==2):
            sair=True
        print(x,y)       
    reflexaox(x,y)

def chamareflexaoy():
    sair = False
    x = []
    y = []

    while(sair!=True):
        xi = int(input('Digite a coordenada do eixo x: '))
        yi = int(input('Digite a coordenada do eixo y: '))
        x.append(xi)
        y.append(yi)
        teste = int(input("Deseja adicionar um novo ponto? 1 - SIM / 2 = NÃO"))
        if(teste==2):
            sair=True
        print(x,y)       
    reflexaoy(x,y) 

def chamareflexaoxy():
    sair = False
    x = []
    y = []

    while(sair!=True):
        xi = int(input('Digite a coordenada do eixo x: '))
        yi = int(input('Digite a coordenada do eixo y: '))
        x.append(xi)
        y.append(yi)
        teste = int(input("Deseja adicionar um novo ponto? 1 - SIM / 2 = NÃO"))
        if(teste==2):
            sair=True
        print(x,y)       
    reflexaoxy(x,y)

def chamadda():
    xi = int(input('Digite o x inicial '))
    yi = int(input('Digite o y inicial: '))
    xf = int(input('Digite o x final '))
    yf = int(input('Digite o y final'))   

    dda(xi,yi,xf,yf)

def chamabress():
    xi = int(input('Digite o x inicial '))
    yi = int(input('Digite o y inicial: '))
    xf = int(input('Digite o x final '))
    yf = int(input('Digite o y final'))   

    bressreta(xi,yi,xf,yf)

def chamabresscirc():
    xi = int(input('Digite o x inicial '))
    yi = int(input('Digite o y inicial: '))
    r = int(input('Digite o raio: '))

    bresscirc(xi,yi,r)

def chamacohen():
    xi = int(input('Digite o x inicial '))
    yi = int(input('Digite o y inicial: '))
    xf = int(input('Digite o x final '))
    yf = int(input('Digite o y final'))   
    xmin= int(input('Digite o x minimo da janela: '))
    ymin = int(input('Digite o y minimo da janela: '))
    xmax = int(input('Digite o x máximo da janela: '))
    ymax = int(input('Digite o y máximo da janela: '))   

    cohensutherland(xi,yi,xf,yf,xmin,ymin,xmax,ymax)

def chamaliang():
    xi = int(input('Digite o x inicial '))
    yi = int(input('Digite o y inicial: '))
    xf = int(input('Digite o x final '))
    yf = int(input('Digite o y final'))   
    xmin= int(input('Digite o x minimo da janela: '))
    ymin = int(input('Digite o y minimo da janela: '))
    xmax = int(input('Digite o x máximo da janela: '))
    ymax = int(input('Digite o y máximo da janela: '))   

    liangbarski(xi,yi,xf,yf,xmin,ymin,xmax,ymax)

#MAIN
if __name__ == "__main__":
    switch = {
        "1": chamatranslacao,
        "2": chamaescala,
        "3": chamarotacao,
        "4": chamareflexaox,
        "5": chamareflexaoy,
        "6": chamareflexaoxy,
        "7": chamadda,
        "8": chamabress,
        "9": chamabresscirc,
        "10":chamacohen,
        "11":chamaliang,
        "12": sair
    }
    opcao = 0
    while(opcao!=12):
        print("MENU")
        print("1 - Translação")
        print("2 - Escala")
        print("3 - Rotação")
        print("4 - Reflexão eixo x")
        print("5 - Reflexão eixo y")
        print("6 - Reflexão eixo xy")
        print("7 - DDA")
        print("8 - Bressenham Retas ")
        print("9 - Bressenham Circunferencia ")
        print("10 - Recorte Cohen-Sutherland ")
        print("11 - Recorte Liang-Barsky")
        print("12 - Sair")

        opcao = input("Digite um número: ")
        case = switch.get(opcao, default)
        case()
