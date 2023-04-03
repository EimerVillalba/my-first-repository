

palabra = input('Ingresa una palabra => ')

#invirtiendo la palabra

rev = palabra[::-1]

if palabra == rev:
    print('la palabra ', palabra, ' es un palindromo')

else:
    print('la palabra ', palabra, ' no es un palindromo por que quedaría desigual: ', rev)


# FUNCIÓN REV = REVERSED