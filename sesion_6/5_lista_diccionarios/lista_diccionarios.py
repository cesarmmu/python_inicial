productos = [
    {
        'nombre': 'Leche desnatada',
        'precio': 2,
        'cantidad': 12
    },
    {
        'nombre': 'Cereales',
        'precio': 8,
        'cantidad': 2
    },
    {
        'nombre': 'Pescado',
        'precio': 22,
        'cantidad': 1
    },
]

#print( len(productos) )

#print(productos[0]) # diccionario completo
#print(productos[0]['nombre']) # leche


def pintar_lista(lista):
    if len(lista) == 0:
        print('No hay resultados')
        return 
    for producto in lista:
        print('-' * 30)
        print(f"{producto['nombre']} => precio: {producto['precio'] * producto['cantidad']} euros")
    
    

#pintar_lista(productos)

# añadais tres productos a lista, y filtreis una lista con todo los producto cuya cantidad se mayor que 0.

def add_product(name_product, price, quantity, lista):
    # necesito crear un diccionario con el nuevo producto. Y tengo que añadirlo a la lista principal
    nuevo_producto = {
        'nombre': name_product,
        'precio': price,
        'cantidad': quantity
    }
    lista.append(nuevo_producto)
    pintar_lista(lista)

# nombre = input('Dime el nombre del producto: ') 
# precio = float(input('Dime el precio: '))
# cantidad = int(input('Dime un cantidad: '))
# add_product(nombre, precio, cantidad, productos)


def filtrar_por_cantidad(lista, cantidadmin, cantidadmax): 
    lista_filtrada= []
    for producto in lista:
        if producto['cantidad'] >= cantidadmin and producto['cantidad'] <= cantidadmax: 
            lista_filtrada.append(producto)
    return lista_filtrada

lista_resultante1 = filtrar_por_cantidad(productos, 0, 2)
lista_resultante2 = filtrar_por_cantidad(productos, 10, 20)
lista_resultante3 = filtrar_por_cantidad(productos, 20, 30)
pintar_lista(lista_resultante1)