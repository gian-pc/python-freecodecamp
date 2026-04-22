# Métodos más comunes para trabajar con tuplas

#todo: count() --> cuantas veces aparece un elemento en una tupla
programming_languages = ['Python', 'Ruby', 'Java', 'Scala', 'Python']
print(programming_languages.count('Python')) # 2
print(programming_languages.count('Php')) # 0
# print(programming_languages.count()) --> sino se pasa el argumento se genera un TypeError

#todo: index() --> encuentra el indice donde se encuentra un elemento
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.index('Java')) # 1

# si no se encuentra el elemento genera un ValueError
# print(programming_languages.index('JavaScript'))

# pasar índices de busqueda de inicio y fin
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3)) # 5

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5)) # 2

#todo: sorted() --> devuelve una nueva lista con los valores ordenados
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers)) # [2, 3, 7, 13, 18, 45, 67, 78]

# ordenamos en función de su longitud de caracteres con todo: key
letters = ('abc', 'cb', 'P', 'xyzu', 'abcda')
print(sorted(letters, key=len)) # ['P', 'cb', 'abc', 'xyzu', 'abcda']

# Ordenamos de forma inversa
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True)) # ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']