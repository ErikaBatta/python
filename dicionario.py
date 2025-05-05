                
persona = {
    "nombre": "Carlos",
    "apellido": "Amaya",
    "edad": 30,
    "ciudad": "Bogotá"
}

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

                
persona["profesión"] = "Ingeniero"
persona["edad"] = 31

print(persona)
               
                
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
                
                               
clave = input("Ingrese una clave: ")

if clave in persona:
    print(f"{clave} existe y su valor es: {persona[clave]}")
else:
    print(f"{clave} no existe en el diccionario.")
    
               
del persona["ciudad"]
print(persona)
              
                
print(len(persona))
       
                
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}

dic1.update(dic2)
print(dic1)
             
                
claves = ["nombre", "edad", "ciudad"]
dic_predeterminado = dict.fromkeys(claves, "Desconocido")

print(dic_predeterminado)
                
                            
frase = "python es genial y python es poderoso"
palabras = frase.split()

contador = {}

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)
                
                  
diccionario = {"rojo": "red", "azul": "blue", "verde": "green"}
invertido = {valor: clave for clave, valor in diccionario.items()}

print(invertido)
                
                 
persona = {"nombre": "Carlos", "edad": 30}

# Intentar obtener la clave "profesión" con un valor por defecto
profesion = persona.get("profesión", "No especificado")

print(profesion)
                                
                