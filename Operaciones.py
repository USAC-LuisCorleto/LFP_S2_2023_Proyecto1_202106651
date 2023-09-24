from Analizador import Autómata
import graphviz
import math

tokens = []  
dot_file_name = "grafo.dot"   
node_counter = 1

def generate_node_id():
    global node_counter
    node_id = f"node_{node_counter}"
    node_counter += 1
    return node_id           

def realOp (cadena):
    global tokens
    global dot_file_name
    respuesta = Autómata(cadena)
    tokens = respuesta[0] #El retorno se hizo en una lista y la lista de tokens se guardó en la primera posición, en este caso la posición 0.   
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