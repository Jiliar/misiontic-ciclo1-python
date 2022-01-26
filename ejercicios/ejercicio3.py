#Leer un número de 4 digitos, mostrar el digito mayor e informar si es par o impar.

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
