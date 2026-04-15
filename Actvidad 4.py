edad= int(16)
estatura= float(1.75)
print("Ingrese la altura y base del triangulo") 
base = float(input("Base:"))
altura = float(input("Altura:"))
Area= 0.5 * base * altura
# %%
print("Ingrese lados a,b,c de un triangulo:")
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
# %%
print("Ingrese longitud y ancho del rectángulo:")
longitud = float(input("longitud: "))
ancho = float(input("ancho: "))
area= longitud * ancho
perimetro= 2 * (longitud + ancho)
# %%
print("Ingrese el radio del círculo:")
radio = float(input("Radio: "))
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio
print("Encuentra la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10)")
pendiente= (10 - 2) / (6 - 2) 
distancia= ((6 - 2)**2 + (10 - 2)**2)**0.5
print("Calcula el valor de y en la función:y = x² + 6x + 9")
print("Prueba con diferentes valores de x y determina para qué valor de x, y es igual a 0.")
def calcular_y(x):
    return x**2 + 6*x + 9
valores_x = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
print("Valores de x y correspondientes y:")
for x in valores_x:
    y = calcular_y(x)
    print(f"x = {x}, y = {y}")
print("y es igual a 0 cuando x = -3")
len("python") < len("dragon")
len("python") > len("dragon")
len("python") == len("dragon")
resultado = "on" in "python" and "on" in "dragon"
print(f"¿'on' está en 'python' y en 'dragon'? {resultado}")
resultado= "jergan" in "Espero que este curso no este lleno de jerga"
len("python") 
float(len("python"))
str(len("python"))
verificacion = (7 // 3) == int(2.7)
print(f"¿7 // 3 == int(2.7)? {verificacion}") 
verificacion2= "10" == int(10)
print(f"¿'10' == int(10)? {verificacion2}") 
verificacion3= float("9.8") == 10
print(f"¿('9.8') == 10? {verificacion3}")
horas_trabajadas = float(input("Ingrese las horas que trabaja por día: "))
tarifa_por_hora = float(input("Ingrese su tarifa por hora: "))
salario_diario = horas_trabajadas * tarifa_por_hora
print(f"Su salario diario es: {salario_diario}")
años_vida = int(input("Ingrese su edad: "))
seg_año= int(31536000)
seg_vida= años_vida * seg_año
print(f"Su vida en segundos es: {seg_vida}")
#%%
print("Tabla:")
for n in range(1, 6):
    print (f"{n} 1{n} {n**2} {n**3}")
