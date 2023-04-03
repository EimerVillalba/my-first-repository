datos = {}

while True:
    nit = input("Ingrese el número del NIT (o 'q' para salir): ")
    if nit == 'q':
        break

    datos[nit] = {
        "nombre": input("Ingrese el nombre: "),
        "direccion": input("Ingrese la dirección: "),
        "celular": input("Ingrese el celular: "),
        "correo": input("Ingrese el correo: ")
    }

    print("NIT\tNombre\t\tDirección\tCelular\t\tCorreo")
    for nit, info in datos.items():
        print(f"{nit}\t{info['nombre']}\t\t{info['direccion']}\t\t{info['celular']}\t\t{info['correo']}")
