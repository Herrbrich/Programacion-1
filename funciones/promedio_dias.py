def promedio_dias(archivo_clinico):
    contador_paciente = 0
    dias_internados = 0

    for paciente in archivo_clinico:
        if paciente[4] > 0:
            dias_internados += paciente[4]
            contador_paciente +=1
    if contador_paciente == 0:
        print("No hay pacientes con dias para calcular el pomedio.")
        return           

    promedio = dias_internados / contador_paciente
    return promedio