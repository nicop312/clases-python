Numero = int(input("Ingrese el numeo a multiplicar: "))
D = int(input("Ingrese el numero hasta donde se va a multiplicar: "))
x= int(input("Ingrese el numero desde donde se comienza a multiplicar: "))
for i in range(x, D+1):
    m = Numero * i
    print(Numero, "x", i, "=", m)
#Ejercicio 2
notas = [8,8,8,8,10]
suma = 0
for i in range (1,4):
    suma = suma + notas[i]
promedio = suma/3
print ("El pomedio de las notas es: ", promedio)
