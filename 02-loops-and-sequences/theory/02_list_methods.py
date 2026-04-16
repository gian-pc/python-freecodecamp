"""
Metodos más comunes usados en una lista

    append()
    extend()
    insert(a, b)
    remove()
    pop()
    clear()
    sort()
    sorted()
    reverse()
    index()

"""
numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

# Agregamos una lista a otra lista
even_numbers = [2,4,6,8]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, [2, 4, 6, 8]]

# Pero si quiero agregar los numeros individuales usa el metodo extend()
letters = ['a', 'b', 'c']
new_letters = ['x', 'y', 'z']
letters.extend(new_letters)
print(letters) # ['a', 'b', 'c', 'x', 'y', 'z']

# insert()
letters.insert(1, 4)
print(letters) # ['a', 4, 'b', 'c', 'x', 'y', 'z']

# remove() -> solo elimina el primero que se repite
numbers_2 = [1, 2, 3, 4, 5, 5, 5]
numbers_2.remove(5)
print(numbers_2) # [1, 2, 3, 4, 5, 5]

# pop() -> elimina un elemento de un índice específico
numbers_3 = [1, 2, 3, 4, 5]
res_numbers_3 = numbers_3.pop(3)
print(res_numbers_3) # 4

# pop() -> sin indice elimina el último
res_numbers_3 = numbers_3.pop()
print(res_numbers_3) # 5

# clear() -> para vaciar una []
numbers_3.clear()
print(numbers_3) # []

# sort() -> ordena los elementos in situ
numbers_4 = [3, 1, 5, 2, 4]
numbers_4.sort()
print(numbers_4) # [1, 2, 3, 4, 5]

# sorted() -> ordena y devuelve una nueva lista
sorted_numbers_4 = sorted(numbers_4)
print(sorted_numbers_4) # [1, 2, 3, 4, 5]

# reverse() -> invierte el orden de sus elementos
numbers_5 = [3, 2, 1]
numbers_5.reverse()
print(numbers_5) # [1, 2, 3]

# index()
programming_languages = ['Rust', 'Java', 'Python', 'C++']

print(programming_languages.index('Python')) # 2