def sumar(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    print(suma)
    
    
sumar(1,2,3,4,5)

# kargs

def presentar(nombre, edad):
    print(f"me llamo {nombre} y tengo {edad} años")
    

presentar('Juan', 44)
persona = {'nombre': 'Maria', 'edad': 23}
presentar(**persona)