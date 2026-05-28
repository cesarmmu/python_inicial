#opcion 1 importar todo el fichero
# import lib.funciones as fn
#opcion 2 importar solo lo que necesito
from lib.funciones import sumar

def init():
    print('Estamos en el modulo principal')  
    print(sumar(1,2))
    
if __name__ == "__main__":
    init() 