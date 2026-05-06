def sumar(*numeros):
    #print(len(numeros))
    suma = 0
    for numero in numeros:
        suma += numero
    print(suma)
    
sumar(2,3)
sumar(2,3,65)
sumar(3,5,7,9,5)

# un conjunto de lo que sea empieza en la posicion 0 y acabe en la posicion n-1 siendo n la longitud del conjunto