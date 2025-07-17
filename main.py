# main.py

from clases import Estudiante, Becado
from funciones import generar_reporte

estudiantes = []

def mostrar_menu():
    print("=== Mini Sistema Académico ===")
    print("1. Registrar Estudiante")
    print("2. Mostrar Todos los Estudiantes")
    print("3. Generar Reporte Estadístico")
    print("4. Salir")

def ejecutar_accion(opcion):
    if opcion == "1":
        # Llamar a la función para registrar estudiante
        registrar_estudiante()
    elif opcion == "2":
        # Mostrar todos los estudiantes
        mostrar_estudiantes()
    elif opcion == "3":
        # Llamar a la función para generar el reporte
        generar_reporte(estudiantes)
    elif opcion == "4":
        print("¡Hasta luego!")
        return False
    return True

def registrar_estudiante():
    print("=== Registrar Estudiante ===")
    
    # Solicitar datos al usuario
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))
    carrera = input("Carrera del estudiante: ")
    
    # Solicitar las notas
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Ingrese la nota {i}: "))
        notas.append(nota)
    
    # Preguntar si tiene beca
    beca = input("¿Tiene beca? (sí/no): ").strip().lower()
    tiene_beca = beca == 'sí'
    
    # Crear el objeto Estudiante (o Becado)
    if tiene_beca:
        tipo_beca = input("Tipo de beca: ")
        estudiante = Becado(nombre, edad, carrera, notas, tiene_beca, tipo_beca)
    else:
        estudiante = Estudiante(nombre, edad, carrera, notas, tiene_beca)
    
    # Agregar el estudiante a la lista
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito.")


def mostrar_estudiantes():
    print("=== Estudiantes Registrados ===")
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    # Mostrar todos los estudiantes
    for estudiante in estudiantes:
        print(estudiante.mostrar_datos())


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if not ejecutar_accion(opcion):
            break
