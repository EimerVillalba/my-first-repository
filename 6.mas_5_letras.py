palabras = []
counter= 1

while counter <= 5:
    palabra = input('ingresa una palabra => ')
    palabras.append(palabra)
    counter += 1
    
for palabra in palabras:
    if len(palabra) > 5:
        print(palabra)