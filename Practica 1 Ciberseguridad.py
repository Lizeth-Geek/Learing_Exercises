#Práctica de ciberseguridad - Curso 7 Python_Certificado con Google y Coursera

#Ejercicio sobre tipos de cadenas
username = ["elarson", "bmoreno", "tshah"]
data_type = type(username)
print(data_type)

#Ejercicios
#Quieres imprimir un mensaje que le indique al usuario “inténtalo de nuevo” 
#siempre y cuando el valor de la variable de intento sea 5 o menos, y deseas 
#incrementar el valor de esta variable en 1 cada vez que pase por el bucle.

attempt = 1
while attempt <= 5:
print("Inténtalo de nuevo.")
attempt = attempt + 1

#Ejercicios
#Deseas dar la bienvenida a 3 usuarios de una lista por su nombre
#(por ejemplo, “Bienvenido, Emerick Larson”).
name = ["Emrick Larson", "Estrella Ortiz", "Tori Shah"]
for i in name:
print("Te damos la bienvenida,", i)

#Ejercicios
#Explicación
#Cómo llamar a una función
#Después de definir una función, puedes usarla en tu código tantas veces como la necesites. 
#Cuando utilizas una función después de definirla, se dice que estás llamando (o invocando) 
#a dicha función. Para hacerlo, escribe su nombre seguido de paréntesis. A fin de llamar a 
#la función que definiste antes, podrás utilizar el siguiente código: display_investigation_message()
#Si bien utilizarás funciones de formas más complejas a medida que vayas ampliando 
#tus conocimientos, el siguiente código proporciona una introducción sobre cómo 
#la función display_investigation_message() puede formar parte de una sección más extensa de código.

def display_investigation_message():
    print("investigate activity")
application_status = "potential concern"
email_status = "okay"
if application_status == "potential concern":
    print("application_log:")
    display_investigation_message()
if email_status == "potential concern":
    print("email log:")
    display_investigation_message()

#La función display_investigation_message() se usa dos veces en el código. Imprimirá 
#mensajes de "investigate activity" sobre dos registros diferentes cuando las condiciones 
#especificadas se evalúen como True (verdaderas). En este ejemplo, solo la primera sentencia 
#condicional se evalúa como True, por lo que el mensaje se imprime una vez.

#Otro ejemplo práctico

def alert():
print("Problema de seguridad detectado.")
alert() 

#Otro ejemplo práctico
#En el siguiente ejemplo, la información devuelta a partir de la llamada
# a remaining_login_attempts se almacena en una variable nombrada remaining_attempts. 
#Luego, esta variable se usa en una sentencia condicional que imprime el mensaje 
#"Your account is locked" cuando remaining_attempts es menor o igual a 0. 
def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3, 3)
if remaining_attempts <= 0:
    print("Your account is locked")

#Otro ejemplo práctico
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)

#Otro ejemplo práctico
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

#Otro ejemplo práctico
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

#La función sorted() ordena los componentes de una lista, opera en cualquier iterable, 
#como una cadena, y devuelve elementos ordenados en una lista. Por defecto, los 
#clasifica en orden ascendente. Cuando se le proporciona un iterable que contiene números, 
#los ordena de menor a mayor; esto incluye iterables que contienen datos numéricos, 
#así como aquellos que contienen datos de cadena que comienzan con números. Aquellos 
#iterables que contengan cadenas que empiecen con caracteres alfabéticos se ordenarán 
#alfabéticamente.

#Otro ejemplo práctico
"""Otra forma de escribir comentarios es con """


#Otro ejemplo práctico
