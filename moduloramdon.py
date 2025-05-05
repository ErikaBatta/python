import random

# colores = ["rojo", "azul", "verde", "amarillo"]

# print(random.choice(colores))           # Ejemplo: "azul"
# print(random.sample(colores, 2))        # Ejemplo: ["rojo", "verde"]
# random.shuffle(colores)
# print(colores)                          # Ejemplo: ["verde", "amarillo", "rojo", "azul"]
            


#ejemplo aleatorio juego piedra papel o tijera
import random 
opciones= ["piedra", "papel", "tijera"]
jugador=input("ingrese piedra papel o tijera")
    
juego= ( random.choice(opciones))
print(juego)
if juego == "piedra" and jugador == "tijera" or juego=="papel" and jugador == "piedra" or juego=="tijeras" and jugador == "papel":
 print("gano el computador")
elif jugador == "tijera" and juego == "papel" or jugador == "papel" and juego == "piedra" or jugador == "piedra" and juego == "tijera":
 print("gano el jugador") 
else:
 print("es un empate")
 
#  # Ejemplos de números aleatorios
# print(random.randint(1, 10))     # Ejemplo: 7
# print(random.random())           # Ejemplo: 0.6524
# print(random.uniform(1, 10))     # Ejemplo: 3.785
 
#  numero = random.randint(1,100)
#  intentos = 0
 
#  while true:
#      gues = int (input("ingrese un numero"))
#      if numero == gues:
#          intentos +=1
#          print(f"has ganado con {intentos}intentos")
#          break 
#      elif numero < gues:
#          intentos +=1
#          print("el numero es menor")
#     elif numero > gues:
#          intentos +=1
#          print("el numero es mayor")       