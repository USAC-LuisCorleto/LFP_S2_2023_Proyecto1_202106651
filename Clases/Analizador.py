import json

tabla_errores = []

def Autómata (archivo):
    global tabla_errores
    tabla_tokens = [] #Lista para guardar los tokens.
    fila = 1 #Fila del lexema        
    columna = 0 #Columna del lexema
    i = 0 #Contador para el recorrido de la cadena (archivo)
    varTemp = "" #Variable temporal para armar los lexemas (números)
    estadoActual = 0 #Variable para movilizarnos de estado a estado.
    palabrasReservadas = ["operaciones", "operacion", "configuraciones", "texto", "fondo", "fuente", "forma"] #Palabras reservadas del lenguaje.
    operadores = ["suma", "resta", "multiplicacion", "division", "potencia", "raiz", "inverso", "seno", "coseno", "tangente", "mod"] #También son palabras reservadas pero se manejan por separado para la vericiación en la operación.
    valor = ["valor1", "valor2"] #Todas las operaciones tendrán como máximo 2 valores, exceptuando mod y las trigonométricas.

    while i < len(archivo): #Recorre caracter por caracter

        if estadoActual == 0:
            if archivo[i] == ",":
                tabla_tokens.append([archivo[i], "Coma", fila, columna])
                varTemp = ""
                columna += 1

            elif archivo[i] == "{":
                tabla_tokens.append([archivo[i], "Llave de apertura", fila, columna])
                varTemp = ""
                columna += 1

            elif archivo[i] == "}":
                tabla_tokens.append([archivo[i], "Llave de cierre", fila, columna])
                varTemp = ""
                columna += 1

            elif archivo[i] == "[":
                tabla_tokens.append([archivo[i], "Corchete de apertura", fila, columna])
                varTemp = ""
                columna += 1

            elif archivo[i] == "]":
                tabla_tokens.append([archivo[i], "Corchete de cierre", fila, columna])
                varTemp = ""
                columna += 1

            elif archivo[i] == ":":
                tabla_tokens.append([archivo[i], "Dos Puntos", fila, columna])
                varTemp = ""
                columna += 1

            elif archivo[i] == '"':
                estadoActual = 2
                columna += 1

            elif archivo[i].isdigit():
                varTemp += archivo[i]
                estadoActual = 1
                columna += 1

            elif archivo[i] == "\r":
                pass

            elif archivo[i] == "\n":
                columna = 1
                fila += 1
        
            elif archivo[i] == " ":
                columna += 1

            elif archivo[i] == "\t":
                columna += 1
        
            else:
                tabla_errores.append([archivo[i], fila, columna])
                varTemp = ""
                columna += 1

        elif estadoActual == 1:
            if archivo[i].isdigit():
                varTemp += archivo[i]   
                columna += 1

            elif archivo[i] == ".":
                varTemp += archivo[i]  
                estadoActual = 3
                columna += 1

            else:
                tabla_tokens.append([varTemp, "Numero", fila, columna])
                varTemp = ""       
                columna += 1
                i -= 1          
                estadoActual = 0

        elif estadoActual == 2:
                
            if archivo[i] == '"':
                if varTemp in palabrasReservadas:
                    tabla_tokens.append([varTemp, "Reservada", fila, columna])
                elif varTemp in operadores:
                    tabla_tokens.append([varTemp, "Operador", fila, columna])
                elif varTemp in valor:
                    tabla_tokens.append([varTemp, "Valor", fila, columna])
                else:
                    tabla_tokens.append([varTemp, "Cadena", fila, columna])
                varTemp = ""
                columna += 1
                estadoActual = 0

            elif archivo[i] == "\n": 
                tabla_errores.append([varTemp, fila, columna]) 
                varTemp = ""
                columna = 1
                fila += 1
                estadoActual = 0

            else:
                varTemp += archivo[i] 
                columna += 1 

        elif estadoActual == 3:
            if archivo[i].isdigit():
                varTemp += archivo[i]
                estadoActual = 4
                columna += 1
            
            else:
                tabla_errores.append([varTemp, fila, columna])
                varTemp = ""
                columna += 1
                estadoActual = 0

        elif estadoActual == 4:
            if archivo[i].isdigit():
                varTemp += archivo[i]
                columna += 1
        
            else:
                tabla_tokens.append([varTemp, "Numero", fila, columna])
                varTemp = ""
                columna += 1
                i -= 1
                estadoActual = 0
        i += 1
    res = [tabla_tokens, tabla_errores] #Retornamos las 2 listas.
    return res

'''def errores():
    global tabla_errores 
    
    errores_json = {"errores": []}

    for i, error in enumerate(tabla_errores):
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

    with open("errores.json", "w", encoding="utf-8") as json_file:
        json.dump(errores_json, json_file, indent=4)'''

def main():
    entrada ='''
                {
                    "operaciones": [+
                                        {
                                            "operacion":"suma",
                                            "valor1": 4.5,
                                            "valor2": '
                                        }
                                    ], 
                    "configuraciones": [-
                                            {
                                                "texto": "Operaciones",
                                                "fondo": "azul"
                                            }
                                        ]
                }'''
    salida = Autómata(entrada)
    print("TOKENS")
    for token in salida[0]:
        print(token)
    #errores()

if __name__ == "__main__":
    main()
