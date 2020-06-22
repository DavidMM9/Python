

# Task 3.2

def my_func():
    print("Hello")
    print("World")


my_func()


# Task 3.3

def print_with_exclamation(word, word1):
    print(word + ", " + word1 + "!")


print_with_exclamation("Hello", "World")
print_with_exclamation("World", "Hello")


# El argumento entrante de la funcion se puede utilizar como dentro de la funcion pero no fuera de ella.
def function(variable):
    variable += 1
    print(variable)


function(7)         # Si pusiera "print(variable)" daria un error.


# Task 3.4

def min(x, y):
    if(x < y):
        return x
        # Cuando se hace un return no se ejecuta el resto del codigo.
        print("This won't be printed")
    else:
        return y        # Los return solo pueden ir dentro de una funcion.


print(min(4, 6))
z = min(9, 5)
print(z)


# Task 3.6

def funcion(x):
    print(x)


# Se puede asignar a otro nombre de variables las funciones.
nombre = funcion
nombre(2)


#####################################


def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10

print(do_twice(add, a, b))


# Task 3.7

# Si intentas importar un modulo que no es valido saltara un error.
import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)


from math import pi, sqrt

print(pi)
print(sqrt(100))

# Renombra el objeto que estas importando.
from math import sqrt as sqrt_user

print(sqrt_user(100))
