# MANUAL TÉCNICO
## Luis Carlos Corleto Marroquín
### Proyecto 1 - Aplicación numérica con análisis léxico.
**OBJETIVO GENERAL** 
Que el estudiante cree una herramienta la cual sea capaz de reconocer un lenguaje, dado por medio de un analizador léxico el cual cumple con las reglas establecidas, manejando la lectura y escritura de archivos para el manejo de la información. A través de un entorno gráfico. 
**OBJETIVOS ESPECÍFICOS**
* Implementar por medio de estados un analizador léxico. 
* Utilizar funciones de manejo de cadenas de caracteres en lenguaje 
Python. 
* Programar un Scanner para el análisis léxico. 
* Construir un scanner basándose en un autómata finito determinístico. 
* Crear una herramienta para interactuar de forma visual con el usuario con 
Tkinter 
* Crear diagramas con la librería Graphviz.
### DESCRIPCIÓN 
Se solicita la lectura de código fuente, el cual tendrá un formato JSON, creando un 
programa el cual sea capaz de identificar un lenguaje dado, identificando los errores 
léxicos y ejecutando las instrucciones correspondientes. 
Se listarán una serie de instrucciones las cuales deben de ser ejecutadas, 
cumpliendo con el formato asignado, generando un resultado y graficarlos en un 
archivo según la jerarquía operacional de cada instrucción. Colocando el resultado 
en cada nodo que aplique. 
Los errores deben ser generados en un archivo JSON.
#### ANALIZADOR LÉXICO:
``` 
tabla_errores = []

def Autómata (archivo): 
    global tabla_errores 
    tabla_tokens = [] 
    fila =       
    columna = 0 
    i = 0 
    varTemp = "" 
    estadoActual = 0 
    Strings = ["operaciones", "operacion", "configuraciones", "texto", "fondo", "fuente", "forma"] 
    operadores = ["suma", "resta", "multiplicacion", "division", "potencia", "raiz", "inverso", "seno", "coseno", "tangente", "mod"] 
    valor = ["valor1", "valor2"]

    while i < len(archivo): 

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
            if archivo[i] == '/' or archivo[i] == '\\':
                columna += 1
                
            if archivo[i] == '"':
                if varTemp in Strings:
                    tabla_tokens.append([varTemp, "String", fila, columna])
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
    res = [tabla_tokens, tabla_errores]
    return res 
```
1. La función recibe como entrada o parámetro un archivo (representado como una cadena llamada archivo -> nombre del parámetro).

2. Declara algunas variables globales, como tabla_errores (una lista vacía para almacenar los errores) y tabla_tokens (una lista vacía para almacenar los tokens).

3.  Inicializa algunas variables locales, como fila y columna para rastrear la posición actual en el archivo, varTemp para construir lexemas (números, ya que los strings se manejaron por listas), y estadoActual para controlar el estado actual del autómata.

4. Se definen algunas listas de palabras clave (Strings, operadores, valor) que se utilizarán para verificar si un lexema es una palabra clave, operador o valor.

5. Luego, la función entra en un bucle while que recorre cada carácter en el archivo de entrada.

6. En función del estado actual (estadoActual), la función realiza diferentes acciones: 
   + Estado 0: En este estado, el programa maneja caracteres como comas, llaves, corchetes, dos puntos, comillas, dígitos, saltos de línea y espacios en blanco. Dependiendo del carácter actual, se agregan tokens a tabla_tokens o errores a tabla_errores.
   + Estado 1: Se realiza la transición  a este estado cuando se ha detectado un dígito. El programa construye un lexema numérico y cambia a este estado. Si se encuentra un punto decimal, pasa al estado 3.

   + Estado 2: Se realiza la transición a este estado cuando se ha detectado una comilla de apertura. El programa construye un lexema y busca una comilla de cierre. Dependiendo del contenido entre comillas, clasifica el lexema como "String", "Operador", "Valor" o "Cadena" y agrega un token correspondiente a tabla_tokens.

   + Estado 3: Se realiza la transición a este estado después de encontrar un punto decimal en el estado 1. El programa continúa construyendo un número decimal y pasa al estado 4.

   + Estado 4: En este estado, el programa continúa construyendo un número decimal hasta que se encuentre un carácter que no sea un dígito. Luego, agrega un token numérico a tabla_tokens.

7. El bucle while continúa hasta que se haya procesado todo el archivo.

8. Al final, el programa retorna una lista que contiene dos listas: tabla_tokens y tabla_errores. Esto permite acceder a los tokens y errores encontrados durante el análisis del archivo.

#### PROCESAMIENTO DE LAS OPERACIONES
Para el procesamiento de las operaciones se manejaron varios métodos y funciones para la ejecución correcta de cada operación, utilizando recursividad y un poco de análisis sintáctico para indicar el final de las operaciones, la separación de valores y más.
```
tokens = []  
dot_file_name = "grafo.dot"   
node_counter = 1

def generate_node_id():
    global node_counter
    node_id = f"node_{node_counter}"
    node_counter += 1
    return node_id    
```
Este método genera un identificador único para un nodo en el grafo. Utiliza una variable global node_counter para mantener un contador de nodos y genera identificadores únicos en forma de "node_x". 
```
def realOp (cadena):
    global tokens
    global dot_file_name
    respuesta = Autómata(cadena)
    tokens = respuesta[0]
    tokens.reverse()
    iniciar()
    with open(dot_file_name, "a") as dot_file:
        dot_file.write(f'\n    }}')

    graph = graphviz.Source.from_file(dot_file_name)

    output_file_name = "grafo"
    graph.format = "png"
    graph.render(output_file_name, view=False)
    with open(dot_file_name, "r") as dot_file:
        lines = dot_file.readlines()

    with open(dot_file_name, "w") as dot_file:
        dot_file.write(lines[0])  
```
Este método toma una cadena como entrada y realiza el análisis de las operaciones matemáticas en la cadena utilizando el autómata definido en el método Autómata. Luego, genera un grafo en formato DOT que representa las operaciones y sus resultados, y lo guarda en un archivo llamado "grafo.dot". Finalmente se utiliza la biblioteca graphviz para renderizar el grafo en un archivo PNG llamado "grafo.png".
* Llama al método Autómata para obtener una lista de tokens y errores.
* Almacena los tokens en la variable global tokens.
* Invierte la lista de tokens.
* Llama al método iniciar() para comenzar la ejecución de las operaciones.
* Cierra la definición del grafo en el archivo DOT.
* Carga el grafo desde el archivo DOT, configura la salida en formato PNG y renderiza el grafo en un archivo llamado "grafo.png".
* Lee las líneas del archivo DOT para actualizar el archivo con el nuevo grafo.
```
def iniciar():
    try:
        tokens.pop()     
        operaciones()
        tokens.pop()
        configGraph()
        tokens.pop()
        print("Terminaron las operaciones") 
    except Exception as e:
        pass
```
Este método contiene un poco de análisis sintáctico y llama a los métodos necesarios para analizar las operaciones.
* Elimina los tokens correspondientes a la palabra clave "configuraciones" y el símbolo ":".
* Llama al método operaciones() para analizar las operaciones.
* Elimina el token correspondiente al cierre de llave "}".
* Imprime el mensaje que indica que terminaron las operaciones.
```
def operaciones():
    try:
        for _ in range(3):
            tokens.pop()
        operacion()
        tokens.pop()
    except Exception as e:
        pass
```
Este método analiza una secuencia de operaciones matemáticas. En este caso, se espera que hayan 3 tokens que siempre vendrán en el archivo.
* Elimina tres tokens para avanzar a la primera operación.
* Llama al método operacion() para analizar la operación.
* Elimina el token correspondiente al cierre de llave "}".
```
def operacion():
    try:
        expresion()
        temp = tokens[-1]
        if temp[1] != "Coma":
            return
        tokens.pop()        
        operacion()
    except Exception as e:
        pass
```
Este método analiza una operación matemática, que consiste en una expresión seguida de una coma y otra operación (recursión).
* Llama al método expresion() para analizar la expresión.
* Se le asigna a la variable temporal el valor de la última posición de la lista.
* Obtiene el token temporal para verificar si es una coma.
* Si el token no es una coma, regresa, lo que indica el final de la operación actual.
* Llama recursivamente al método operacion() para analizar la siguiente operación.
```
def expresion():
    operador = ""                               
    valores = []                              
    resultado = 0           
    node_id = generate_node_id()                   

    try:
        temp = tokens.pop()                     
        temp = tokens.pop()   
        temp = tokens.pop()  
        temp = tokens.pop()                     
        operador = temp[0]
        temp = tokens.pop()  
        listavalores(valores)
        temp = tokens.pop()   

        if len(valores) == 0:
            print("No hay valores en la operación.")
            return 0

        #OPERACIONES
        if operador == "suma":
            for numero in valores:
                resultado += numero
            print(f"Operador: {operador} - ({valores[0]} + {valores[1]}) = {resultado}")
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {node_id} [label="{resultado} - Suma", fillcolor="blue", style="filled", shape="circle"]')
                for valor in valores:
                    valor_node_id = generate_node_id()  
                    dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {node_id} -> {valor_node_id}')

        elif operador == "resta":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado -= numero
            print(f"Operador: {operador} - ({valores[0]} - {valores[1]}) = {resultado}")
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {node_id} [label="{resultado} - Resta", fillcolor="blue", style="filled", shape="circle"]')
                for valor in valores:
                    valor_node_id = generate_node_id() 
                    dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {node_id} -> {valor_node_id}')
        
        elif operador == "multiplicacion":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado *= numero
            print(f"Operador: {operador} - ({valores[0]} * {valores[1]}) = {resultado}")
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {node_id} [label="{resultado} - Multiplicacion", fillcolor="blue", style="filled", shape="circle"]')
                for valor in valores:
                    valor_node_id = generate_node_id()  
                    dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {node_id} -> {valor_node_id}')
        
        elif operador == "division":
            try:
                if len(valores) > 2:
                    print("Error: La division solo admite dos valores.")
                else:
                    resultado = valores[0] / valores[1]
                    print(f"Operador: {operador} - ({valores[0]} / {valores[1]}) = {resultado}")
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {node_id} [label="{resultado} - Division", fillcolor="blue", style="filled", shape="circle"]')
                        for valor in valores:
                            valor_node_id = generate_node_id() 
                            dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                            dot_file.write(f'\n    {node_id} -> {valor_node_id}')
            except:
                resultado = 0

        elif operador == "potencia":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado **= numero
            print(f"Operador: {operador} - ({valores[0]} ^ {valores[1]}) = {resultado}")
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {node_id} [label="{resultado} - Potencia", fillcolor="blue", style="filled", shape="circle"]')
                for valor in valores:
                    valor_node_id = generate_node_id() 
                    dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {node_id} -> {valor_node_id}')
        
        elif operador == "raiz":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado **= 1/numero
            print(f"Operador: {operador} - √{valores[0]} = {resultado}")
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {node_id} [label="{resultado} - Raiz", fillcolor="blue", style="filled", shape="circle"]')
                for valor in valores:
                    valor_node_id = generate_node_id() 
                    dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {node_id} -> {valor_node_id}')

        elif operador == "inverso":
            try:
                valor_original = valores[0]
                resultado = 1 / valor_original
                print(f"Operador: {operador} - 1/{valores[0]} = {resultado}")
                print("1/", valores[0], "=", resultado, operador)
                with open(dot_file_name, "a") as dot_file:
                    dot_file.write(f'\n    {node_id} [label="{resultado} - Inverso", fillcolor="blue", style="filled", shape="circle"]')
                    for valor in valores:
                        valor_node_id = generate_node_id() 
                        dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {node_id} -> {valor_node_id}')
            except:
                print("No se pudo operar, el inverso es 0 o contiene más de un valor.")

        elif operador == "mod":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado %= numero
            print(f"Operador: {operador} - ({valores[0]} % {valores[1]}) = {resultado}")
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {node_id} [label="{resultado} - Modulo", fillcolor="blue", style="filled", shape="circle"]')
                for valor in valores:
                    valor_node_id = generate_node_id() 
                    dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {node_id} -> {valor_node_id}')
            
        elif operador == "seno":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'seno' debe tener un solo valor.")
                else:
                    resultado = math.sin(math.radians(valores[0]))
                    print(f"Operador: {operador} - sen({valores[0]})")
                    #print("sen(", valores[0], ") =", resultado, operador)
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {node_id} [label="{resultado} - Seno", fillcolor="blue", style="filled", shape="circle"]')
                        for valor in valores:
                            valor_node_id = generate_node_id()  
                            dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                            dot_file.write(f'\n    {node_id} -> {valor_node_id}')
            except:
                print("No se pudo calcular el seno.")
                resultado = 0

        elif operador == "coseno":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'coseno' debe tener un solo valor.")
                else:
                    resultado = math.cos(math.radians(valores[0]))
                    print(f"Operador: {operador} - cos({valores[0]})")
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {node_id} [label="{resultado} - Coseno", fillcolor="blue", style="filled", shape="circle"]')
                        for valor in valores:
                            valor_node_id = generate_node_id()
                            dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                            dot_file.write(f'\n    {node_id} -> {valor_node_id}')
            except:
                print("No se pudo calcular el coseno.")
                resultado = 0

        elif operador == "tangente":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'tangente' debe tener un solo valor.")
                else:
                    resultado = math.tan(math.radians(valores[0])) 
                    print(f"Operador: {operador} - tan({valores[0]})")
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {node_id} [label="{resultado} - Tangente", fillcolor="blue", style="filled", shape="circle"]')
                        for valor in valores:
                            valor_node_id = generate_node_id()
                            dot_file.write(f'\n    {valor_node_id} [label="{valor}", fillcolor="blue", style="filled", shape="circle"]')
                            dot_file.write(f'\n    {node_id} -> {valor_node_id}')
            except:
                print("No se pudo calcular la tangente.")
                resultado = 0

        return resultado
            
    except Exception as e:
        return 0
```
Este método analiza una expresión que consiste en un operador seguido de valores.

* Se inicializan variables para el operador, los valores y el resultado de la operación.
* Genera un identificador único para el nodo del grafo.
* Se extraen los tokens necesarios para obtener el operador y los valores.
* Realiza diferentes operaciones matemáticas según el operador y almacena el resultado en la variable resultado. También agrega nodos al grafo DOT para representar la operación y los valores involucrados.
* En caso de excepción, se maneja el error y se devuelve 0, esto para que no se detenga la ejecución del programa por algún error en el archivo no contemplado a parte de los errores léxicos.
```
def listavalores(valores):
    try:
        numero = valor()
        valores.append(numero)
        temp = tokens[-1]

        if temp[1] != "Coma":
            return
        tokens.pop()        
        listavalores(valores)
    except Exception as e:
        pass
```
Este método analiza una lista de valores separados por comas y los almacena en una lista.

* Llama al método valor() para obtener el primer valor.
* Obtiene el token temporal para verificar si es una coma.
* Si el token no es una coma, regresa, lo que indica el final de la lista de valores.
* Llama recursivamente al método listavalores() para analizar el siguiente valor.
```
def valor():
    try:
        tokens.pop()                    
        tokens.pop()     
        resultado = numero()
        return resultado

    except Exception as e:
        return float(0)
```
Este método analiza un valor que puede ser un número o una expresión entre corchetes.

* Se descartan los tokens correspondientes a la palabra clave "valor1" y "valor2", los dos puntos ":" y el valor numérico o la apertura de corchete.
* Llama al método numero() para obtener un valor numérico.
* Retorna el resultado.
* Retorna un 0 si se encuentra un error.
```
def numero():
    resultado = 0  
    try:
        temp = tokens[-1]
        if temp[1] == "Numero":
            try:
                tokens.pop()        
                resultado = float(temp[0])
            except:
                resultado = float(0)
        
        else:
            temp = tokens.pop()     

            if temp[1] != "Corchete de apertura":           
                return 
            resultado = float(expresion())
            temp = tokens.pop()     

            if temp[1] != "Corchete de cierre":           
                return 
        return resultado
    except Exception as e:
        return 0
```
Este método analiza un número, ya sea un número real o una expresión entre corchetes.

* Inicializa la variable resultado.
* Verifica si el token actual es un número. Si es así, se extrae y se almacena en la variable resultado.
* Si el token actual es una apertura de corchete, se llama al método expresion() para analizar una expresión encerrada entre corchetes.
* Devuelve el valor numérico o 0 en caso de error.
```
def configGraph():
    try:
        temp = tokens.pop()     
        if temp[0] != "configuraciones":            
            return 
        temp = tokens.pop()    

        if temp[1] != "Dos Puntos":           
            return 
        temp = tokens.pop()   

        if temp[1] != "Corchete de apertura":           
            return 
        temp = tokens.pop()    

        if temp[1] != "Llave de apertura":            
            return 0
        ajustesGraph() 
        temp = tokens.pop()        

        if temp[1] != "Llave de cierre":         
            return 0
        temp = tokens.pop()   

        if temp[1] != "Corchete de cierre":           
            return 
    except Exception as e:
        pass
```
Este método analiza la configuración del grafo.

* Elimina los tokens correspondientes a la palabra clave "configuraciones" y el símbolo ":".
* Verifica que la configuración incluya una llave de apertura y llama al método ajustesGraph() para analizar los ajustes de configuración.
* Verifica que la configuración incluya una llave de cierre y una corchete de cierre.
```
def ajustesGraph():
    try:
        temp = tokens.pop()                     
        if temp[1] != "String":            
            return 
        temp = tokens.pop()   

        if temp[1] != "Dos Puntos":           
            return 
        temp = tokens.pop()   

        if temp[1] != "Cadena":           
            return 
        temp = tokens[-1]

        if temp[1] != "Coma":
            return
        tokens.pop()        
        ajustesGraph()
    except Exception as e:
        pass
```
Este método analiza los ajustes de configuración del grafo.

* Elimina los tokens correspondientes a la configuración de ajustes.
* Verifica que los ajustes incluyan una cadena y una cadena de ajustes. Luego, se obtiene el token temporal para verificar si hay una coma.
* Si el token no es una coma, regresa, lo que indica el final de los ajustes.
* Llama recursivamente al método ajustesGraph() para analizar los ajustes restantes.