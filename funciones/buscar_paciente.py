
def buscar_paciente(archivo_clinico):

    """Busca por número de historia clínica y 
    
    muestra los datos si lo encuentra."""
 
    if len(archivo_clinico) == 0:
        print("No hay pacientes cargados.")
        return

    paciente_a_buscar = int(input("Ingrese el número de historia clínica del paciente a buscar: "))

  
    for paciente in archivo_clinico:
        if paciente[0] == paciente_a_buscar:      
            print(f"el paciente {paciente[0]} fue encontrado")
            print(f"su nombe es: {paciente[1]} ")
            print(f"su su edad es: {paciente[2]} ")
            print(f"su diagnostico es: {paciente[3]} ")
            print(f"El paciente lleva {paciente[4]} dias de internacion.")
            break                                
    else:
        print("Paciente no encontrado")
