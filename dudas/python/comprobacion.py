numero = input('Dime un numero: ')

if numero.isdigit():
    numero = int(numero)
else:
    print('no es un numero')

print(numero)