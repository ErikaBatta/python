respuestas = { "hola":"hola como esta?",
         "que cursos tienen disponibles": "cursos de ai, programacion, analisis de datos, blockchain",
        "donde esta ubicados": "estamos ubicados en la cra 29 # 50-20",
        "como me puedo inscribir":"para inscribirte visitar la pagina de talento tech",
        "chao": "hasta luego fue un gusto ayudarte"
        }

def obtener_respuesta(mensaje):
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
        return "no entiendo tu pregunta"

print("hola, soy un chatbot de soporte al cliente")
while True: 
    mensaje = input("ingrese su consulta")
    if mensaje.lower()=="salir":
      break
    respuesta=obtener_respuesta(mensaje)
    print(respuesta)