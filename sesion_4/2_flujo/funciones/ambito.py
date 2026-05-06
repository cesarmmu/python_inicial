cantidad = 10 # global

# ambito funcional, cualquier variable creada dentro de una función es ambito local, es decir solo existe dentro de esa funcion


def calcular_pvp(precio, cantidad, impuesto):
    coste = precio * cantidad
    iva = (coste  * impuesto ) / 100
    pvp = coste + iva # local variable
    return pvp
    # despues return salimos de la funcion

mi_pvp = calcular_pvp(100, cantidad, 21)

print(mi_pvp)


