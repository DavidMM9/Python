# Task 4.1

# Si el programa encuentra una expepcion como puede ser una division entre cero se deja de ejecutar.

"""
Excepciones mas comunes:

ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

"""

# Task 4.2
try:
    num_1 = 7
    num_2 = 0
    print(num_1 / num_2)
    print("Calculo hecho")

# Cuando salta la excepcion "ZeroDivisionError" se ejecutaria esta parte del codigo.
except ZeroDivisionError:
    print("Ha ocurrido un error")
    print("Debido a una division por cero")

# Puede haber tantos "except" como queramos y se pueden ver varios errores a la vez separandolos con ",".
except (ValueError, TypeError):
    print("Ha ocurrido un error")


try:
    x = "Hola"
    y = 2
    print(x + y)
    print("No way")

# Se puede hacer un "except" general para todos los tipos de excepciones.
except:
    print("Ha habido un error")

# El "finally" siempre se ejecuta aunque se haya encontrado alguna excepcion.
finally:
    print(x)
    print("Esto siempre se ejecuta")


# Task 4.4

"""
"raise" se utiliza para hacer saltar una excepcion manualmente.

print(1)
raise ValueError("Error en los valores.")
print(2)
"""


"""
En este caso raise mostraria la excepcion con el nombre especifico "ZeroDivisionError"

try:
   num = 5 / 0
except:
   print("An error occurred")
   raise

"""


# Task 4.5

print(1)

# Los "assert" comprueban algo y si devuelve false hara saltar una excepcion y se dejaria de ejecutar el codigo.
# Se suele utilizar al principio y al final de funciones para comprobar que no hay errores con valores validos
assert 1 + 1 == 2
print(2)

"""
Si metemos un segundo elemento en un "assert" se introducira como mensaje de la excepcion.

x = -10
assert(x > 0), "Es menor que 0"
"""


# Task 4.6

# Lo primero el nombre del archivo y lo segundo el permiso.
archivo = open("test.txt", "r")
archivo.close()


# Task 4.7

file = open("test.txt", "r")
cont = file.read()      # Permite leer lo que hay dentro del archivo.
print(cont)
file.close()


file2 = open("test.txt", "r")
print(file2.read(2))        # Lee los 2 primeros bytes del archivo.
print(file2.read(7))        # Lee los siguientes 7 bytes del archivo.
file2.close()

# Si se intenta leer cuando el archivo esta vacio o ya se ha mostrado todo aparecera una lista vacia.


# Metodos para leer todas las lineas de un archivo.

# Medodo 1
file3 = open("test.txt", "r")
print(file3.readlines())
file3.close


# Metodo 2
file4 = open("test.txt", "r")

for line in file4:
    print(line)

file4.close()


# Task 4.8

# Entra con permiso de escritura y, si no existiera el archivo seleccionado lo crearia.
file5 = open("test.txt", "w")
file5.write("This has been added.")         # Añade el String al archivo.
file5.close()

file5 = open("test.txt", "w")
# Sobreescribe lo que haya en el archivo.
file5.write("This has been changed")
file5.close()

file5 = open("test.txt", "r")
print(file5.read())
file5.close()


msg = "Number of changed characters"
file6 = open("test.txt", "w")
# Devuelve el numero de bytes modificados.
amount = file6.write(msg)
print(amount)
file6.close()


# Task 4.9

# Al hacer un try-finally nos aseguramos de que el archivo se cierra aunque ocurra alguna excepcion.
try:
    f = open("test.txt")
    print(f.read())

finally:
    f.close()


# Tambien se puede utilizar el "with", que nos asegura que en el momento que el "with" termine se cerrara el archivo independientente de lo que ocurra.
with open("test.txt") as f:
    print(f.read())
