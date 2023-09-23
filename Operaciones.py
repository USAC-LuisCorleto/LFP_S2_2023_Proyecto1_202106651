from Analizador import Autómata
import graphviz
import math

tokens = []  
dot_file_name = "grafo.dot"              

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

def operaciones():
    try:
        for _ in range(3):
            tokens.pop()
        operacion()
        tokens.pop()
    except Exception as e:
        pass

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

def expresion():
    operador = ""                               
    valores = []                              
    resultado = 0                              

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
            print(valores[0], "+", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {resultado} [label="{resultado} - Suma", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')

        elif operador == "resta":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado -= numero
            print(valores[0], "-", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {resultado} [label="{resultado} - Resta", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
        
        elif operador == "multiplicacion":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado *= numero
            print(valores[0], "*", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {resultado} [label="{resultado} - Multiplicacion", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
        
        elif operador == "division":
            try:
                if len(valores) > 2:
                    print("Error: La division solo admite dos valores.")
                else:
                    resultado = valores[0] / valores[1]
                    print(valores[0], "/", valores[1], "=", resultado, operador)
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {resultado} [label="{resultado} - Division", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {valores[1]} [label="{valores[1]}", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {resultado} -> {valores[0]}')
                        dot_file.write(f'\n    {resultado} -> {valores[1]}')
            except:
                resultado = 0

        elif operador == "potencia":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado **= numero
            print(valores[0], "^", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {resultado} [label="{resultado} - Potencia", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
        
        elif operador == "raiz":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado **= 1/numero
            print("√", valores[0], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {resultado} [label="{resultado} - Raiz", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')

        elif operador == "inverso":
            try:
                valor_original = valores[0]
                resultado = 1 / valor_original
                print("1/", valores[0], "=", resultado, operador)
                with open(dot_file_name, "a") as dot_file:
                    dot_file.write(f'\n    {resultado} [label="{resultado} - Inverso", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
            except:
                print("No se pudo operar, el inverso es 0 o contiene más de un valor.")

        elif operador == "mod":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado %= numero
            print(valores[0], "%", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:
                dot_file.write(f'\n    {resultado} [label="{resultado} - Mod", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}", fillcolor="blue", style="filled", shape="circle"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
            
        elif operador == "seno":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'seno' debe tener un solo valor.")
                else:
                    resultado = math.sin(math.radians(valores[0]))
                    print("sen(", valores[0], ") =", resultado, operador)
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {resultado} [label="{resultado} - Seno", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {resultado} -> {valores[0]}')
            except:
                print("No se pudo calcular el seno.")
                resultado = 0

        elif operador == "coseno":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'coseno' debe tener un solo valor.")
                else:
                    resultado = math.cos(math.radians(valores[0]))
                    print("cos(", valores[0], ") =", resultado, operador)
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {resultado} [label="{resultado} - Coseno", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {resultado} -> {valores[0]}')
                print("grafo creado")
            except:
                print("No se pudo calcular el coseno.")
                resultado = 0

        elif operador == "tangente":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'tangente' debe tener un solo valor.")
                else:
                    resultado = math.tan(math.radians(valores[0])) 
                    print("tan(", valores[0], ") =", resultado, operador)
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {resultado} [label="{resultado} - Tangente", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {valores[0]} [label="{valores[0]}", fillcolor="blue", style="filled", shape="circle"]')
                        dot_file.write(f'\n    {resultado} -> {valores[0]}')
            except:
                print("No se pudo calcular la tangente.")
                resultado = 0

        return resultado
            
    except Exception as e:
        return 0

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

def valor():
    try:
        tokens.pop()                    
        tokens.pop()     
        resultado = numero()
        return resultado

    except Exception as e:
        return float(0)

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

def ajustesGraph():
    try:
        temp = tokens.pop()                     
        if temp[1] != "Reservada":            
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