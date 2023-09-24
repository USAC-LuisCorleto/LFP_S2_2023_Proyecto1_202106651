tabla_errores = []

def Autómata (archivo): #Método para analizar el archivo.
    global tabla_errores #Tabla de tokens global para realizar el archivo de errores en la interfaz.
    tabla_tokens = [] #Lista para guardar los tokens.
    fila = 1 #Fila del lexema        
    columna = 0 #Columna del lexema
    i = 0 #Contador para el recorrido de la cadena (archivo)
    varTemp = "" #Variable temporal para armar los lexemas (números)
    estadoActual = 0 #Variable para movilizarnos de estado a estado.
    Strings = ["operaciones", "operacion", "configuraciones", "texto", "fondo", "fuente", "forma"] #Palabras Strings del lenguaje.
    operadores = ["suma", "resta", "multiplicacion", "division", "potencia", "raiz", "inverso", "seno", "coseno", "tangente", "mod"] #También son palabras Strings pero se manejan por separado para la verficiación en la operación.
    valor = ["valor1", "valor2"] #Todas las operaciones tendrán como máximo 2 valores, exceptuando mod y las trigonométricas.

    while i < len(archivo): #Recorre caracter por caracter.

        if estadoActual == 0: #Estado actual, identifica llaves, corchetes, comas y dos puntos.
            if archivo[i] == ",": #Identifica una coma.
                tabla_tokens.append([archivo[i], "Coma", fila, columna])
                varTemp = ""
                columna += 1 #Aumenta la columna en 1

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

            elif archivo[i] == '"': #Aquí termina el string analizado en el estado 2.
                estadoActual = 2
                columna += 1

            elif archivo[i].isdigit(): #Si identifica una número se va al estado 1.
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

        elif estadoActual == 1: #Aquí va formando los números, si identifica un punto es decimal y se va al estado 3 a formarlo.
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

        elif estadoActual == 2: #Aquí luego de las comillas puede venir cualquier cosa, exceptuando espacios en blanco, guarda cualquier string permitido.
            if archivo[i] == '/' or archivo[i] == '\\':
                columna += 1
                
            if archivo[i] == '"':
                if varTemp in Strings:
                    tabla_tokens.append([varTemp, "String", fila, columna]) #Para los strings.
                elif varTemp in operadores:
                    tabla_tokens.append([varTemp, "Operador", fila, columna]) #Para los operadores.
                elif varTemp in valor:
                    tabla_tokens.append([varTemp, "Valor", fila, columna]) #Para los valores.
                else:
                    tabla_tokens.append([varTemp, "Cadena", fila, columna]) #Esto es poara las configuraciones.
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
    res = [tabla_tokens, tabla_errores] #Lista con las 2 listas dentro.
    return res #Se retorna la lista con las 2 listas

def mostrarTokens(salida): #Método para imprimir los tokens en la caja de texto.
    print(' ' * 51 + "TOKENS RECONOCIDOS" + ' ' * 51)
    print('-' * 120)
    print("{:<35} {:<35} {:<30} {:<25}".format("Lexema ", "Tipo de Token", "Fila", "Columna")) #Se aplicó formato.
    print('-' * 120)
    for token in salida[0]:
        print("{:<35} {:<35} {:<30} {:<25}".format(token[0], token[1], token[2], token[3]))
