import tkinter as tk
from tkinter import font
from tkinter import font, filedialog, messagebox
from Analizador import Autómata
from Analizador import mostrarTokens
from Operaciones import realOp
import json
import sys
import io

# Colores
bg_color = "#2E2E2E"
fg_color = "#FFFFFF"
ventana = tk.Tk() #Ventana principal.
cajatxt = tk.Text(ventana, height=30, width=120) #Caja de texto.
fuente = font.Font(family="Helvetica", size=12) #Cambio de fuente para los botones.
ventana.config(bg=bg_color) #Color del background de la ventana.

archivo_actual = None #Booleano para el manejo del archivo (Guardar, guardar como, abrir, salir).
tabla_errores = []

def abrirArchivo(): #Método o comando para abrir un archivo y colocar el contenido en la caja de texto.
    global archivo_actual
    archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
    if archivo:
        archivo_actual = archivo
        with open(archivo, "r") as f:
            contenido = f.read()
            cajatxt.delete(1.0, tk.END)
            cajatxt.insert(tk.END, contenido)

def guardarArchivo(): #Método o comando para guardar el archivo editado en la caja de texto actual, si no se abrió ningun archivo y se guarda, se mandará al método guardarComo.
    global archivo_actual
    if archivo_actual:
        contenido = cajatxt.get("1.0", tk.END)
        with open(archivo_actual, "w") as f:
            f.write(contenido)
        messagebox.showinfo("Archivo guardado correctamente", "El archivo se ha guardado exitosamente.")
    else:
        guardarArchivoComo()

def guardarArchivoComo(): #Métdo o comando que permite guardar el archivo con un nombre.
    global archivo_actual
    archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
    if archivo:
        archivo_actual = archivo
        contenido = cajatxt.get(1.0, tk.END)
        with open(archivo, "w") as f:
            f.write(contenido)
        messagebox.showinfo("Archivo guardado correctamente", "El archivo se ha guardado exitosamente.")

def analizarArchivo(): #Método para analizar el archivo abierto, específicamente lo que está en la caja de texto.
    contenido = cajatxt.get("1.0", tk.END)
    resultado = Autómata(contenido)
    
    sys.stdout = io.StringIO()
    mostrarTokens(resultado)
    salida = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    cajatxt.delete(1.0, tk.END)
    cajatxt.insert(tk.END, salida)
    messagebox.showinfo("Archivo analizado", "Se ha analizado correctamente el archivo.")
    
def mostrarErrores(): #Método o comando que genera el archivo de errores del archivo analizado.
    contenido = cajatxt.get("1.0", tk.END)
    resultado = Autómata(contenido)
    
    errores_json = {"errores": []}

    for i, error in enumerate(resultado[1]):
        error_dict = {
            "No": i + 1,
            "descripcion": {
                "lexema": error[0],
                "tipo": "error lexico",
                "columna": error[2],
                "fila": error[1]
            }
        }
        errores_json["errores"].append(error_dict)

    with open("Erorres_202106651.json", "w", encoding="utf-8") as json_file:
        json.dump(errores_json, json_file, indent=4, ensure_ascii=False)
    messagebox.showinfo("JSON de errores", "El archivo JSON Errores se ha generado correctamente.")

def mostrarReporte(): #Método o comando que genera el reporte de graphviz y muestra las operaciones en la caja de texto.
    global archivo_actual
    if archivo_actual:
        with open(archivo_actual, 'r') as json_file:
            json_data = json_file.read()
        json_data = json_data.lower()
        cajatxt.delete(1.0, tk.END)
        sys.stdout = io.StringIO()
        realOp(json_data)

        salida = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__
        cajatxt.insert(tk.END, salida)
        messagebox.showinfo("Informe generado", "El informe se ha generado exitosamente.")
    
def borrarTexto(): #Método o comando para borrar el texto de la caja, solo por comodidad.
    cajatxt.delete("1.0", tk.END)

def salir(): #Método o comando para salir de la ventana.
    ventana.destroy()

def Interfaz(): #Aqui está la declaración de los botones, diseño y asignación de comandos a los botones.
    frame_botones = tk.Frame(ventana, bg=bg_color)
    frame_botones.pack(fill="x")
    ventana.title("Menú Principal")
    ventana.geometry("1000x600")

    barraMen = tk.Menu(ventana)

    menArchivo = tk.Menu(barraMen, tearoff=False)
    menArchivo.add_command(label="Abrir", command=abrirArchivo)
    menArchivo.add_command(label="Guardar", command=guardarArchivo)
    menArchivo.add_command(label="Guardar como", command=guardarArchivoComo)
    menArchivo.add_command(label="Salir", command=salir)

    barraMen.add_cascade(label="Archivo", menu=menArchivo)

    ventana.config(menu=barraMen)
    cajatxt.pack()

    botAnalizar = tk.Button(frame_botones, text="Analizar", font=fuente, bg="#474747", fg=fg_color, padx=20, pady=10, command=analizarArchivo)
    botErrores = tk.Button(frame_botones, text="Errores", font=fuente, bg="#474747", fg=fg_color, padx=20, pady=10, command= mostrarErrores) 
    botReporte = tk.Button(frame_botones, text="Reporte", font=fuente, bg="#474747", fg=fg_color, padx=20, pady=10, command=mostrarReporte)
    botBorrar = tk.Button(frame_botones, text="Borrar", font=fuente, bg="#474747", fg=fg_color, padx=20, pady=10, command=borrarTexto)

    botAnalizar.pack(side=tk.LEFT, padx=20, pady=20)
    botErrores.pack(side=tk.LEFT, padx=20, pady=20)
    botReporte.pack(side=tk.LEFT, padx=20, pady=20)
    botBorrar.pack(side=tk.LEFT, padx=20, pady=20)

    botAnalizar.pack(side="left")
    botErrores.pack(side="left")
    botReporte.pack(side="right")

    ventana.mainloop()
