
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class CartesianPlotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Plano Cartesiano Interativo")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.ax.grid(True)
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)

        self.plot_point(2, 3)  # Exemplo: plotando o ponto (2, 3)

        self.frame = tk.Frame(master=self.master)
        self.frame.pack(side=tk.BOTTOM)

        self.label_x = tk.Label(self.frame, text="X:")
        self.label_x.grid(row=0, column=0)
        self.entry_x = tk.Entry(self.frame)
        self.entry_x.grid(row=0, column=1)

        self.label_y = tk.Label(self.frame, text="Y:")
        self.label_y.grid(row=0, column=2)
        self.entry_y = tk.Entry(self.frame)
        self.entry_y.grid(row=0, column=3)

        self.plot_button = tk.Button(self.frame, text="Plotar Ponto", command=self.plot_point_from_entry)
        self.plot_button.grid(row=0, column=4)

    def plot_point(self, x, y):
        self.ax.plot(x, y, 'ro')
        self.canvas.draw()

    def plot_point_from_entry(self):
        try:
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
            self.plot_point(x, y)
        except ValueError:
            pass

def main():
    root = Tk()
    app = CartesianPlotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
