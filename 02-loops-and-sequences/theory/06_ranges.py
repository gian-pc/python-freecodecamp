# Rangos

# todo: sintaxis basica
# range(start, stop, step) --> stop es el único argumento requerido

for num in range(3): # solo tiene stop
    print(num) # 0 1 2

# ahora con start y stop
for num in range(1, 5):
    print(num) # 1 2 3 4

# ahora con start, stop, step
for num in range(2, 11, 2):
    print(num) # 2 4 6 8 10

# en orden decreciente
for num in range(40, 0, -10):
    print(num) # 40 30 20 10

# también podemos crear una lista de enteros con la función range()
numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]