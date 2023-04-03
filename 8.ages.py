'''#diccionario vacío
estudents = {}

#contador de cuantas notas quiere ingresar
counter_estudentes = int(input('ingresa el número de notas que quieres calcular => '))
print('\n')

#contador de estudiante
estudents = 0

#ciclo
for i in range(counter):
    estudents += 1
    print(f"estudiante # {estudents}")
    print('*' * 40)
    estudent = input('ingresa el nombre => ')
    rating = float(input('ingresa su nota => '))    
    ratings[estudent] = rating
    print('\n')


print(ratings)'''

# Crear un diccionario vacío para almacenar información de estudiantes
estudiantes = {}

# Solicitar al usuario que ingrese el número de estudiantes a agregar
num_estudiantes = int(input("¿Cuántos estudiantes quieres agregar? "))

# Repetir el proceso de agregar información para cada estudiante
for i in range(num_estudiantes):
    # Solicitar al usuario que ingrese el nombre del estudiante
    nombre = input(f"Ingrese el n            ombre del estudiante: {i + 1} ")
    
    # Crear un diccionario vacío para almacenar información de materias y calificaciones
    materias_calificaciones = {}
    
    # Solicitar al usuario que ingrese el número de materias y calificaciones a agregar
    num_materias = int(input(f"¿Cuántas materias y calificaciones quieres agregar para {nombre}? "))
    
    # Repetir el proceso de agregar información de materia y calificación para cada materia
    for j in range(num_materias):
        # Solicitar al usuario que ingrese el nombre de la materia
        materia = input(f"Ingrese el nombre de la materia #{j+1}: ")
        
        # Solicitar al usuario que ingrese la calificación de la materia
        calificacion = float(input(f"Ingrese la calificación de la materia #{j+1}: "))
        
        # Agregar la materia y la calificación al diccionario de materias y calificaciones
        materias_calificaciones[materia] = calificacion
    
    # Agregar el diccionario de materias y calificaciones al diccionario del estudiante
    estudiantes[nombre] = materias_calificaciones

# Calcular el promedio de las calificaciones de todas las materias de todos los estudiantes
total_calificaciones = 0
num_calificaciones = 0
for estudiante in estudiantes.values():
    for calificacion in estudiante.values():
        total_calificaciones += calificacion
        num_calificaciones += 1
promedio = total_calificaciones / num_calificaciones

# Imprimir la información de todos los estudiantes y el promedio de calificaciones
print(f"\nInformación de todos los estudiantes:\n{estudiantes}\n")
print(f"Promedio de calificaciones: {promedio}")
