def menos_dias(archivo_clinico):
    
    if len(archivo_clinico) == 0:
        print("No hay pacientes cargados.")
        return                    
    
    paciente_min = archivo_clinico[0]
    for paciente in archivo_clinico[1:]:
        if paciente[4] < paciente_min[4]:   
            paciente_min = paciente         
    return paciente_min