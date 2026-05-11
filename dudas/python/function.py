def solo_posicion(x, /):
    print(x)
    
    
def solo_nombre(*, y):
    print(y)
    
    
solo_posicion(10)
#solo_posicion(x=20) incorrecto

solo_nombre(y=12)
#solo_nombre(12) incorrecto


def sumar(x,y):
    print(x,y)
    
    
sumar(y=1,x=2)