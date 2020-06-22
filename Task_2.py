# Task 2.2

x = 10
if x <= 20:
    print("Hello World")
    if x != 100:
        print("Hey World")


# Task 2.3

x = 10
if x <= 5:
    print("Hello World")

elif x <= 8:
    print("Hey World")

else:
    print("Bye World")


#  Task 2.4

if (1 == 1) and (2 == 3):  # Igual con el 'or'
    print("No tiene pinta")

else:
    print("Muy bien")

x = True
print(not x)  # El 'not' cambia de True a False y viceversa


# Task 2.5

# El '==' tiene mayor prioridad frente al 'and'.


# Task 2.6

i = 1
x = 3

while i <= 10:
    print(i + x)
    i = i + 1

    if i == 3:
        print("Vuelve al bucle")
        continue  # 'Continue' devuelve al principio del bucle

    if i >= 3:
        print("Rompe el bucle")
        break  # 'Break' sale del bucle

print("Fin bucle")


# Task 2.7

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)


number = 3
things = ["String", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][1])

str = "Hello world"
print(str[6])       # El String funciona como una lista.


# Task 2.8

lista = [4, 4, 4]
lista[1] = 8
print(lista)
print(lista + [5, 5, 5])        # Se le suma a la lista la otra lista.
print(lista * 3)
print(4 in lista)               # Se mira si el número está en la lista.
print(6 in lista)
print(4 not in lista)           # Se mira si el número no está en la lista.
print(6 not in lista)


# Task 2.9       IMPORTANTE!!

lista_2 = [1, 2, 3]
lista_2.append(4)               # Se añade lo de dentro al final de la lista.
print(lista_2)
print(len(lista_2))             # Muestra la longitud de la lista.

# Muestra la posición de la primera vez que aparece el elemento.
print(lista_2.index(2))

# Muestra el número con mayor valor de la lista.
print(max(lista_2))

# Muestra el número con mayor valor de la lista.
print(min(lista_2))

# Muestra las veces que aparece un elemento en la lista.
print(lista_2.count(1))

lista_2.remove(3)               # Borra el elemento de la lista.
print(lista_2)
lista_2.reverse()               # Cambia el orden de los elementos de la lista.
print(lista_2)

words = ["Python", "Fun"]
index = 1

# Inserta un elemento en la lista en la posición seleccionada.
words.insert(index, "is")

print(words)


# Task 2.10

numbers = list(range(10))       # Crea una lista de los elementos de 0 hasta 9.
print(numbers)

# Crea una lista con los elementos de 2 hasta 6 con saltos de 2 en 2.
numbers = list(range(2, 7, 2))

print(numbers)
print(range(0, 5) == range(5))


# Task 2.11

words = ["How", "Are", "You", "World"]
counter = 0
max_value = len(words)

while counter < max_value:
    word = words[counter]
    print(word + "?")
    counter += 1


words = ["How", "Are", "You", "World"]
for x in words:                             # Es equivalente al while anterior.
    print(x + "?")


for x in range(5):
    print("Hey")


# Task 2.12                         PRIMER SEMI-PROYECTO (CALCULADORA)

while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break

    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
        continue
