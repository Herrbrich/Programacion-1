def mas_dias(archivo_clinico):
    
    if len(archivo_clinico) == 0:     
        return "sin opacientes cargados"                    
    
    paciente_max = archivo_clinico[0]
    for paciente in archivo_clinico[1:]:
        if paciente[4] > paciente_max[4]:   
            paciente_max = paciente         
    return paciente_max