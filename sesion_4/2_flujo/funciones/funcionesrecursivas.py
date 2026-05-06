# Funcion recursiva es un funcion que se llama si misma. Es como hacer un bucle

def pedir_numero():
    numero = input('Dime un numero: ')
    if not numero.isdigit():
        print('esto no es un numero, prueba otra vez')
        pedir_numero()
    numero = int(numero)
    print( numero * 2 )
    
pedir_numero()


def main():
    menu = """## bienvenido a mi app
[1].saluda
[2].despidete
[3].salir
"""
    print(menu)
    option = input('dime que opcion necesitas: ')
    if option == '1':
        print('Hola como estan los maquinas')
        main()
    elif option == '2':
        print('Hasta luego MariCarmen')
    elif option == '3':
        print('hasta pronto')
    else: 
        print('opcion no valida')
        main()
    
    
main()