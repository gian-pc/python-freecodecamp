# funciones Enumerate y Zip
'''
 todo: Esta función enumerate() mantiene un registro del índice de un iterable
 todo: y devuelve un objeto enumerado.
'''

languages = ['Spanish', 'English', 'Russian', 'Chinese']

# todo: forma tradicional con un index y un for
index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

# todo: usando la función enumerate()
print(list(enumerate(languages))) # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# todo: utilizando la función enumerate() y extraemos su indice y el valor de la lista
for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

# todo: ahora le agregamos un parámetro opcional start valor de inicio de conteo del indice en este caso 1
for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

# Pero, ¿qué ocurre si necesitas iterar sobre varios iterables en paralelo?
# todo: función zip()
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids))) # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# y ahora con un for
for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')





