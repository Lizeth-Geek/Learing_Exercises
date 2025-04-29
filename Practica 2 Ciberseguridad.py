#Practica 2 Ciberseguridad

#Las cadenas en un entorno de seguridad
device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])

#Con ambas formas funciona y nos arroja como resultado la letra "h"
#Si queremos una "rebanada" slice podemos tomarla con el siguiente código
print("h32rb17"[0:3])

#Métodos y funciones de las cadenas
#Las funciones str() y len() son útiles para trabajar con cadenas.
#También puedes aplicar métodos a cadenas, incluidos
# .upper(), .lower(), e .index()00.
#Un método es una función que pertenece a un tipo de datos específico.

#str() y len()   #La función str() convierte su objeto de entrada en una cadena.
#Considera el ejemplo de una ID de empleado 19329302 que debes convertir en una cadena.
#Puedes usar la siguiente línea de código para convertirla en una cadena y almacenarla en una variable:
string_id = str(19329302)

#La segunda función que aprendiste es len(), que devuelve el número de elementos de un objeto.
device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.")

#.index()    El método .index() encuentra la primera ocurrencia de la entrada en una cadena y devuelve su ubicación.
print("h32rb17".index("r"))


#Una subcadena es una secuencia continua de caracteres dentro de una cadena. Es decir, es un pedecito de una cadena.
#Por Ejemplo "americano" _ cano
cano_index = "tsnow, cano, bmoreno - updated".index("cano")
print(cano_index)

#Ejercicio. Deseas encontrar el índice donde comienza la subcadena "192.168.243.140"
#dentro de la cadena contenida en la variable ip_addresses. 
ip_addresses = "192.168.140.81, 192.168.109.50, 192.168.243.140".index("192.168.243.140")
print(ip_addresses)


#Listas. Una lista es una estructura de datos que consta de una colección de datos en forma secuencial.
#Puedes usar listas para almacenar varios elementos en una sola variable.
#Una sola lista puede contener varios tipos de datos. 
#Ejemplos
print("Ejemplos ejercicios con listas")

username_list = ["elarson", "fgarcia", "cano", "ramore"]
print(username_list[2])

print(["elarson", "fgarcia", "cano", "ramore"][1])


#Cómo extraer una porción de una lista
#Al igual que con las cadenas, también se puede usar la notación entre corchetes para tomar una porción de una lista. 
#En este caso, esto significa extraer más de un elemento.
#Cuando se extrae una porción de una lista, el resultado es otra lista. 
#Esta lista extraída se llama sublista porque es parte de la lista original, que es más grande. 
#Para extraer una sublista mediante notación entre corchetes, debes incluir dos índices.
username_list = ["perez", "hndz", "cano", "ramirez"]
print(username_list[0:2])


#Cómo cambiar los elementos de una lista
#Para cambiar un elemento de lista, utiliza una sintaxis similar a la que utilizarías al reasignar una variable, 
#pero coloca el elemento específico para cambiar la notación entre corchetes después del nombre de la variable.
username_list = ["perez", "hndz", "cano", "ramirez"]
print("Before changing an element:", username_list)
username_list[1] = "moreno"
print("After changing an element:", username_list)


#Métodos de lista
#.insert() 
#El método .insert() agrega un elemento en una posición específica dentro de una lista. 
#Tiene dos parámetros. El primero es el índice donde insertarás el nuevo elemento,
#y el segundo es el elemento que deseas insertar.

print("Ejemplos de métodos de lista")
print(".insert()")

username_list = ["perez", "hndz", "cano", "ramirez"]
print("Before inserting an element:", username_list)
username_list.insert(2,"lopez")
print("After inserting an element:", username_list)

#.remove()
#El método .remove() elimina la primera aparición de un elemento específico en una lista. 
#Solo tiene un parámetro, el elemento que deseas eliminar.
print(".remove()")
username_list = ["perez", "hndz", "cano", "ramirez"]
print("Before removing an element:", username_list)
username_list.remove("perez")
print("After removing an element:", username_list)

#Nota: Si hay dos apariciones del mismo elemento en una lista, 
#el método .remove() solo elimina la primera instancia de ese #elemento y no todas las ocurrencias.

#.append() 
#El método .append() agrega entradas al final de una lista. 
#Su único parámetro es el elemento que deseas agregar al final de la lista.
print(".append()")
username_list = ["perez", "hndz", "cano", "ramirez"]
print("Before appending an element:", username_list)
username_list.append("chavez")
print("After appending an element:", username_list)

#El método .append() se usa a menudo con bucles for para rellenar una lista vacía con elementos.
print("#El método .append() se usa a menudo con bucles for para rellenar una lista vacía con elementos")
numbers_list = []
print("Before appending a sequence of numbers:", numbers_list)
for i in range(10):
    numbers_list.append(i)
print("After appending a sequence of numbers:", numbers_list)

#Antes del bucle for, la variable numbers_list no contiene ningún elemento. 
#Cuando se imprime, se muestra la lista vacía. 
#Luego, el bucle for itera a través de una secuencia de números 
#y usa el método .append() para agregar cada uno de estos #números a numbers_list. 
#Después del bucle, cuando se imprime la variable numbers_list, muestra estos números.


#Conceptos básicos de las expresiones regulares
print("Conceptos básicos de las expresiones regulares")
#Una expresión regular (regex) es una secuencia de caracteres que forma un patrón. 
#Puedes usarlas en Python para buscar una variedad de patrones. #Esto podría incluir direcciones IP,
#correos electrónicos o identificadores de dispositivos.

#Para acceder a expresiones regulares y funciones relacionadas #en Python, primero debes importar el módulo re. 
#Debes utilizar la siguiente línea de código para importar el módulo re:

#import re
print("import re")
#Las expresiones regulares se almacenan en Python como cadenas. 
#Luego, estas se utilizan en las funciones del módulo re para buscar en otras cadenas. 
#Hay muchas funciones en el módulo re, pero explorarás cómo funcionan las expresiones
#regulares a través de re.findall(). 
#La función re.findall() devuelve una lista de coincidencias a una expresión regular. 
#Requiere dos parámetros; el primero es la cadena que contiene el #patrón de expresión
#regular,  y el segundo es la cadena que deseas buscar.

#Los patrones que comprenden una expresión regular consisten en caracteres
#alfanuméricos y símbolos especiales. Si un patrón de expresión regular consiste solo en
#caracteres alfanuméricos, Python revisará la cadena especificada para buscar
#coincidencias con este patrón y las devolverá. En el siguiente
#ejemplo, el primer parámetro es un patrón de expresión regular
#que consiste solo en los caracteres alfanuméricos "ts". 
#El segundo parámetro, "tsnow, tshah, bmoreno", es la cadena que buscarás.

import re
re.findall("ts", "tsnow, tshah, bmoreno")

#Símbolos para expresiones regulares
#Símbolos para tipos de caracteres
#Puedes usar una variedad de símbolos para formar un patrón para tu expresión regular. 
#Algunos de estos símbolos identifican un tipo particular de carácter. 
#Por ejemplo, \w coincide con cualquier carácter alfanumérico. 
#Puedes ejecutar este código para explorar lo que re.findall() 
#devuelve al aplicar la expresión regular de "\w" a la ID de dispositivo de "h32rb17".
import re
re.findall("\w", "h32rb17")

#Debido a que cada carácter dentro de esta ID de dispositivo es alfanumérico, 
#Python devuelve una lista con siete elementos. Cada elemento 
#representa uno de los caracteres de la ID del dispositivo.
#Puedes usar estos símbolos adicionales para que coincidan con 
#tipos específicos de caracteres:
 #"." coincide con todos los caracteres, incluidos los símbolos
#"\d" coincide con todos los dígitos [0-9]
#"\s" coincide con todos los espacios individuales 
#"\." coincide con el carácter del punto
print("Ejemplo usando \d")
import re
re.findall("\d", "h23rb18")
print("esto debería de salir pero el código previo ya no corre y no sé por qué", "['3', '2', '1', '7']")

#Símbolos para cuantificar ocurrencias
#Otros símbolos cuantifican el número de ocurrencias de un carácter específico en el patrón. 
#En un patrón de expresión regular, puedes agregarlos después de
#que un carácter o un símbolo identifique un tipo de carácter para 
#especificar el número de repeticiones que coinciden con el patrón.
#Por ejemplo, el símbolo + representa una o más ocurrencias de un carácter específico. 
#En el siguiente ejemplo, el patrón lo coloca después del símbolo
# "\d" para encontrar coincidencias con una o más ocurrencias de un solo dígito:
print("Ejemplo usando \d+")
import re
re.findall("\d+", "h32rb17")
print("esto debería de salir pero el código previo ya no corre y no sé por qué", "['32', '17']")


#Otro símbolo utilizado para cuantificar el número de ocurrencias 
#es el símbolo *. El símbolo * representa cero, una o más 
#ocurrencias de un carácter específico. El siguiente código 
#sustituye el símbolo * por el + utilizado en el ejemplo anterior. 
#Es decir, deja vacios los espacios donde debería haber algo.
print("Ejemplo usando \d*")
import re
re.findall("\d*", "h32rb17")
print("esto debería de salir pero el código previo ya no corre y no sé por qué", "['', '32', '', '', '17', '']")

#Si deseas indicar un número específico de repeticiones a permitir, 
#puedes colocar este número entre llaves ({ }) después del 
#carácter o símbolo. En el siguiente ejemplo, el patrón de 
#expresión regular "\d{2}" indica a Python que devuelva todas las
#coincidencias de exactamente dos dígitos seguidos de una 
#cadena de múltiples ID de dispositivo:
print("Ejemplo usando ({ })")
import re
re.findall("\d{2}", "h32rb17 k825t0m c2994eh")
print("esto debería de salir pero el código previo ya no corre y no sé por qué", "['32', '17', '82', '29', '94']", "aunque no entiendo bien a bien porqué pasa eso, no me explico el resultado")

#Debido a que coincide con dos repeticiones, cuando Python se 
#encuentra con un solo dígito, verifica si hay otro después de él. Si 
#lo hay, Python agrega los dos dígitos a la lista y pasa al siguiente. 
#Si no lo hay, pasa al siguiente dígito sin agregar el primero a la lista.

#Nota: Python escanea cadenas de izquierda a derecha cuando se 
#compara con una expresión regular. Cuando Python encuentra 
#una parte de la cadena que coincide con el primer carácter 
#esperado que ha sido definido en la expresión regular, continúa 
#comparando los caracteres posteriores con el patrón esperado. 
#Cuando el patrón se completa, este proceso comienza de nuevo. 
#Entonces, en los casos en que aparecen tres dígitos en una fila, el 
#tercero se toma como un nuevo dígito inicial.

#También puedes especificar un rango dentro de las llaves 
#separando dos números con una coma. El primer número es el 
#número mínimo de repeticiones, y el segundo, el número máximo 
#de repeticiones. El siguiente ejemplo arroja todas las 
#coincidencias que tienen entre una y tres repeticiones de un solo dígito:
print("El siguiente ejemplo arroja todas las coincidencias que tienen entre una y tres repeticiones de un solo dígito:")
import re
re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")
print("esto debería de salir pero el código previo ya no corre y no sé por qué", "['32', '17', '825', '0', '299', '4']", "y sigo sin entender porqué pasa eso... :/")


#Cómo construir un patrón
#Construir una expresión regular requiere que descompongas el 
#patrón que estás buscando en trozos más pequeños y 
#representes estos trozos a través de los símbolos que ya 
#aprendiste. Revisa este ejemplo, en que una cadena contiene 
#múltiples piezas de información sobre los empleados de una 
#organización. Para cada empleado, la siguiente cadena contiene 
#su ID de empleado, su nombre de usuario seguido de dos puntos 
#(:), sus intentos de inicio de sesión del día y su área:

#employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"

#Tu tarea es extraer el nombre de usuario y los intentos de inicio 
#de sesión, sin el número de identificación o área del empleado.

#Para completarla mediante expresiones regulares, debes dividir 
#lo que estás buscando en componentes más pequeños. En este 
#caso, esos componentes son el número variable de caracteres en 
#un nombre de usuario, dos puntos, un espacio y un número 
#variable de dígitos individuales. Los símbolos de expresión 
#regular correspondientes son \w+, :, \s y \d+ respectivamente. Al 
#utilizar estos símbolos como tu expresión regular, puedes 
#ejecutar el siguiente código para extraer las cadenas:
print("Ejemplo de extracción de cadenas", "este si funcionó, no como los otros")
import re
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))
