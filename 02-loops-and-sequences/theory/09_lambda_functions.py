# antes definiamos funciones con def
def square(num):
    return num ** 2

print(square(4)) # 16

# Pero cuando se trata de trabajar con funciones de orden superior como map()y filter(),
# puedes usar una función anónima en línea. Aquí es donde entran en juego las funciones lambda.
numbers = [1, 2, 3, 4, 5]

# como sabemos filter recibe 2 argumentos, una función y un iterable
# y en este caso la función es una función lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# todo: Al trabajar con funciones lambda, es importante conocer las mejores prácticas.
#  Por ejemplo, no es una buena práctica asignar una función lambda a una variable de esta manera:
numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

# Esto anula el propósito de usar funciones anónimas.
# En este caso, deberías usar una función normal