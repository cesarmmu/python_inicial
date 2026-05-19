def sumar():
    error = False
    try:
        numero1 = int(input('dime un número: '))
        numero2 = int(input('dime otro número: '))
    except ValueError:
        error = True
        print('El valor introducido no es un número')
    finally:
        #lanzar un acción da igual si vamos por el error o por el acierto.
        if error:
            sumar()
        else:
            resultado = numero1 + numero2
            print(resultado)
    

sumar()