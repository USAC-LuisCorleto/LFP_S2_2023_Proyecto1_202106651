# MANUAL DE USUARIO
## Luis Carlos Corleto Marroquín
### Proyecto 1 - Aplicación numérica con análisis léxico.
#### Menú principal
![Imágen 1](Images/../../Images/Img%201.png)
El menú principal tiene un diseño agradable, con botones accesibles al momento de la ejecución del programa, el usuario podrá interactuar con la funcionalidad de los distintos botontes que se explicarán a continuación.
![Imágen 2](../Images/Img%202.png)
El menú cuenta con un botón "Archivo" tipo cascada que despliega distintas opciones.
**-Abrir:** El usuario podrá abrir un archivo JSON mediante el siguiente menú.
![Imágen 3](../Images/Img%203.png)
Deberá seleccionar exclusivamente un archivo JSON para la analización correspondiente, este archivo que seleccione el usuario, se mostrará en la ventana de texto que contiene la interfaz principal, como en la siguiente imágen.
![Imágen 4](../Images/Img%205.png)
Aquí se mostrará el contenido del archivo abierto anteriormente, además el usuario puede modificar el contenido del archivo JSON como quiera, tomando en cuenta los errores por aparte de un archivo JSON, como el cierre correcto de las llaves, el uso de las comas y demás, si el usuario modifica el archivo puede analizarlo y utilizar cualquiera de las funcionalidades de las botones.
**-Guardar:** Si el usuario abrió un archivo y lo modifica, tiene la opción de "Guardar" que permite al usuario guardar los cambios que realizó, aquí es imporante mencionar que el programa identifica si un archivo fue un abierto o no, ya que si el usuario intenta guardar sin previamente abrir un archivo, el menú que le saldrá al usuario será el de guardar como, la razón es que se interpretar el contenido de la caja de texto como un nuevo archivo, esto no interfiere en ninguna funcionalidad del programa, pero es importante mencionarlo.
**-Guardar como:** En esta opción el usuario puede guardar el archivo o contenido que está manejando actualmente y modificar o guardar con el nombre que él desee, independientemente de si se abrió un archivo o no.
**-Salir:** El usuario puede detener la ejecución del menú con esta opción, cierra la ventana.
#### Botones
![Imágen 1](Images/../../Images/Img%201.png)
De nuevo con el menú principal, debajo del botón desplegable "Archivo" se encuentra la zona de botones que realizan la funcionalidad del proyecto, se explicará su funcionalidad a continuación:
**-Analizar:** Si previamente el usuario seleccionó un archivo, puede hacer uso de este botón, esta funcionalidad analizar el archivo e identifica los tokens reconocidos y permitidos por el programa, poniendo de ejemplo el archivo que abrió puntos atrás
![Imágen 4](../Images/Img%205.png)
se abrió el archivo y se presionó el botón analizar
![Imágen 5](../Images/Img%206.png)
una vez se haya presionado, se mostrará un mensaje de diálogo indicando que se analizó correctamente el archivo, además en la caja de texto de la interfaz, se muestran, el lexema, tipo de token, fila y columna de los tokens reconocidos en el archivo.
**-Errores:** De nuevo, previamente seleccionado un archivo, el usuario puede generar un archivo JSON mediante el botón, que mostrará los errores léxicos del archivo con el siguiente formato: 
: : : ![Imágen 6](../Images/Img%208.png) : : :