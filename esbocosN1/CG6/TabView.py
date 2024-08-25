import tkinter as tk
import customtkinter
import Rasteriza as rt
import random

class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color="#F3F3F3", segmented_button_selected_color="#7056A6")

        tkEntryVar = tk.StringVar(value='-1,-0;1,1')
        tkEntryVarCurva = tk.StringVar(value='-0.5,-0.5;0.5,-0.5')
        tkEntryTVar = tk.StringVar(value='0,-1;1,0')
        tkEntrySegVar = tk.IntVar(value=5)
        tkEntryVarPoligono = tk.StringVar(value='1, 0;-0.5, -0.866;-0.5, 0.866')

        #Criando as Tabs
        self.add('Reta')
        self.add('Curva')
        self.add('Polígono')

        #Reta Tab
        self.rowconfigure((0,1), weight=1, uniform='a')

        self.entryReta = customtkinter.CTkEntry(master=self.tab('Reta'), textvariable=tkEntryVar, width=600, height=62, font=("Helvetica", 24))
        self.buttonReta = customtkinter.CTkButton(master=self.tab('Reta'), command=lambda: self.adicionarReta(tkEntryVar), text="Adicionar", corner_radius=24, fg_color="#7056A6",font=('Helvetica', 24), width=272, height=62)
        self.buttonRasterizarReta = customtkinter.CTkButton(master=self.tab('Reta'), command=self.rasterize,text="Rasterizar", font=("Helvetica", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.buttonApagaMatrizReta = customtkinter.CTkButton(master=self.tab('Reta'), command=self.zeraMatriz, text="Limpar", corner_radius=24, fg_color="#7056A6",font=('Helvetica', 24), width=272, height=62)
        self.textBoxReta = customtkinter.CTkTextbox(master=self.tab('Reta'), width=300,height=300, corner_radius=24, font=("Helvetica", 14))
        
        self.textBoxReta.grid(row=1, column=1)
        self.entryReta.grid(row=1, column=0, padx=20, pady=20)
        self.buttonReta.grid(row=1, column=0, padx=20, pady=20, sticky='sw')
        self.buttonRasterizarReta.grid(row=1, column=0, padx=20, pady=20, sticky='se')
        self.buttonApagaMatrizReta.grid(row=2, column=1, padx=20, pady=20, sticky='w')

        #Curva Tab
        self.segLabel = customtkinter.CTkLabel(master=self.tab('Curva'), text='Segmentos', height=10, width=50)
        self.entryCurva = customtkinter.CTkEntry(master=self.tab('Curva'), textvariable=tkEntryVarCurva, width=300, height=62, font=("Helvetica", 24))
        self.entryTan = customtkinter.CTkEntry(master=self.tab('Curva'), textvariable=tkEntryTVar, width=300, height=62, font=('Helvetica', 24))
        self.entrySeg = customtkinter.CTkEntry(master=self.tab('Curva'), textvariable=tkEntrySegVar, width=50, height=62, font=('Helvetica', 24))
        self.buttonCurva = customtkinter.CTkButton(master=self.tab('Curva'), command=lambda: self.adicionarCurva(tkEntryVarCurva, tkEntryTVar, tkEntrySegVar),text="Adicionar", corner_radius=24, fg_color="#7056A6",font=('Helvetica', 24), width=272, height=62)
        self.buttonRasterizarCurva = customtkinter.CTkButton(master=self.tab('Curva'), command=self.rasterize, text="Rasterizar", font=("Helvetica", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.buttonApagaMatrizCurva = customtkinter.CTkButton(master=self.tab('Curva'), command=self.zeraMatriz, text="Limpar", corner_radius=24, fg_color="#7056A6",font=('Helvetica', 24), width=100, height=62)
        self.textBoxCurva = customtkinter.CTkTextbox(master=self.tab('Curva'), width=200,height=300, corner_radius=24, font=("Helvetica", 12))
        
        self.textBoxCurva.grid(row=1, column=3)
        self.entryCurva.grid(row=1, column=0, padx=20, pady=20)
        self.entryTan.grid(row=1, column=1, padx=0, pady=0)
        self.segLabel.grid(row=0, column=2, padx=0, pady=0, sticky='s')
        self.entrySeg.grid(row=1, column=2, padx=20, pady=20)
        self.buttonCurva.grid(row=1, column=0, padx=20, pady=20, sticky='s')
        self.buttonRasterizarCurva.grid(row=1, column=1, padx=20, pady=20, sticky='s')
        self.buttonApagaMatrizCurva.grid(row=2, column=3, padx=20, pady=20, sticky='s')


        #Polígono Tab
        self.entryPoligono = customtkinter.CTkEntry(master=self.tab('Polígono'), textvariable=tkEntryVarPoligono, placeholder_text="ex: -1,-0;1,1", width=600, height=62, font=("Helvetica", 24))
        self.buttonPoligono = customtkinter.CTkButton(master=self.tab('Polígono'),command=lambda: self.adicionarPoligonos(tkEntryVarPoligono), text="Adicionar", corner_radius=24, fg_color="#7056A6",font=('Helvetica', 24), width=272, height=62)
        self.buttonRasterizarPoligono = customtkinter.CTkButton(master=self.tab('Polígono'),command=self.rasterize, text="Rasterizar", font=("Helvetica", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.buttonApagaMatrizPoligono = customtkinter.CTkButton(master=self.tab('Polígono'), command=self.zeraMatriz, text="Limpar", corner_radius=24, fg_color="#7056A6",font=('Helvetica', 24), width=272, height=62)
        self.textBoxPoligono = customtkinter.CTkTextbox(master=self.tab('Polígono'), width=300,height=300, corner_radius=24, font=("Helvetica", 12))
        
        self.textBoxPoligono.grid(row=1, column=1)
        self.entryPoligono.grid(row=1, column=0, padx=20, pady=20)
        self.buttonPoligono.grid(row=1, column=0, padx=20, pady=20, sticky='sw')
        self.buttonRasterizarPoligono.grid(row=1, column=0, padx=20, pady=20, sticky='se')
        self.buttonApagaMatrizPoligono.grid(row=2, column=1, padx=20, pady=20, sticky='w')

    #Inicialização da matriz
    matrizTela = rt.Tela()

    #Métodos
    def rasterize(self):
        print(rt.myMatriz.matriz)
        self.matrizTela.draw_Tela(rt.myMatriz.matriz)
        rt.mostrar()

    def zeraMatriz(self):
        rt.myMatriz.zerarMatriz()
        self.textBoxReta.delete('0.0', 'end')
        self.textBoxCurva.delete('0.0', 'end')
        self.textBoxPoligono.delete('0.0', 'end')

    def adicionarReta(self, entryData):
        points = self.transformToRetaMatrix(entryData)
        tempLine = rt.Reta(points, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.matrizTela.add_Reta(tempLine)
        self.textBoxReta.insert('0.0', f'Reta {points}\n')
        self.textBoxCurva.insert('0.0', f'Curva {points}\n')
        self.textBoxPoligono.insert('0.0', f'Polígono {points}\n')


    def adicionarCurva(self, entryData, entryTData, numSeg):
        points = self.transformToRetaMatrix(entryData)
        tangents = self.transformToRetaMatrix(entryTData)
        tempLine = rt.Curva(points, tangents,numSeg.get(), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.matrizTela.add_Curva(tempLine)
        self.textBoxReta.insert('0.0', f'Reta {points}\n')
        self.textBoxCurva.insert('0.0', f'Curva {points}\n')
        self.textBoxPoligono.insert('0.0', f'Polígono {points}\n')

    def adicionarPoligonos(self, entryData):
        points = self.transformListPoligono(entryData)
        print(points)
        tempPoligono = rt.Poligono(points, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.matrizTela.add_Poligono(tempPoligono)
        self.textBoxReta.insert('0.0', f'Reta {points}\n')
        self.textBoxCurva.insert('0.0', f'Curva {points}\n')
        self.textBoxPoligono.insert('0.0', f'Polígono {points}\n')

    def transformToRetaMatrix(self, entryData):
        entry = entryData.get()
        temp1 = entry.split(";")
        temp2 = []
        temp3 = []
        for i in range(len(temp1)):
            temp2.append(temp1[i].split(","))
        for i in range(len(temp2)):
            aux = temp2[i]
            for j in aux:
                temp3.append(float(j))
        toReturn = [[temp3[0],temp3[1]],[temp3[2],temp3[3]]]
        return toReturn
    
    def transformToRetaList(self, entryData):
        temp1 = entryData.get().split(";")
        temp2 = []
        temp3 = []
        for i in range(len(temp1)):
            temp2.append(temp1[i].split(","))
        for i in range(len(temp2)):
            aux = temp2[i]
            for j in aux:
                temp3.append(float(j))
        return temp3

    def transformListPoligono(self, entryData):
        temp = self.transformToRetaList(entryData)
        listaDePontos = [(temp[i], temp[i+1]) for i in range(0, len(temp), 2)]
        return listaDePontos


    def transformToCurvaMatrix(self, entryData):
        pass

    


    