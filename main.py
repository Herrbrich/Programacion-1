from funciones.cargar_paciente import cargar_paciente
from funciones.mostrar_pacientes import mostrar_pacientes
from funciones.buscar_paciente import buscar_paciente
from funciones.ordenar_pacientes import ordenar
from funciones.mas_dias_internado import mas_dias
from funciones.menos_dias_internado import menos_dias
from funciones.mayor_5_dias import mas_5
from funciones.promedio_dias import promedio_dias
from funciones.mostrar_menu import mostrar_menu, obtener_opcion

archivo_clinico = []


opcion = obtener_opcion()

while 1 <= opcion <= 9:

    match opcion:
        case 1:
            cargar_paciente(archivo_clinico)
        case 2:
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun. ")
            else:
                mostrar_pacientes(archivo_clinico)
        case 3:
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun. ")    
            else:
                buscar_paciente(archivo_clinico)
        case 4:
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun.")
            else:
                ordenar(archivo_clinico)              
                print("Pacientes ordenados por número de HC:")
                mostrar_pacientes(archivo_clinico)    
                
        case 5:
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun. ")
            else:
                paciente = mas_dias(archivo_clinico)
                print("Paciente con MÁS días internado:", paciente)         
        case 6:                    
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun. ")
            else: 
                paciente = menos_dias(archivo_clinico)
                print("Paciente con MENOS días internado:", paciente)
        case 7:
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun.")
            else:
                pacientes = mas_5(archivo_clinico)
                if len(pacientes) > 0:
                    print("Pacientes con más de 5 días de internación:")
                    for p in pacientes:
                        print(p)               
        case 8:
            if len(archivo_clinico) == 0:
                print("No hay pacientes cargados aun. ")
            else:
                prom = promedio_dias(archivo_clinico)
                print(f"Promedio de días de internación: {prom:.2f}")
            
        case 9: 
            print("\n¡Hasta luego!")
            break
    opcion = obtener_opcion()

print("\nPrograma finalizado.")





