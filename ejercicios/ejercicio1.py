
def validar(numeros):
    if numeros[0] != numeros[1] and numeros[0] != numeros[2]:
        print('Los números son diferentes')
    elif numeros[0] == numeros[1] or numeros[0] == numeros[2]:
         print('El número '+numeros[0]+' esta repetido')
    elif numeros[1] == numeros[0] or numeros[1] == numeros[2]:
         print('El número '+numeros[1]+' esta repetido')
    elif numeros[2] == numeros[0] or numeros[2] == numeros[1]:
         print('El número '+numeros[2]+' esta repetido')

numeros = []
for i in range(0,3):
     numero = input('Digite el número '+str(i+1)+': ')
     numeros.append(numero)
     
validar(numeros)