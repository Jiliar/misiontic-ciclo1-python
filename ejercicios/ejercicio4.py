#Leer dos números de 3 digitos cada uno, formar un tercer número con el mayor del primero y el menor del segundo
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

flag = True
numeros = []
for i in range(0,2):
    try:
        print('-'*50)
        numero = int(input('Digite el número '+str(i+1)+': '))
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