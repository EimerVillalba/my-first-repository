counter = 1
import sys #sirve para finalizar el programa escribiendo (sys.exit())
clients_date = {}

while True:
    
    
    options = [1, 2, 3, 4, 5]
    counter += 1
    
    print('*' * 50)
    print('\n')
    print('            BASE DE DATOS DE CLIENTES')
    print('\n')
    print('*' * 50)
    
    if counter == 1:
        print('Bienvenido, Escoge una acción:')
    else:
        print('Escoge una acción:')
        
    select = input('''
1.añadir cliente
2.eliminar cliente 
3.mostrar cliente 
4.listar todos los clientes 
5.listar clientes preferentes

Escribe (exit) para salir

¿Que quieres hacer? (escribe el número) => ''')
        
    if select == 'exit':
        break
    
    select = int(select)
    
    if not select in options:
        print('\n')
        print('*' * 50)
        print('Opción incorrecta, fin del programa')
        break

    counter_next = 0  
    while select == 1:
        
        print('\n')
        print('*' * 50)
        print('     DATOS PARA EL CLIENTE NUEVO : ')
        preferential_input = input('¿El cliente es preferente? (S / N)\n => ' )
        preferential = preferential_input.upper() == 'S'
        nit = int(input('\nNIT => '))

        clients_date[nit] = {           
    "nombre": input("Nombre => "),
    "direccion": input("Dirección => "),
    "celular": int(input("Celular => ")),
    "correo": input("Correo => "),
    "preferente": preferential
}
        
        print('\nagregado\n')
        print('*' * 50)
        next = int(input('''\n    ELIJE UNA OPCIÓN
1. Agregar otro cliente
2. Salir al menú principal
3. Fin del programa

=> '''))
        options_next = (1,2,3)
        
        if not next in options_next:
            print('Opción incorrecta, fin del programa')
            break
        elif next == 2:
            break
        elif next == 3:
            sys.exit('Hasta luego...')
        
    
    while select == 2:
        print('\n')
        print('*' * 50)
        print('\n     ELIMINAR CLIENTE : ')
        
        delete_nit = int(input('Digíta el NIT del cliente a eliminar => '))
        
        if delete_nit in clients_date:
            
            print('\nListo! El cliente : ')
            print("NIT\tNombre\t\tDirección\tCelular\t\tCorreo")
            for nit, info in clients_date.items():
                print(f"{nit}\t{info['nombre']}\t\t{info['direccion']}\t\t{info['celular']}\t\t{info['correo']}\t\t{info['preferente']}")
            del clients_date[nit]
            print('\nHa sido eliminado de la base de datos :) ')
        else:
            print('El cliente a eliminar no se encuentra en la base de datos\n')
            
        print('\n')
        print('*' * 50)        
        next = int(input('''    ELIJE UNA OPCIÓN
1. Eliminar otro cliente
2. Salir al menú principal
3. Fin del programa

=> '''))
        options_next = (1,2,3)
        
        if not next in options_next:
            print('Opción incorrecta, fin del programa')
            break
        elif next == 1:
            counter_next +=1
        elif next == 2:
            break
        elif next == 3:
            sys.exit('Hasta luego...')
        
     
     
