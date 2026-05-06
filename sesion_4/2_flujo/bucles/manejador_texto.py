texto = 'Juan Antonio'

# longitud
print( len(texto) ) # 12
print( texto[5] ) # A

# partir la cadena de caracteres
print( texto[5:12] )

# ana 3 => 0 - 2
for i in range(len(texto)):
    print( texto[i] )
    
# for in 
otro_texto = 'en un lugar de la mancha'

for caracter in otro_texto:
    print(caracter)
    
# convertir una frase a mayusculas
frase = 'Los viajéros llegarán a la ciudad mañana'
print( frase.upper() )

# quitarle los acentos
sin_acentos = ""
for caracter in frase:
    if caracter == 'á' or caracter == 'Á':
        sin_acentos += 'a'
    elif caracter == 'é' or caracter == 'é':
        sin_acentos += 'e'
    else:
        sin_acentos += caracter

print(sin_acentos)
