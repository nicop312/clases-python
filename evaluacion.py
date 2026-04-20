nombre = "Lucía"
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))

## Parte A
##1.-
## a) Indica el tipo de dato de cada variable.
## NOMBRE: str, EDAD: int, PROMEDIO: float, CURSOS: list
## b) Escribe qué mostraría el programa en pantalla.
## <class 'str'>
## <class 'int'>
## <class 'float'>
## <class 'list'>
## c) Explica qué hace len(nombre).
## La función len() devuelve la cantidad de caracteres que tiene la variable nombre, incluyendo espacios. En este caso, el resultado sería 6, ya que "Lucía" tiene 6 caracteres (L, u, c, í, a).
##2.-
## a) ¿Qué diferencia hay entre print() e input()?
## La función print() se utiliza para mostrar información en la pantalla, mientras que input() se utiliza para solicitar al usuario que ingrese datos desde el teclado. print() no espera ninguna entrada del usuario, mientras que input() detiene la ejecución del programa hasta que el usuario ingresa algo y presiona Enter.
## b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
## Porque input() devuelve un dato de tipo string (cadena de texto) por defecto. Si intentamos usar ese dato directamente en un cálculo que espera un número (como una suma o una multiplicación), se producirá un error de tipo, ya que no se pueden realizar operaciones matemáticas con cadenas de texto sin convertirlas primero a un tipo numérico (como int o float).
## c) Explica la diferencia entre /, // y %.
## El operador / realiza una división normal y devuelve un resultado de tipo float, incluso si ambos operandos son enteros. El operador // realiza una división entera y devuelve el resultado como un entero, descartando cualquier parte decimal. El operador % devuelve el resto de la división entre dos números, es decir, el valor que queda después de dividir el primer número por el segundo.
## d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
## python --version
## e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
##import keyword
##print(keyword.kwlist) 
##SECCION B
## 3.-
##El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione.
##ancho = float(input("Ingrese el ancho del terreno: "))
##largo = float(input("Ingrese el largo del terreno: "))
##precio = float(input("Ingrese el precio por metro cuadrado: "))
##area = ancho * largo
##costo = area * precio
##print("Área total: ", area)
##print("Costo estimado: ", costo)
##Luego responde:
##a) ¿Cuáles eran los errores principales?
## Los errores principales eran que las variables ancho, largo y precio se estaban tomando como strings (cadenas de texto) debido a que se usaba input() sin convertir los datos a un tipo numérico. Para corregir esto, se deben convertir las entradas a float o int antes de realizar los cálculos. Además, la connecion de variables se uso el +, lo que esta incorrecto ya que se usa , para conectar variables en print() y no +, que se usa para concatenar strings. 
##b) ¿Por qué tu corrección sí permite obtener resultados válidos?
## Porque al convertir las entradas a un tipo numérico (float), el programa puede realizar las operaciones matemáticas necesarias para calcular el área y el costo sin generar errores de tipo. De esta manera, el programa puede procesar correctamente los datos ingresados por el usuario y mostrar resultados válidos.
## 4.-
##Escribe un fragmento de código que haga lo siguiente:
##1. Cree la variable frase con el texto "Tecnología para todos".
##2. Muestre la frase en mayúsculas.
##3. Muestre la cantidad de caracteres de la frase.
##4. Verifique si la palabra "Python" está dentro de la frase.
##5. Reemplace "Tecnología" por "Programación".
##6. Divida la frase en palabras usando split(). 
##Respuesta:
##Tecnología_para_todos = "Tecnología para todos"
##print(Tecnología_para_todos.upper())
##print(len(Tecnología_para_todos))
##print("Python" in Tecnología_para_todos)
##print(Tecnología_para_todos.replace("Tecnología", "Programación"))
##print(Tecnología_para_todos.split())
