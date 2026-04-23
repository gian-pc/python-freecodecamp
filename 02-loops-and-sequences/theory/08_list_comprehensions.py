
even_numbers = []
for num in range(10):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers) # [0, 2, 4, 6, 8]

# Ahora utilizando List Comprehensions
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Otro ejemplo
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result) # [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# todo: funcion filter() --> acepta una función y un iterable como argumentos
# Otra forma de crear una lista a partir de un iterable existente es mediante la función filter()
# La función filter() se utiliza para seleccionar elementos de un iterable que cumplan una condición específica.

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

# todo: funcion map() --> acepta una función y un iterable como argumentos
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]


# todo: función sum() -->  Esta función se utiliza para obtener la suma de un iterable como una lista o una tupla
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

## Ambos producen los mismos resultados, solo que uno es más explícito que otro
# start
numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60

# start como palabra clave
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60