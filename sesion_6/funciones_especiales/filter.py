lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares = []
for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print(pares)

# filter es un funcion corta que aplica una lambda o tambien llamada función de condicion, sobre una lista concreta

impares = list(filter(lambda numero: numero % 2 != 0, lista_numeros))
print(impares)

productos = [
    {
        'id': 1,
        'titulo': 'Leche desnatada',
        'precio': 0.56,
        'cantidad': 3,
        'stock': True
    },
    {
        'id': 2,
        'titulo': 'Carne',
        'precio': 4.25,
        'cantidad': 1,
        'stock': False
    },
    {
        'id': 3,
        'titulo': 'Pan',
        'precio': 0.30,
        'cantidad': 6,
        'stock': True
    },
    {
        'id': 4,
        'titulo': 'Huevos',
        'precio': 2,
        'cantidad': 3,
        'stock': True
    },
    {
        'id': 5,
        'titulo': 'Cereales',
        'precio': 3.15,
        'cantidad': 1,
        'stock': False
    }
]


# quiero obtener aquellos productos que tienen stock

def getStock(lista, valor_stock):
    lista_resultante = []
    for producto in lista:
        if producto['stock'] == valor_stock:
           lista_resultante.append(producto)
    print(lista_resultante)

getStock(productos, True)

print('-' * 40)

def getStock2(lista, valor_stock):
    return (list(filter(lambda producto: producto['stock'] == valor_stock, lista)))

lista_sin_stock = getStock2(productos, False)
lista_con_stock = getStock2(productos, True)