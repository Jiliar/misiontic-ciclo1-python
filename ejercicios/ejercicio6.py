#Union de ejercicios anteriores
def funcion1(numero):
    es_par = ''
    numeros = []
    for i in list(numero):
        numeros.append(int(i))
        
    if max(list(numeros)) % 2 == 0:
        es_par = 'es par'
    else:
        es_par = 'es impar'
        
    print('-'*50)
    print('El número mayor es',str(max(numero)),'y',es_par,sep=' ')
    print('-'*50)

def funcion2(numeros):
    numbers = []
    for x in numeros:
        lista = []
        for y in str(x):
            lista.append(int(y))
        numbers.append(lista)
    
    value_max = str(max(numbers[0]))
    value_min = str(min(numbers[1]))
    print('-'*50)
    print('Números ingresados',numeros,sep=' ')
    print('Nuevo valor:',(value_max+value_min),sep=' ')
    print('-'*50)

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

position = True
while position:
    print('-'*200)
    print('OPERACIONES CON NÚMEROS')
    print('-'*200)
    print('1. Leer un número de 4 digitos, mostrar el digito mayor e informar si es par o impar.')
    print('2. Leer dos números de 3 digitos cada uno, formar un tercer número con el mayor del primero y el menor del segundo.')
    print('3. Leer un número de 3 digitos y formar el mayor número posible con sus cifras.')
    print('4. Salir')
    print('-'*200)
    opc = int(input('Digite Opcion: '))
    if opc == 1:
        try:
            print('-'*50)
            numero = int(input('Digite número de 4 cifras: '))
            if len(str(numero)) == 4:
                funcion1(str(numero))
            else:
                print('-'*50)
                print('¡El tamaño del número no es 4!')
        except BaseException:
            print('-'*50)
            print('¡No es un número!')
            print('-'*50)

    elif opc == 2:
        
        flag = True
        numeros = []
        for i in range(0,2):
            try:
                print('-'*50)
                numero = int(input('Digite el número '+str(i+1)+' de 3 cifras: '))
                if len(str(numero)) == 3:
                    numeros.append(numero)
                else:
                    print('-'*50)
                    print('¡El tamaño del número '+str(i+1)+' no es 3!')
                    print('-'*50)
                    flag = False
                    break
                print('-'*50)
            except BaseException:
                print('-'*50)
                print('¡No es un número!')
                print('-'*50)
                flag = False
                break
                
        if flag:
            funcion2(numeros)
        else:
            print('-'*50)
            print('¡No es posible procesar la solicitud!')
            print('-'*50) 
    
    elif opc == 3:
        
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
    
    elif opc == 4:
        print('-'*50)    
        salir = input('¿Desea salir del programa? (S/N): ').upper()
        if salir == 'N':
            continue
        else:
            print('-'*50)   
            print('¡Good Bye!')
            print('-'*50) 
            break
  
    
