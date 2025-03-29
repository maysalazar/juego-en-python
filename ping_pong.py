import tkinter as tk

# Configuración del juego
ANCHO = 600
ALTO = 400
VELOCIDAD_PELOTA = [3, 3]

class Pong:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        
        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="black")
        self.canvas.pack()
        
        # Crear paletas y pelota
        self.paleta_izq = self.canvas.create_rectangle(20, 150, 30, 250, fill="white")
        self.paleta_der = self.canvas.create_rectangle(570, 150, 580, 250, fill="white")
        self.pelota = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        
        # Movimiento inicial
        self.dx, self.dy = VELOCIDAD_PELOTA
        
        # Controles
        self.root.bind("<w>", lambda e: self.mover_paleta(self.paleta_izq, -20))
        self.root.bind("<s>", lambda e: self.mover_paleta(self.paleta_izq, 20))
        self.root.bind("<Up>", lambda e: self.mover_paleta(self.paleta_der, -20))
        self.root.bind("<Down>", lambda e: self.mover_paleta(self.paleta_der, 20))
        
        self.actualizar_juego()
    
    def mover_paleta(self, paleta, dy):
        self.canvas.move(paleta, 0, dy)
        
    def actualizar_juego(self):
        self.canvas.move(self.pelota, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.pelota)
        
        # Rebote con paredes
        if y1 <= 0 or y2 >= ALTO:
            self.dy = -self.dy
        
        # Rebote con paletas
        if (self.colision(self.paleta_izq) or self.colision(self.paleta_der)):
            self.dx = -self.dx
        
        # Reiniciar si la pelota sale
        if x1 <= 0 or x2 >= ANCHO:
            self.canvas.coords(self.pelota, 290, 190, 310, 210)
            self.dx = VELOCIDAD_PELOTA[0] if x1 <= 0 else -VELOCIDAD_PELOTA[0]
        
        self.root.after(20, self.actualizar_juego)
    
    def colision(self, paleta):
        px1, py1, px2, py2 = self.canvas.coords(paleta)
        x1, y1, x2, y2 = self.canvas.coords(self.pelota)
        return px1 < x2 and px2 > x1 and py1 < y2 and py2 > y1

if __name__ == "__main__":
    root = tk.Tk()
    juego = Pong(root)
    root.mainloop()