numero1 = 12
numero2 = 23

# parametros obligatorios, parametros optativos. Primero van todos los obligatorios y luego todos los optativos
def sumar(numero1, numero2=10):
    resultado = numero1 + numero2
    print(resultado)
    
    
sumar(15,5)
sumar( numero1, numero2 )
sumar( 1 )
