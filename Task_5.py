# Task 5.1

# El "None" es un elemento similar a "null" pero en una variable booleana seria false, se suele utilizar para representar la falta de un valor.
print(None)


def func():
    print("Hi!")


var = func()
print(var)          # Devolveria "Hi!" y tambien None.


# Task 5.2

# Crea una lista con unas etiquetas con determinados valores.
años = {"David": 21, "Manolo": 45, "Marina": 20}
print(años["Marina"])
print(años["Manolo"])


primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}

# Devuelve los valores de "red". Si intentaramos printear un valor que no esta en la lista saltara un "KeyError".
print(primary["red"])


# Task 5.3

# En el caso de los diccionarios a diferencia de las listas cuando cambias un valor lo estas haciendo sobre el valor, no sobre la posicion.
cuadrados = {1: 1, 2: 4, 3: "error", 4: 16}
cuadrados[3] = 9
cuadrados[8] = 64
cuadrados[6] = 36
print(cuadrados)

# Devuelve true o false dependiendo de si esta o no en el diccionario.
print(5 in cuadrados)
print(4 in cuadrados)
print(0 not in cuadrados)

# El ".get" devuelve el resultado del valor asignado y si no se encuentra en el diccionario devolvera un "None".
print(cuadrados.get(3))
print(cuadrados.get(7))
# Si añadimos otro argumento y el ".get" no encuentra el valor en el diccionario devolvera el segundo valor.
print(cuadrados.get(12345, "No esta en el diccionario"))


# Task 5.4

# Cuando una variable esta inicializada con parentesis en vez de con corchetes quiere decir que son tuplas. La diferencia con las listas es que los valores
# no se pueden cambiar
words = ("spam", "eggs", "sausages")
print(words[1])
# words[0] = "hola"         Esto daria un TypeError ya que las tuplas no se pueden modificar.

# Tambien se pueden crear sin poner parentesis.
words1 = "spam", "eggs", "sausages"


# Task 5.5

cuadrados1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Devuelve la lista desde la posicion 2 hasta la posicion 6 no inclusive.
print(cuadrados1[2:6])

# Devuelve la lista desde la posicion 0 hasta la posicion 1 no inclusive.
print(cuadrados1[0:1])

# Si uno de los dos elementos se omiten se toma desde el principio o desde el final.
print(cuadrados1[:4])
print(cuadrados1[4:])

# Si incluimos un tercer valor este nos dira los saltos que da la lista.
print(cuadrados1[1:4:2])
print(cuadrados1[::3])

# Se pueden utilizar numeros negativos, si esta al principio o al final se contara desde el final de la lista.
# Me devuelve los ultimos 3 numeros de la lista.
print(cuadrados1[-3:])
# Devuelve desde el 4º ultimo numero de la lista hasta el 8º.
print(cuadrados1[-4:8])

# Me devuelve la lista menos los 3 ultimos valores.
print(cuadrados1[:-3])
# Me devuelve la lista desde el 3er valor hasta el tercer ultimo.
print(cuadrados1[3:-3])

# Tambien se pueden utilizar en el tercer valor, el cual haria que se empezara a contar la lista desde atras.
# Es muy comun para darle la vuelta a las listas.
print(cuadrados1[::-1])
print(cuadrados1[4:2:-1])
print(cuadrados1[::-2])


# Task 5.6

# Crearia una lista de los cubos de los 5 primeros numeros.
cubos = [i**3 for i in range(5)]
print(cubos)

# Crearia una lista de los cuadrados de los 10 primeros numeros pero con la condicion de que el cuadrado sea un numero par.
pares = [i**2 for i in range(0, 10) if i**2 % 2 == 0]
print(pares)

# Si intentamos crear una lista con un rango demasiado grande nos dara un error de memoria "MemoryError".
# error = [2*i for i in range(10**100000)]           Esto nos dara un error de memoria por ser demasiado grande el rango.


# Task 5.7

# Para poder combinar strings con otro tipo de valores se devera utilizar el ".format" que sustiuira en orden a los valores anteriores puestos entre llaves "{}".
numeros = [4, 5, 6]
# Importante.
mensaje = "Numeros: {0}, {1}, {2}".format(numeros[0], numeros[1], numeros[2])
print(mensaje)

# Tambien se pueden meter valores en el ".format"
mensaje1 = "Los numeros son: {x}, {y}".format(x=3, y=4)
print(mensaje1)


# Task 5.8

# El ".join" convierte una lista de strings en un string con un separador.
print(",".join("Esto va entre comas"))
print(",".join(["Hello", " world"]))

# El ".split" convierte un string en una lista con un separador en ella.
print("Hello, world, hey".split(","))
# Este nos lo devuelve como solo 1 elemento en la lista.
print("Hello, world, hey".split("."))

# El ".replace" reemplaza un elemento por otro.
print("Hello David".replace("David", "World"))
print("Hello David".replace("Hello David", "World"))

# El ".startswith" devuelve true si el string empieza con el elemento que digamos y false si no.
print("Hello world".startswith("Hello"))
print("Hello world".startswith("world"))

# El ".endswith" devuelve true si el string termina con el elemento que digamos y false si no.
print("Hello world".endswith("Hello"))
print("Hello world".endswith("world"))

# El ".upper" convierte el string a letras mayusculas.
print("Hello world".upper())

# El ".lower" convierte el string a letras minusculas.
print("HELLO WORLD".lower())

# Se pueden utilizar "all" y "any" que toman como argumento una lista para devolver true o false dependiendo de si se cumple la condicion.
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("Todos son mayores que 5.")

if any([i % 2 == 0 for i in nums]):
    print("Al menos uno es par.")

# Se puede utilizar "enumerate" para iterar una lista y devolvernos la posicion con el valor correspondiente de cada elemento.
for v in enumerate(nums):
    print(v)


# Task 5.9

# Creariamos una funcion a la cual le entra un archivo y un char y nos devolveria las veces que aparece ese char en el archivo.
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Mete un archivo: ")

with open(filename) as f:
    text = f.read()

print(count_char(text, "r"))


# Creariamos un bucle que nos devolveria el porcentaje que ocupa el char en el archivo.
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))


