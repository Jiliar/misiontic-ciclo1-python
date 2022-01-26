import math

def inputs_def(co2):
    
    result = []
    #Declaración de constantes:
                          #C[0]       Il[1]   Ih[2]    BPl[3]   BPh[4]    
    MATRIZ_VALORES  = [ ((0, 4.5),      0,      50,     0,      4.4),
                        ((4.5, 9.5),   51,      100,    4.5,    9.4),
                        ((9.5, 12.5),  101,     150,    9.5,    12.4),
                        ((12.5, 15.5), 151,     200,    12.5,   15.4),
                        ((15.5, 30.5), 201,     300,    15.5,   30.4),
                        ((30.5, 40.5), 301,     400,    30.5,   40.4),
                        ((40.5, 50.5), 401,     500,    40.5,   50.4) ]
    
    for val in MATRIZ_VALORES:
        if (co2 >= val[0][0]) and (co2 < val[0][1]):
            result = (val,co2)
            break
        
    return result

def ica_operation(value):
    #(Ih - Il)/(BPh - BPl)* (C-BPl) + Il
    val = value[0]
    ica  = (val[2] - val[1]) / (val[4] - val[3]) * (value[1]-val[3]) + val[1]
    return ica

def alert_generation(value):
    result = 0
    ALERTAS = [ ((-1,50),     'verde'),
                ((50,100),    'amarillo'),
                ((100,150),   'naranja'),
                ((150,200),   'rojo'),
                ((200,300),   'morado'),
                ((300,999999999999999999),'marron')] 
    for val in ALERTAS:
        if (value > val[0][0]) and (value <= val[0][1]):
            result = val[1]
            break
     
    return result 

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n


try:
    co2 = float(input('Digite el valor de la concentracion de CO 8h (ppm): '))
    data = inputs_def(co2)
    if  len(data) > 0:
        value = ica_operation(data)
        alert = alert_generation(value)
        present = "{:.2f}".format(truncate(value,2))
        print(present, alert, sep=' ')
    else:
        print(-1,'error en los datos',sep=' ')
except BaseException:
    print('¡Error al ingresar datos!')