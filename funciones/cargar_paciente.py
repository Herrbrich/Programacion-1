
def cargar_paciente(archivo_clinico):
    
    seguir = "si"

    while seguir == "si":

        numero_clinico = int(input("Ingrese el numero de historia clinica: "))
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("ingrese el diagnostico del paciente: ")
        dias_internado = int(input("Ingrese la cantidad de dias internado: "))

        paciente = [numero_clinico, nombre, edad, diagnostico, dias_internado]
        archivo_clinico[:] += [paciente]
        seguir = input("desea seguir cargando pacientes? (si/no): ")

