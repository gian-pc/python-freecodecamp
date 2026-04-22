# Tuplas
'''
¿Cuándo se puede usar una tupla en lugar de una lista?

Si necesitas una colección dinámica de elementos donde puedas agregar,
eliminar y actualizar elementos, entonces debes usar una lista.
Si sabes que estás trabajando con una colección de datos fija e inmutable,
entonces debes usar una tupla.
'''

developer = ('Gian', 42,  'Go Developer')
print(developer)

# Intentando modificar una TUPLA --> Esto generará un TypeError
programming_languages = ('Python', 'Java', 'C++', 'Rust')
# programming_languages[0] = 'JavaScript' --> Esto genera un Error

# Accediendo a un elemento de una Tupla
print(developer[1]) # 42

# Accediendo a elementos comenzando desde el final
numbers = (1, 2, 3, 4, 5)
print(numbers[-2]) # 4

# Otra forma de crear una TUPLA --> tuple()
developer = 'Gian'
print(tuple(developer)) # ('G', 'i', 'a', 'n')

# Para comprobar si un elemento esta en una tupla usamos --> in
is_rust = 'Rust' in programming_languages
print(is_rust) # True

# Extraer elementos de una tupla
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer
print(name) # Alice
print(age) # 34
print(job) # Rust Developer

# Para elementos restantes de una tupla puedes usar el operador *
name, *rest = developer

print(name) # Alice
print(rest) # [34, 'Rust Developer']

# Para Extraer un segmento de una tupla
desserts = ['Cake', 'pie', 'coookies', 'ice cream']
print(desserts[1:3]) # ['pie', 'coookies']

# Eliminar un elemento de una lista --> Esto no será posible porque las tuplas son inmutables
developer = ('Jane Doe', 23, 'Python Developer')
# del developer[1] --> Esto genera un TypeError
