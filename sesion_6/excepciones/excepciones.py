# pedir dos numeros y sumarlos.
def main():
    try:
        numero1 = int(input('Dime un numero: '))
        numero2 = int(input('Dime otro numero: '))

        resultado = numero1 / numero2
        print(resultado)
    except ValueError:
        print('es que no has metido un numero en los datos .....')
        main()
    except ZeroDivisionError:
        print('No se puede dividir por cero')
        main()
    except Exception as e:
        print(f'errorcito por usar windows {e}, pantallazo azul')



main() 
print('seguimos con nuestro programa')