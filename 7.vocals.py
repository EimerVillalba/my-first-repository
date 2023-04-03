#vocale
vocals = ['a', 'e','i' ,'o' ,'u']

#ingreso de palabra
input_word = input('ingresa una palabra => ')

#contador
counter = 0

#ciclo para ver cuantas vocales hay dentro de la lista
for letra in input_word:
    if letra.lower() in vocals:
        counter += 1

print('la palabra', input_word, ' tiene ', counter, ' vocales')