def mostrar_pacientes(archivo_clinico):

    """Muestra cada paciente (una fila)
       con todos sus datos."""
    
    if len(archivo_clinico) == 0:
        print("No hay pacientes cargados.")
        return

    print("=== LISTA DE PACIENTES ===")
    print("HC | Nombre | Edad | Diagnostico | Días intenado")

    for paciente in archivo_clinico:  
        print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | "
              f"{paciente[3]} | {paciente[4]}")