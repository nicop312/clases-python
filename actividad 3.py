#Nicolas_Avalos 10/04/2026, Variables.py
############

nombre, apellido,NombreCompleto,pais,ciudad,edad,anos,Estacasado,esVerdadero,luzencendida = "Nicolas", "Avalos", "Nicolas Emanuel Avalos Ruales", "Ecuador","Quito",16,"diploma 1", False,True,True

#Actividad 2

print(type(nombre))
print(type(apellido))
print(type(NombreCompleto))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(anos))
print(type(Estacasado))
print(type(esVerdadero))
print(type(luzencendida)) 

#Actividad 3

len_nombre = len(nombre)
len_apellido = len(apellido)
print("Longitud de nombre:" ,len_nombre)
print("Longitud de apellido:" ,len_apellido)
if len_nombre > len_apellido:
    print("El nombre es más largo que el apellido")
elif len_nombre < len_apellido:
    print("El apellido es más largo que el nombre")
else:
    print("El nombre y el apellido tienen la misma longitud")

#Actividad 4

numeroUno = 5
numeroDos = 4

#Actividad 5

total = numeroUno + numeroDos
print("Total:", total)

#Actividad 6

diferencia = numeroUno - numeroDos
print("Diferencia:", diferencia)

#Actividad 7

producto = numeroUno * numeroDos
print("Producto:", producto)

#Actividad 8

division = numeroUno / numeroDos
print("División:", division)

#Actividad 9

residuo = numeroUno % numeroDos
print("Residuo:", residuo)

#Actividad 10

potencia = numeroUno ** numeroDos
print("Potencia:", potencia)

#Actividad 11

divisionEntera = numeroUno // numeroDos
print("División entera:", divisionEntera)

#Actividad 12

radio = 30

#Actividad 13

pi = 3.141592653589793
areaCirculo = pi * radio ** 2
print("Área del círculo:", areaCirculo)

#Actividad 14

circunferenciaCirculo = 2 * pi * radio
print("Circunferencia del círculo:", circunferenciaCirculo)

#Actividad 15

radio_usuario = (input("Ingresa el radio del círculo: "))
area_usuario = pi * radio_usuario ** 2
print("Área del círculo con radio del usuario:", area_usuario)

#Actividad 16

nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
pais_usuario = input("Ingresa tu país: ")
edad_usuario = int(input("Ingresa tu edad: "))
print("Nombre:", nombre_usuario)
print("Apellido:", apellido_usuario)
print("País:", pais_usuario)
print("Edad:", edad_usuario)

#Actividad 17

help('keywords')
