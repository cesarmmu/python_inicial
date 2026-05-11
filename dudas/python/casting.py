numero = 13
numero_2 = float(numero) # 13.0
print(numero, numero_2)

try:
    numero = float('a')
    numero = float(input('dime un numero: '))
except ValueError:
    print('no convertir a racional una letra')
    
    
    
numero_racional = int(12.3)
print(numero_racional)
