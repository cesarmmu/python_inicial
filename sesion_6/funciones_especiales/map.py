# funcion de mapeo lo que hace es aplicar a cada elemento de la lista la misma operación o acción

numeros = [1,2,3,4,5,6]


# def obtener_lista_dobles(p):
#     for num in numeros:
#         num = num * p
#         dobles.append(num)
#     return dobles

# print(obtener_lista_dobles(6)  )  

dobles = list(map(lambda numero: numero*2, numeros))
triples = list(map(lambda numero: numero*3, numeros))
print(triples)

ciudades = ['madrid', 'BarCelona', 'VaLLadolID', 'SeVIlla']
# convertir todo el lista a mayusculas


# for ciudad in ciudades:
#     lista_mayusculas.append(ciudad.upper())
    
# print(lista_mayusculas)
lista_mayusculas = list(map(lambda ciudad: ciudad.upper(), ciudades))
print(lista_mayusculas)