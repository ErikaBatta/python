import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyARHI6okdHILflJ4r3JsyE3WEXtHRYj7OE"
genai.configure(api_key=GEMINI_API_KEY)
modelo = genai.GenerativeModel("gemini-2.0-flash")

def obtener_respuesta(mensaje):
    try:
        respuesta = modelo.generate_content(mensaje)
        return respuesta.text.strip()
    except Exception as e:
        print("Error al generar respuesta:", e)
        return "Lo siento, hubo un problema al procesar tu pregunta."
    
print("hola soy un chabot de soporte al cliente")
while True:
    mensaje = input("ingrese su consulta")
    if mensaje.lower() == "salir":
        break
    respuesta = obtener_respuesta(mensaje)
    print(respuesta)