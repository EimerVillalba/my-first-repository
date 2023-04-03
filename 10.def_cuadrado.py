def numbers():
    nbr = int(input('digita cuantos números quieres ingresar => '))
    numbers = {}
    for i in range(nbr):
        number = float(input(f'ingresa el {i + 1} número => '))
        potencia = number ** number
        potencia = int(potencia)
        numbers[number] = potencia
    
    print(numbers)

        
numbers()
    
