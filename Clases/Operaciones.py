from Analizador import Autómata
import math

tokens = []                

def realOp (cadena):
    global tokens
    respuesta = Autómata(cadena)
    tokens = respuesta[0]            
    tokens.reverse()
    iniciar()

def iniciar():
    try:
        tokens.pop()     
        operaciones()
        tokens.pop()
        configGraph()
        tokens.pop()
        print("Terminaron las operaciones") 
    except Exception as e:
        print("Error: " + str(e))

def operaciones():
    try:
        for _ in range(3):
            tokens.pop()
        operacion()
        tokens.pop()
    except Exception as e:
        print("Error: " + str(e))

def operacion():
    try:
        expresion()
        temp = tokens[-1]
        if temp[1] != "Coma":
            return
        tokens.pop()        
        operacion()
    except Exception as e:
        print("Error: " + str(e))

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

        elif operador == "resta":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado -= numero
        
        elif operador == "multiplicacion":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado *= numero
        
        elif operador == "division":
            try:
                if len(valores) > 2:
                    print("Error: La division solo admite dos valores.")
                else:
                    resultado = valores[0] / valores[1]
            except:
                resultado = 0

        elif operador == "potencia":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado **= numero
        
        elif operador == "raiz":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado **= 1/numero

        elif operador == "inverso":
            try:
                valor_original = valores[0]
                resultado = 1 / valor_original
            except:
                print("No se pudo operar, el inverso es 0 o contiene más de un valor.")

        elif operador == "mod":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado %= numero
            
        elif operador == "seno":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'seno' debe tener un solo valor.")
                else:
                    resultado = math.sin(math.radians(valores[0]))
            except:
                print("No se pudo calcular el seno.")
                resultado = 0

        elif operador == "coseno":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'coseno' debe tener un solo valor.")
                else:
                    resultado = math.cos(math.radians(valores[0]))
            except:
                print("No se pudo calcular el coseno.")
                resultado = 0

        elif operador == "tangente":
            try:
                if len(valores) != 1:
                    print("Error: La operación 'tangente' debe tener un solo valor.")
                else:
                    resultado = math.tan(math.radians(valores[0])) 
            except:
                print("No se pudo calcular la tangente.")
                resultado = 0

        print("El resultado de la operacion ", operador, " es: ", resultado)
        return resultado
            
    except Exception as e:
        print("Error: " + str(e))
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
        print("Error: " + str(e))

def valor():
    try:
        tokens.pop()                    
        tokens.pop()     
        resultado = numero()
        return resultado

    except Exception as e:
        print("Error: " + str(e))
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
        print("Error: " + str(e))
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
        print("Error: " + str(e))

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
        print("Error: " + str(e))
