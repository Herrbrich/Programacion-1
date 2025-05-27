def mostrar_menu() -> str:
    print("\n====== MENÚ PRINCIPAL ======")
    print("1. Cargar Pacientes")
    print("2. Mostrar todos los pacientes ")
    print("3. Buscar pacientes por numero de Historia Clinica ")
    print("4. Ordenar pacientes por numero de Historia Clinica ")
    print("5. Mostrar paciente con mas dias de internacion")
    print("6. Mostrar paciente con menos dias de internacion")
    print("7. cantidad de pacientes con mas de 5 dias de internacion ")
    print("8. promedio de dias de internacion de todos los pacientes")
    print("9. Salir")
    return input("Seleccione una opción: ")



def obtener_opcion ()->int:
    opcion = mostrar_menu() 

    while (opcion.isdigit() == False) or (int(opcion) < 1 or int(opcion) > 9):
        print("Opcion invalida")
    
        opcion = mostrar_menu()
        
    return int(opcion)

