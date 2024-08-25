import tkinter as tk
import customtkinter
from TabView import TabView

customtkinter.set_appearance_mode('light')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rasterização de Retas")
        self.geometry("1080x600")

        self.TitleLabel = customtkinter.CTkLabel(self, text="Rasterização - Computação Gráfica", font=('Helvetica',40))
        self.TitleLabel.grid(row=0, column=0, padx=20, pady=20, sticky='se')
        
        #TabView
        self.tab_view = TabView(master=self)
        self.tab_view.grid(row=1, column=0, padx=20, pady=20, sticky='ne')

#Inicialização
app = App()
app.mainloop()