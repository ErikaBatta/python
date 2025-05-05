def conversor_fc(temp):
#formula
celcius = ( temp - 32)/1.8
return celcius

def conversor_cf(temp):
#formula
farenheit = ( temp * 1.8) + 32
return farenheit

tipo= input("ingrese F para obtener farenheit y C para obtener celcius")


if tipo == "C":
    temp = float(input("ingrese la temperatura en farenheit"))
print(conversor_fc(temp))
elif tipo == "F":
     temp = float(input("ingrese la temperatura en celcius"))
print(conversor_cf(temp))
else:
print("el valor ingresado es incorrecto")