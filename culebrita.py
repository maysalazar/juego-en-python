import tkinter as tk
import random

# Configuración del juego
ANCHO = 400
ALTO = 400
TAMANO_CELDA = 20

# Direcciones
DIRECCIONES = {"Arriba": (0, -1), "Abajo": (0, 1), "Izquierda": (-1, 0), "Derecha": (1, 0)}

class JuegoSerpiente:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de la Serpiente")
        
        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="black")
        self.canvas.pack()
        
        self.serpiente = [(100, 100), (90, 100), (80, 100)]
        self.direccion = "Derecha"
        self.comida = self.generar_comida()
        
        self.root.bind("<KeyPress>", self.cambiar_direccion)
        self.actualizar_juego()
        
    def generar_comida(self):
        x = random.randint(0, (ANCHO // TAMANO_CELDA) - 1) * TAMANO_CELDA
        y = random.randint(0, (ALTO // TAMANO_CELDA) - 1) * TAMANO_CELDA
        return (x, y)
    
    def cambiar_direccion(self, evento):
        if evento.keysym in DIRECCIONES:
            nueva_direccion = evento.keysym
            if (DIRECCIONES[nueva_direccion][0] + DIRECCIONES[self.direccion][0] != 0) or \
               (DIRECCIONES[nueva_direccion][1] + DIRECCIONES[self.direccion][1] != 0):
                self.direccion = nueva_direccion

    def actualizar_juego(self):
        cabeza_x, cabeza_y = self.serpiente[0]
        mov_x, mov_y = DIRECCIONES[self.direccion]
        nueva_cabeza = (cabeza_x + mov_x * TAMANO_CELDA, cabeza_y + mov_y * TAMANO_CELDA)
        
        if (nueva_cabeza in self.serpiente or 
            nueva_cabeza[0] < 0 or nueva_cabeza[1] < 0 or
            nueva_cabeza[0] >= ANCHO or nueva_cabeza[1] >= ALTO):
            self.canvas.create_text(ANCHO//2, ALTO//2, text="¡Game Over!", fill="red", font=("Arial", 24))
            return
        
        self.serpiente.insert(0, nueva_cabeza)
        
        if nueva_cabeza == self.comida:
            self.comida = self.generar_comida()
        else:
            self.serpiente.pop()
        
        self.dibujar_elementos()
        self.root.after(100, self.actualizar_juego)
    
    def dibujar_elementos(self):
        self.canvas.delete("all")
        for segmento in self.serpiente:
            self.canvas.create_rectangle(segmento[0], segmento[1], segmento[0] + TAMANO_CELDA, segmento[1] + TAMANO_CELDA, fill="green")
        
        self.canvas.create_oval(self.comida[0], self.comida[1], self.comida[0] + TAMANO_CELDA, self.comida[1] + TAMANO_CELDA, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoSerpiente(root)
    root.mainloop()
