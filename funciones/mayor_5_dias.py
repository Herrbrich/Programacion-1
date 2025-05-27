def mas_5(archivo_clinico):

    if len(archivo_clinico) == 0:          
        print("No hay pacientes cargados.")
        return                          

    paciente_mas_5 = []                     

    for paciente in archivo_clinico:       
        if paciente[4] > 5:                
            paciente_mas_5 += [paciente]    

    return paciente_mas_5
