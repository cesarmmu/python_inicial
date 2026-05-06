# pido un numero por pantalla quiero que me escriba los tres primeros numeros que sean divisible por el numero pedido
# numero = 3 => 3,6,9,

numero = int(input('Dime un numero: '))
contador = 3

for i in range (1, 12):
    if i % numero == 0:
        print(i)
        contador -= 1
        
    if contador == 0:
        break
else:
    print('He terminado')
    
print('--------')
    
# pintar solo los numeros pares entre 1 - 100
for i in range (1, 100):    
    if i % 2 != 0:
        # me salto los impares
        continue
    # pinto los pares.
    print(i)
else: 
    print('terminados')

