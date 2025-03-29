import tkinter as tk
import random

class JuegoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria")
        
        self.pares = list(range(1, 9)) * 2
        random.shuffle(self.pares)
        self.botones = []
        self.seleccionados = []
        
        self.crear_botones()
    
    def crear_botones(self):
        for i in range(4):
            fila = []
            for j in range(4):
                boton = tk.Button(self.root, text="", font=("Arial", 14), width=6, height=3,
                                  command=lambda i=i, j=j: self.mostrar_numero(i, j))
                boton.grid(row=i, column=j)
                fila.append(boton)
            self.botones.append(fila)
    
    def mostrar_numero(self, i, j):
        if len(self.seleccionados) < 2 and self.botones[i][j]["text"] == "":
            self.botones[i][j].config(text=str(self.pares[i * 4 + j]))
            self.seleccionados.append((i, j))
            
            if len(self.seleccionados) == 2:
                self.root.after(500, self.verificar_pareja)
    
    def verificar_pareja(self):
        i1, j1 = self.seleccionados[0]
        i2, j2 = self.seleccionados[1]
        
        if self.pares[i1 * 4 + j1] != self.pares[i2 * 4 + j2]:
            self.botones[i1][j1].config(text="")
            self.botones[i2][j2].config(text="")
        
        self.seleccionados = []

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoMemoria(root)
    root.mainloop()
