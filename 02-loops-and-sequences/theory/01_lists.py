cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0]) # Los Angeles
print(cities[-1]) # Tokyo

'''
Otra forma de crear una lista es utilizando 
el constructor list()
'''
name = 'Gian'
print(list(name)) # ['G', 'i', 'a', 'n']

print(len(name)) # 4

# Para actualizar un valor en un índice específico
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

# Para eliminar un elemento de una lista Todo: del
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

# Para comprobar si existe un elemento
exist_Rust = 'Rust' in programming_languages
exist_JavaScript = 'JavaScript' in programming_languages

print(f'Existe Rust en la lista? {exist_Rust}')
print(f'Existe JavaScript en la lista? {exist_JavaScript}')

# Lista anidadas
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2]) # ['Python', 'Rust', 'C++']
print(developer[2][1]) # Rust

# Desempaquetar valores de una lista
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # Alice
print(age) # 34
print(job) # Rust Developer


# *rest para recopilar los elementos restantes
name, *rest = developer
print(name) # Alice
print(rest) # [34, 'Rust Developer']

# Operador de segmentación ( : )
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # ['Cookies', 'Ice Cream', 'Pie']

# Si quisieras extraer una lista de solo números pares
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2]) # [2, 4, 6]