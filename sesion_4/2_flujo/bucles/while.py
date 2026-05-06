# mientras que se cumpla una condicion no salgo del bucles. Es mas versatil, pero puede darse con mayor media una indeterminación, es decir un bucle infinito

numero = 1

while numero <= 10:
    print(numero)
    numero += 2
else:
    print('he terminado cuando llego al final iteración')