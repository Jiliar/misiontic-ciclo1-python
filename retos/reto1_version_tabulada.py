def inputs_def(co2):
    
    result = []
   #Declaración de constantes:
                          #C[0]       Il[1]   Ih[2]    BPl[3]   BPh[4]    
    MATRIZ_VALORES  = [ [(0, 4.4),      0,      50,     0,      4.4],
                        [(4.5, 9.4),   51,      100,    4.5,    9.4],
                        [(9.5, 12.4),  101,     150,    9.5,    12.4],
                        [(12.5, 15.4), 151,     200,    12.5,   15.4],
                        [(15.5, 30.4), 201,     300,    15.5,   30.4],
                        [(30.5, 40.4), 301,     400,    30.5,   40.4],
                        [(40.5, 50.4), 401,     500,    40.5,   50.49] ]
    
    for val in MATRIZ_VALORES:
        if val[0][0] <= co2 <= val[0][1]:
            result = val
            result.append(co2)
            break
        
    return result

def ica_operation(val):
    print('-'*80,sep=' ')
    print('DATOS DE ENTRADA PARA GENERACIÓN DE CALCULO',sep=' ')
    print('-'*80,sep=' ')
    print('Ih',val[2],sep=' = ')
    print('Il',val[1],sep=' = ')
    print('BPh',val[4],sep=' = ')
    print('BPl',val[3],sep=' = ')
    print('C',val[5],sep=' = ')
    print('-'*80,sep=' ')
    print('FORMULACIÓN:','(Ih - Il)/(BPh - BPl)*(C-BPl)+Il',sep=' ')
    print('-'*80,sep=' ')
    #(Ih - Il)/(BPh - BPl)* (C-BPl) + Il
    ica  = (val[2] - val[1]) / (val[4] - val[3]) * (val[5]-val[3]) + val[1]
    
    return round(ica,4)

def alert_generation(value):
    result = 0
    ALERTAS = [ ((0,50),     'verde'),
                ((50.1,100), 'amarillo'),
                ((100.1,150),'naranja'),
                ((150.1,200),'rojo'),
                ((200.1,300),'morado'),
                ((300.1,),   'marron')] 
    for val in ALERTAS:
        if val[0][0] <= value <= val[0][1]:
            result = val[1]
            break
     
    return result       

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

print('-'*80,sep=' ')
print('Sistema para el cálculo del índice de Calidad del Aire (ICA)')
print('-'*80,sep=' ')
print('Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM)')
print('-'*80,sep=' ')

co2 = float(input('Digite el valor de la concentración de CO 8h (Unidad ppm): '))
data = inputs_def(co2)
if  len(data) > 0:
    value = ica_operation(data)
    alert = alert_generation(value)
    present = '{0:.2f}'.format(value) if str(value)[-2:len(str(value))] == '.0' else truncate(value,2)
    print('Resultado de la evaluación del Sensor',sep=' ')
    print('-'*80,sep=' ')
    print('VALOR ICA: ', present)
    print('-'*80,sep=' ')
    print('ALERTA:',alert,sep=' ')
    print('-'*80,sep=' ')
else:
    print(-1,'error en los datos',sep=' ')