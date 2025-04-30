#print("hola mundo")


#declarar una variable

# Guardamos un número en una variable
edad = 25
# Mostramos el valor
print(edad)  # 25
    
#tipos de variables
nombre = "Ana"      # Texto (string)
edad = 30           # Número entero (int)
altura = 1.75       # Número decimal (float)
es_mayor = True     # Valor lógico (booleano)

print(nombre, edad, altura, es_mayor)
    

#guardar el valor de una variable
x = 10  # x empieza con 10
print(x)  # 10

x = 20  # Ahora x vale 20
print(x)  # 20
    
#asignacion multiple
a, b, c = 5, 10, 15

print(a)  # 5
print(b)  # 10
print(c)  # 15
    
#nombrar variables:
#Pueden contener letras, números y guion bajo (_).
#No pueden empezar con un número.
#No deben ser palabras reservadas de Python.
nombre_usuario = "Carlos"  # Correcto
edad2 = 25  # Correcto
#2edad = 30  # Incorrecto (empieza con número)
#print = "Hola"  # Incorrecto (print es una palabra reservada)

#variables en operaciones matematicas
a = 10
b = 5

suma = a + b
multiplicacion = a * b

print(suma)  # 15
print(multiplicacion)  # 50

#tarea 1
# Escribe tu código aquí
nombre = "Erika"
edad = 25
ciudad = "Bucaramanga"
print(nombre, edad, ciudad)

#tarea 2
# Escribe tu código aquí

num1 = 6
num2 = 3

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(suma, resta, multiplicacion, division)

  #METODOS

#metodo upper
texto = "Hola, mundo"
print(texto.upper())  # "HOLA, MUNDO"

#metodo strip
texto = "  Python  "
print(texto.strip())  # "Python"

#metodo replace
texto = "Me gusta Python"
print(texto.replace("Python", "Java"))  # "Me gusta Java"

#metodo split
texto = "manzana,banana,uva"
print(texto.split(","))  # ['manzana', 'banana', 'uva']

#metodo join
lista = ["Python", "es", "genial"]
print(" ".join(lista))  # "Python es genial"

#metodo find
texto = "Aprender Python"
print(texto.find("Python"))  # 9
print(texto.find("Java"))    # -1
print(texto.find("Aprender"))  
    
#metodo count
texto = "banana banana banana"
print(texto.count("banana"))  # 3

#metodo startwith(si inicia en una subcadena especifica)
texto = "Hola, mundo"
print(texto.startswith("Hola"))  # True
print(texto.startswith("Mundo"))  # False

#metodo endswith
texto = "archivo.txt"
print(texto.endswith(".txt"))  # True
print(texto.endswith(".jpg"))  # False

#metodo isdigit
texto = "12345"
print(texto.isdigit())  # True
print("123a".isdigit())  # False

#metodo isalpha
texto = "Python"
print(texto.isalpha())  # True
print("Python3".isalpha())  # False

#metodo isalnum
texto = "Python3"
print(texto.isalnum())  # True
print("Python 3".isalnum())  # False (espacio no es alfanumérico)

#metodo title
texto = "bienvenidos a python"
print(texto.title())  # "Bienvenidos A Python"
    
#metodo capitalize
texto = "python es genial"
print(texto.capitalize())  # "Python es genial"

#metodo translate

# Crear una tabla de traducción
tabla = str.maketrans("aeiou", "12345")

# Aplicar la traducción a una cadena
texto = "hola amigos"
nuevo_texto = texto.translate(tabla)

print(nuevo_texto)  # h4l1 1m3g4s


#eliminar elementos

# Crear una tabla de eliminación
tabla = str.maketrans("", "", "aeiou")

# Aplicar la traducción
texto = "hola amigos"
nuevo_texto = texto.translate(tabla)

print(nuevo_texto)  # hl mgs
        
    
#eliminar signos de puntuacion

import string

# Crear una tabla para eliminar puntuación
tabla = str.maketrans("", "", string.punctuation)

# Texto con puntuación
texto = "¡Hola! ¿Cómo estás?"

# Aplicar la traducción
texto_limpio = texto.translate(tabla)

print(texto_limpio)  # Hola Como estas    
    
    
    
    
    

     