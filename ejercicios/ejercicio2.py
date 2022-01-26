pos = True

while pos:
    print('-'*50)
    anio = int(input('Digite el año: '))
    
    bandera = anio % 100 != 0
    if anio % 400 == 0:
        bandera = not bandera
        
    if anio % 4 == 0 and bandera:
        print('-'*50)
        print('El año',str(anio),'es biciesto', sep=' ')
    else:
        print('-'*50)
        print('El año',str(anio),'no es biciesto', sep=' ')
    
    print('-'*50)    
    salir = input('¿Desea salir del programa? (S/N): ').upper()
    if salir == 'N':
        continue
    else:
       break
        