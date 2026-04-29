# diccionarios
# son estructuras de datos que almacenan colecciones de pares clave:valor
dictionary = {
    'key1': 'value1',
    'key2': 'value2'
}

print(dictionary)

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# Utilizando el constructor dict()
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
print(pizza)

# Para acceder al valor de name
print(pizza['name']) # Margherita Pizza

# Asignando un nuevo valor
pizza['name'] = 'Margherita'
print(pizza['name']) # Margherita

# Metodo get() recupera el valor asociado a una clave
# es similar a la notacion de corchete
# con la diferencia que te permite pasar un parametro por defecto
# en el caso de que no se encuentre esa clave,
# devolvera el parametro por defecto en este caso []
res = pizza.get('toppings', [])
print(res) # ['mozzarella', 'basil']

res2 = pizza.get('toppings2', []) # no existe 'topping2'
print(res2) # []

# Los métodos .keys() y .values() devuelven un objeto de vista
# con todas las claves y valores del diccionario, respectivamente:
keys = pizza.keys()
print(keys) # dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])

values = pizza.values()
print(values) # dict_values(['Margherita', 8.9, 250, ['mozzarella', 'basil']])

# El metodo .items() devuelve un objeto de vista con todos los pares clave-valor del diccionario,
# incluyendo tanto las claves como los valores:
items = pizza.items()
print(items) # dict_items([('name', 'Margherita'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# Este metodo .clear() elimina todos los pares clave-valor del diccionario:
#pizza.clear()
print(pizza) # {}

print(pizza.pop('price', 10))
print(pizza)
print(pizza.pop('total_price', 'No se encontró'))
print(pizza)

# Elimina el ultimo elemento
pizza.popitem()

print(pizza)

# update
pizza.update({ 'price': 15, 'total_time': 25 })
print(pizza)