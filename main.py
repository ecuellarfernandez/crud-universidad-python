from database import connection as conn
from database.queries import estudiantes, materias, inscripciones, notas
from colorama import Fore, Style
import re

def validar_fecha(fecha):
    # Esta función valida si la fecha está en el formato correcto (YYYY-MM-DD)
    return re.fullmatch(r'\d{4}-\d{2}-\d{2}', fecha) is not None

def main():
    while True:
        print("\nAplicación de Registro de Estudiantes")
        print("1. Registrar un nuevo estudiante")
        print("2. Ver la lista de estudiantes registrados")
        print("3. Ver las materias en las que está inscrito un estudiante específico")
        print("4. Calcular el promedio de notas de un estudiante en una materia específica")
        print("5. Actualizar la información de un estudiante")
        print("6. Actualizar la información de una materia")
        print("7. Eliminar un estudiante de la base de datos")
        print("8. Eliminar una materia de la base de datos")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            while True:
                nombre = ""
                while not nombre:
                    nombre = input(Fore.GREEN + "Ingrese el nombre del estudiante: " + Style.RESET_ALL)
                    if not nombre or not nombre.isalpha():
                        print("El nombre no puede estar vacío. Inténtelo de nuevo.")

                fecha_nacimiento = ""
                while not validar_fecha(fecha_nacimiento):
                    fecha_nacimiento = input(Fore.GREEN + "Ingrese la fecha de nacimiento (YYYY-MM-DD): " + Style.RESET_ALL)
                    if not validar_fecha(fecha_nacimiento):
                        print("La fecha de nacimiento no está en el formato correcto. Inténtelo de nuevo.")

                carrera = ""
                while not carrera:
                    carrera = input(Fore.GREEN + "Ingrese la carrera del estudiante: " + Style.RESET_ALL)
                    if not carrera:
                        print("La carrera no puede estar vacía. Inténtelo de nuevo.")

                break
            conn.execute_query(estudiantes.INSERT_STUDENT, (nombre, fecha_nacimiento, carrera))
            print(Fore.MAGENTA + "Estudiante registrado con éxito." + Style.RESET_ALL)
            pass

        elif opcion == '2':
            estudiantes_response = conn.execute_query(estudiantes.GET_ALL_STUDENTS)
            for est in estudiantes_response:
                print(Fore.BLUE, end="")
                print(est, end="")
                print(Style.RESET_ALL)
            pass

        elif opcion == '3':
            print("Estudiantes disponibles:")
            estudiantes_result = conn.execute_query(estudiantes.GET_ALL_STUDENTS)
            for estudiante in estudiantes_result:
                print(Fore.BLUE+f"ID: {estudiante[0]}, Nombre: {estudiante[1]}" + Style.RESET_ALL)  # Ajusta los índices según la estructura de tus datos

            estudiante_id = input(Fore.GREEN + "Ingrese el ID del estudiante: " + Style.RESET_ALL)
            result = conn.execute_query(materias.GET_SUBJECTS_BY_STUDENT, (estudiante_id,))

            #si no tiene materias inscritas
            if not result:
                print(Fore.YELLOW + "El estudiante no está inscrito en ninguna materia." + Style.RESET_ALL)
                continue

            for materia in result:
                print(Fore.BLUE, end="")
                print(materia, end="")
                print(Style.RESET_ALL)
            pass
        elif opcion == '4':
            while True:
                # Mostrar todos los estudiantes disponibles
                print("Estudiantes disponibles:")
                estudiantes_result = conn.execute_query(estudiantes.GET_ALL_STUDENTS)
                for estudiante in estudiantes_result:
                    print(Fore.BLUE + f"ID: {estudiante[0]}, Nombre: {estudiante[1]}" + Style.RESET_ALL)  # Ajusta los índices según la estructura de tus datos

                estudiante_id = input(Fore.GREEN + "Ingrese el ID del estudiante: " + Style.RESET_ALL)

                if estudiante_id is None:
                    break

                # Mostrar todas las materias disponibles para el estudiante seleccionado
                print("Materias disponibles para el estudiante seleccionado:")
                materias_result = conn.execute_query(materias.GET_SUBJECTS_BY_STUDENT, (estudiante_id,))
                if not materias_result:
                    print(Fore.YELLOW + "El estudiante no está inscrito en ninguna materia." + Style.RESET_ALL)
                    continue

                for materia in materias_result:
                    print(Fore.BLUE + f"ID: {materia[0]}, Nombre: {materia[1]}" + Style.RESET_ALL)  # Ajusta los índices según la estructura de tus datos

                materia_id = input(Fore.GREEN + "Ingrese el ID de la materia: " + Style.RESET_ALL)

                if materia_id is None:
                    break

                notas_result = conn.execute_query(notas.GET_AVERAGE_GRADE_BY_STUDENT_ID_SUBJECT_ID, (estudiante_id, materia_id))

                if not notas_result:
                    print(Fore.YELLOW + "No se encontraron notas para el estudiante en la materia especificada." + Style.RESET_ALL)
                    continue

                print(Fore.MAGENTA + f"El promedio de notas del estudiante en la materia es: {notas_result[0]}" + Style.RESET_ALL)
                break
            pass
        elif opcion == '5':
            # Mostrar todos los estudiantes disponibles
            print("Estudiantes disponibles:")
            estudiantes_result = conn.execute_query(estudiantes.GET_ALL_STUDENTS)
            for estudiante in estudiantes_result:
                print(Fore.BLUE + f"ID: {estudiante[0]}, Nombre: {estudiante[1]}" + Style.RESET_ALL)  # Ajusta los índices según la estructura de tus datos

            # Actualizar la información del estudiante
            estudiante_id = input(Fore.GREEN + "Ingrese el ID del estudiante que desea actualizar: " + Style.RESET_ALL)
            estudiante_actual = conn.execute_query(estudiantes.GET_STUDENT_BY_ID, (estudiante_id,))[0]

            nombre = input(Fore.GREEN + "Ingrese el nuevo nombre del estudiante (o '-' para mantener el actual): " + Style.RESET_ALL)
            nombre = estudiante_actual[1] if nombre == '-' else nombre

            fecha_nacimiento = input(Fore.GREEN + "Ingrese la nueva fecha de nacimiento (YYYY-MM-DD) (o '-' para mantener la actual): " + Style.RESET_ALL)
            fecha_nacimiento = estudiante_actual[2] if fecha_nacimiento == '-' else fecha_nacimiento

            carrera = input(Fore.GREEN + "Ingrese la nueva carrera del estudiante (o '-' para mantener la actual): " + Style.RESET_ALL)
            carrera = estudiante_actual[3] if carrera == '-' else carrera

            conn.execute_query(estudiantes.UPDATE_STUDENT, (nombre, fecha_nacimiento, carrera, estudiante_id))
            print(Fore.MAGENTA + "Información del estudiante actualizada con éxito." + Style.RESET_ALL)
            pass
        elif opcion == '6':
            # Mostrar todas las materias disponibles
            print("Materias disponibles:")
            materias_result = conn.execute_query(materias.GET_ALL_SUBJECTS)
            for materia in materias_result:
                print(Fore.BLUE + f"ID: {materia[0]}, Nombre: {materia[1]}" + Style.RESET_ALL)  # Ajusta los índices según la estructura de tus datos

            # Actualizar la información de la materia
            materia_id = input(Fore.GREEN + "Ingrese el ID de la materia que desea actualizar: " + Style.RESET_ALL)
            materia_actual = conn.execute_query(materias.GET_SUBJECT_BY_ID, (materia_id,))[0]

            codigo = input(Fore.GREEN + "Ingrese el nuevo código de la materia (o '-' para mantener el actual): " + Style.RESET_ALL)
            codigo = materia_actual[1] if codigo == '-' else codigo

            nombre = input(Fore.GREEN + "Ingrese el nuevo nombre de la materia (o '-' para mantener el actual): " + Style.RESET_ALL)
            nombre = materia_actual[2] if nombre == '-' else nombre

            creditos = input(Fore.GREEN + "Ingrese los nuevos créditos de la materia (o '-' para mantener el actual): " + Style.RESET_ALL)
            creditos = materia_actual[3] if creditos == '-' else creditos

            conn.execute_query(materias.UPDATE_SUBJECT, (codigo, nombre, creditos, materia_id))
            print(Fore.MAGENTA + "Información de la materia actualizada con éxito." + Style.RESET_ALL)
            pass
        elif opcion == '7':
            # Delete a student from the database
            print("Estudiantes disponibles:")
            estudiantes_result = conn.execute_query(estudiantes.GET_ALL_STUDENTS)
            for estudiante in estudiantes_result:
                print(Fore.BLUE + f"ID: {estudiante[0]}, Nombre: {estudiante[1]}" + Style.RESET_ALL)  # Adjust the indices according to your data structure

            estudiante_id = input(Fore.GREEN + "Ingrese el ID del estudiante que desea eliminar: " + Style.RESET_ALL)
            conn.execute_query(estudiantes.DELETE_STUDENT, (estudiante_id,))
            print(Fore.MAGENTA + "Estudiante eliminado con éxito." + Style.RESET_ALL)
            pass
        elif opcion == '8':
            # Delete a subject from the database
            print("Materias disponibles:")
            materias_result = conn.execute_query(materias.GET_ALL_SUBJECTS)
            for materia in materias_result:
                print(Fore.BLUE + f"ID: {materia[0]}, Nombre: {materia[1]}" + Style.RESET_ALL)  # Adjust the indices according to your data structure

            materia_id = input(Fore.GREEN + "Ingrese el ID de la materia que desea eliminar: " + Style.RESET_ALL)
            conn.execute_query(materias.DELETE_SUBJECT, (materia_id,))
            print(Fore.MAGENTA + "Materia eliminada con éxito." + Style.RESET_ALL)
            pass
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()