def ordenar(archivo_clinico):
    n = len(archivo_clinico)
    for i in range(n):
      for j in range(n - i -1):
          if archivo_clinico[j][0] > archivo_clinico[j+1][0]:
            aux = archivo_clinico [j+1]
            archivo_clinico[j+1] = archivo_clinico[j]
            archivo_clinico[j] = aux

    return archivo_clinico