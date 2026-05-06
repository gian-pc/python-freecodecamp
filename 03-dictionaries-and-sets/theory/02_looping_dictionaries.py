
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# iterando sobre los valores
for price in products.values():
    print(price)

# iterando sobre los keys
for product in products.keys():
    print(product)

# iterando sobre keys y valores
for product in products.items():
    print(product)

# almacenando las keys y valores en variables separadas
for product, price in products.items():
    print(product, price)

# aplicando un descuento del 20% al precio del producto
for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

# --------------  enumerate  -----------------
# la función enumerate asigna un número a cada par clave valor
for product in enumerate(products):
    print(product)

# también se puede asignar valores a variables separadas
for index, product in enumerate(products):
    print(index, product)

# iterando sobre los valores
for price in enumerate(products.values()):
    print(price)

# también puedes asignarle a variables separadas
for index, price in enumerate(products.values()):
    print(index, price)

# ahora con items()
for index, product in enumerate(products.items()):
    print(index, product)