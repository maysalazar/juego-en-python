import tkinter as tk
import random

# Opciones del juego
opciones = ["Piedra", "Papel", "Tijera"]

# Función para jugar
def jugar(eleccion_usuario):
    eleccion_computadora = random.choice(opciones)
    
    # Determinar el resultado
    if eleccion_usuario == eleccion_computadora:
        resultado = "¡Empate! 😐"
    elif (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_usuario == "Tijera" and eleccion_computadora == "Papel"):
        resultado = "¡Ganaste! 🎉"
    else:
        resultado = "¡Perdiste! 😢"

    # Mostrar resultado en la interfaz
    etiqueta_resultado.config(text=f"Tu elección: {eleccion_usuario}\nComputadora: {eleccion_computadora}\n{resultado}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("400x300")

# Etiqueta de instrucciones
etiqueta_instrucciones = tk.Label(ventana, text="Elige una opción:", font=("Arial", 12))
etiqueta_instrucciones.pack(pady=10)

# Botones para las opciones
boton_piedra = tk.Button(ventana, text="🪨 Piedra", font=("Arial", 12), command=lambda: jugar("Piedra"))
boton_piedra.pack(pady=5)

boton_papel = tk.Button(ventana, text="📄 Papel", font=("Arial", 12), command=lambda: jugar("Papel"))
boton_papel.pack(pady=5)

boton_tijera = tk.Button(ventana, text="✂️ Tijera", font=("Arial", 12), command=lambda: jugar("Tijera"))
boton_tijera.pack(pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14), fg="blue")
etiqueta_resultado.pack(pady=20)

# Iniciar ventana
ventana.mainloop()
