import tkinter as tk
from tkinter import font, filedialog, messagebox
from Analizador import Autómata
from Analizador import mostrarTokens
from Operaciones import realOp
import json
import sys
import io

ventana = tk.Tk()
cajatxt = tk.Text(ventana, height=30, width=120)
archivo_actual = None   
tabla_errores = []

def abrirArchivo():
    global archivo_actual
    archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
    if archivo:
        archivo_actual = archivo
        with open(archivo, "r") as f:
            contenido = f.read()
            cajatxt.delete(1.0, tk.END)
            cajatxt.insert(tk.END, contenido)

def guardarArchivo():
    global archivo_actual
    if archivo_actual:
        contenido = cajatxt.get("1.0", tk.END)
        with open(archivo_actual, "w") as f:
            f.write(contenido)
        messagebox.showinfo("Archivo guardado correctamente", "El archivo se ha guardado exitosamente.")
    else:
        guardarArchivoComo()

def guardarArchivoComo():
    global archivo_actual
    archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
    if archivo:
        archivo_actual = archivo
        contenido = cajatxt.get(1.0, tk.END)
        with open(archivo, "w") as f:
            f.write(contenido)
        messagebox.showinfo("Archivo guardado correctamente", "El archivo se ha guardado exitosamente.")

def analizarArchivo():
    contenido = cajatxt.get("1.0", tk.END)
    resultado = Autómata(contenido)
    
    sys.stdout = io.StringIO()
    mostrarTokens(resultado)
    salida = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    cajatxt.delete(1.0, tk.END)
    cajatxt.insert(tk.END, salida)
    

def mostrarErrores():
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

def mostrarReporte():
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
        
def salir():
    ventana.destroy()

def Interfaz():

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

    fuenteN = font.Font(family="Arial", size=16, weight="bold")

    botAnalizar = tk.Button(ventana, text="Analizar", bg="gray", font=fuenteN, height=3, width=20, command=analizarArchivo )
    botErrores = tk.Button(ventana, text="Errores", bg="gray", font=fuenteN, height=3, width=20, command=mostrarErrores)
    botReporte = tk.Button(ventana, text="Reporte", bg="gray", font=fuenteN, height=3, width=20, command=mostrarReporte)

    botAnalizar.pack(side=tk.LEFT, padx=20, pady=20)
    botErrores.pack(side=tk.LEFT, padx=20, pady=20)
    botReporte.pack(side=tk.LEFT, padx=20, pady=20)

    botAnalizar.pack(side="left")
    botErrores.pack(side="left")
    botReporte.pack(side="right")

    ventana.mainloop()
