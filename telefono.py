import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("TelePhone")  # Título de la ventana
root.geometry("350x700")  # Aumentamos la altura aún más para dar espacio suficiente
root.resizable(False, False)  # Evitamos que se pueda redimensionar la ventana

# Establecer el color de fondo de la ventana principal
root.config(bg="black")

# Variable para el número marcado
numero_marcado = tk.StringVar()

# Función para actualizar la pantalla
def agregar_numero(numero):
    numero_marcado.set(numero_marcado.get() + str(numero))

# Función llamada
def llamar():
    numero_marcado.set(f"Llamando al {numero_marcado.get()}...")

# Función borrar el número
def colgar():
    numero_marcado.set("") 

# Pantalla para mostrar el número marcado (Usamos un Label en lugar de un Entry para mayor control sobre el tamaño)
pantalla = tk.Label(root, textvariable=numero_marcado, font=("Arial", 18), bd=5, relief="sunken", justify="right", bg="black", fg="white", height=2)
pantalla.pack(pady=20, padx=10, fill="x")

# Marco teclado
marco_teclado = tk.Frame(root, bg="black")
marco_teclado.pack(pady=20)

# Crear el grid de botones del teclado
botones = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2), 
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), 
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), 
    ("*", 3, 0), ("0", 3, 1), ("#", 3, 2), 
]

# Función para crear un botón circular
def crear_boton_circular(texto, fila, columna):
    # Crear un círculo usando Canvas
    boton = Canvas(marco_teclado, width=80, height=80, bg="black", bd=0, highlightthickness=0)  # Eliminar bordes extra
    # Creamos el óvalo y lo guardamos en una variable para poder modificarlo después
    ovalo = boton.create_oval(5, 5, 75, 75, fill="lightblue", outline="black", width=2)  # Borde negro más delgado
    boton.create_text(40, 40, text=texto, font=("Arial", 18), fill="black")
    boton.grid(row=fila, column=columna, padx=10, pady=10)  # Espacio entre botones

    # Función que se ejecuta cuando el botón es presionado
    def boton_presionado(e, t=texto):
        agregar_numero(t)
        boton.itemconfig(ovalo, fill="lightgreen")  # Cambiar color del círculo a verde cuando se presiona

    # Función que se ejecuta cuando el botón es soltado
    def boton_soltado(e):
        boton.itemconfig(ovalo, fill="lightblue")  # Volver al color original (lightblue)

    # Asociar eventos
    boton.bind("<ButtonPress-1>", boton_presionado)  # Cuando se presiona el botón
    boton.bind("<ButtonRelease-1>", boton_soltado)  # Cuando se suelta el botón

# Botones numéricos circulares
for(texto, fila, columna) in botones:
    crear_boton_circular(texto, fila, columna)

# Marco para los botones de "Llamar" y "Colgar"
marco_botones = tk.Frame(root, bg="black")
marco_botones.pack(pady=20)

# Cargar y redimensionar los iconos con transparencia
def cargar_icono_rizado(path):
    # Abrimos la imagen
    icono_img = Image.open(path)
    
    # Aseguramos que la imagen sea PNG y tenga transparencia
    icono_img = icono_img.convert("RGBA")  # Convertir la imagen a formato con canal alfa (transparente)
    
    # Redimensionamos la imagen al tamaño adecuado
    icono_img = icono_img.resize((60, 60))  
    
    # Crear una máscara circular
    mask = Image.new("L", icono_img.size, 0)  # Creamos una máscara en escala de grises
    mask.paste(255, (0, 0, icono_img.width, icono_img.height))  # Poner el color blanco en toda la imagen
    
    # Aplicar la máscara circular en la imagen
    icono_img.putalpha(mask)  # Ahora aplicamos la máscara en la imagen con el canal alfa

    return ImageTk.PhotoImage(icono_img)

# Cargar los iconos de llamada y colgar
icono_llamar = cargar_icono_rizado("./img/call.png")
icono_colgar = cargar_icono_rizado("./img/hangupphone.png")

# Botón de llamar con icono
boton_llamar = tk.Button(marco_botones, image=icono_llamar, command=llamar, relief="flat", width=80, height=80, bg="black", bd=0, highlightthickness=0)
boton_llamar.grid(row=0, column=0, padx=10, pady=10)  # Coloca el botón en la primera columna

# Botón de colgar con icono
boton_colgar = tk.Button(marco_botones, image=icono_colgar, command=colgar, relief="flat", width=80, height=80, bg="black", bd=0, highlightthickness=0)
boton_colgar.grid(row=0, column=1, padx=10, pady=10)  # Coloca el botón en la segunda columna

# Iniciar la aplicación para que se active todo
root.mainloop()
