cantidad = 10

for i in range(cantidad):
    print(f'Hola {i}' )
else:
    print('he terminado el bucle')
    
print('-' * 30)

for i in range(2, cantidad):
     print(f'Adios {i}' )
     
print('-' * 30)

for i in range(3, cantidad, 3):
    print(f'hasta luego {i}')
    
print('-'* 30)

suma = 0
for i in range(1, 11):
    suma += i
print(suma)