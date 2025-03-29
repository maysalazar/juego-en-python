import tkinter as tk
import random

# Número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Función para verificar el número
def verificar():
    try:
        numero_usuario = int(entrada.get())
        if numero_usuario < numero_secreto:
            resultado.config(text="Demasiado bajo. Intenta de nuevo!", fg="red")
        elif numero_usuario > numero_secreto:
            resultado.config(text="Demasiado alto. Intenta de nuevo!", fg="red")
        else:
            resultado.config(text=f"¡Correcto! El número era {numero_secreto}", fg="green")
    except ValueError:
        resultado.config(text="Ingresa un número válido", fg="red")

# Crear ventana
ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.geometry("400x250")

# Etiqueta de instrucciones
etiqueta = tk.Label(ventana, text="Adivina el número entre 1 y 100", font=("Arial", 12))
etiqueta.pack(pady=10)

# Entrada de número
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botón para verificar
boton = tk.Button(ventana, text="Adivinar", font=("Arial", 12), command=verificar)
boton.pack(pady=5)

# Etiqueta de resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

# Iniciar ventana
ventana.mainloop()

