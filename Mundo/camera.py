import sys
import tkinter as tk
import cv2
import numpy as np

# Cria uma instância da classe Tk
root = tk.Tk()

# Cria uma instância da classe Canvas
canvas = tk.Canvas(root, width=640, height=480)

# Adiciona o canvas à janela
canvas.pack()

# Cria uma instância da classe Label
label = tk.Label(root, text="Vetorizar")

# Adiciona o label à janela
label.pack()

# Cria uma instância da classe VideoCapture
cap = cv2.VideoCapture(0)

# Verifique se a câmera está conectada
if not cap.isOpened():
    print("A câmera não está conectada")
    sys.exit(1)

# Defina o tamanho da imagem
cap.set(3, 640)
cap.set(4, 480)

# Loop infinito para capturar imagens
while True:
    # Captura uma imagem da câmera
    ret, frame = cap.read()

    # Converte a imagem para um array NumPy
    img = np.array(frame)

    # Mostra a imagem na janela
    canvas.create_image(0, 0, image=img)

    # Aguarda uma tecla ser pressionada
    key = cv2.waitKey(1)

    # Se a tecla `q` for pressionada, o programa é encerrado
    if key == ord("q"):
        break

# Fecha a câmera
cap.release()

# Limpa todas as janelas abertas
cv2.destroyAllWindows()

# Cria um botão que diz "Vetorizar"
button = tk.Button(root, text="Vetorizar", command="vector")

# Adiciona o botão à janela
button.pack()

# Define o tamanho da janela
root.geometry("640x480")

# Mostra a janela
root.mainloop()

# Função que vetoriza a imagem
def vectorize():
    # Captura a imagem da janela
    img = canvas.postscript_as_string()

    # Vectoriza a imagem
    vectorized_img = cv2.imread(img)

    # Mostra a imagem vetorizada na janela
    canvas.create_image(0, 0, image=vectorized_img)