#Leer un número de 3 digitos y formar el mayor número posible con sus cifras
def funcion3(numero):
    import itertools
    permutaciones = list(itertools.permutations(list(numero)))
    lista = []
    for i in range(0,len(permutaciones)):
        acumulador = ''
        for j in range(0,len(permutaciones[i])):
            acumulador = acumulador+permutaciones[i][j]
        lista.append(int(acumulador))
    print('Posibles permutaciones',lista,sep=' ')
    print('Número mayor posible con sus cifras:',str(max(lista)),sep=' ')

pos = True
while pos:
    
    print('-'*50)
    try:
        print('-'*50)
        numero = int(input('Digite un número de 3 cifras: '))
        if len(str(numero)) == 3:
            funcion3(str(numero))
            print('-'*50)
        else:
            print('-'*50)
            print('¡El tamaño del número ingresado no es 3!')
            print('-'*50)
    except BaseException:
        print('-'*50)
        print('¡No es un número!')

    print('-'*50)    
    salir = input('¿Desea salir del programa? (S/N): ').upper()
    if salir == 'N':
        continue
    else:
       break
        
        