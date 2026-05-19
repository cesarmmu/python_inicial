# funciones lambda es una funcion abreviada

# funcion que reciba un nombre y un apellido y devuelva el nombre completo
# Juan Antonio, Perez => Juan Antonio Perez


def getNameComplete(name, surname):
    return f'{name} {surname}'

nombre_completo = getNameComplete('Juan Antonio', 'Perez')
print(nombre_completo)


getNameCompleteLambda = lambda name, surname: f'{name} {surname}'

nombre_completo2 = getNameCompleteLambda('Pilar', 'Martinez')
print(nombre_completo2)