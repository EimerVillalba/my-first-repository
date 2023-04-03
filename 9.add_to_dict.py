dict = {}

count_elements = int(input('ingresa el número de productos que queires agregar => '))
counter = 0

while counter < count_elements:
    element = input(f'ingresa el producto # {counter + 1} => ')
    value = int(input('ingresa el valor del producto => '))
    dict[element] = value
    counter += 1

    
print(dict)