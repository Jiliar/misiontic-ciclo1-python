#Declarations of Constants
                    #C[0]       Il[1]   Ih[2]    BPl[3]   BPh[4]    
MATRIZ_VALORES  = [ ((0, 4.5),      0,      50,     0,      4.4),
                    ((4.5, 9.5),   51,      100,    4.5,    9.4),
                    ((9.5, 12.5),  101,     150,    9.5,    12.4),
                    ((12.5, 15.5), 151,     200,    12.5,   15.4),
                    ((15.5, 30.5), 201,     300,    15.5,   30.4),
                    ((30.5, 40.5), 301,     400,    30.5,   40.4),
                    ((40.5, 50.5), 401,     500,    40.5,   50.4) ]


ALERTAS = [ ((-1,50),      'verde'),
            ((50,100),    'amarillo'),
            ((100,150),   'naranja'),
            ((150,200),   'rojo'),
            ((200,300),   'morado'),
            ((300,99999999999),'marron')] 
    
# Start Functions
def inputs_def(co2):
    
    result = []    
    maximum = MATRIZ_VALORES[len(MATRIZ_VALORES)-1][0][1]
    if co2 <= maximum :
        for val in MATRIZ_VALORES:
            if (co2 >= val[0][0]) and (co2 < val[0][1]):
                result = (val,co2)
                break
    else:
        result = -1
        
    return result

def ica_operation(value):
    val = value[0]
    ica  = (val[2] - val[1]) / (val[4] - val[3]) * (value[1]-val[3]) + val[1]
    return ica

def alert_generation(value):
    result = 0
    for val in ALERTAS:
        if (value > val[0][0]) and (value <= val[0][1]):
            result = val[1]
            break
     
    return result 
#End Functions 

try:
    #Definitions of Variables
    pos = 0
    alerts_list = []
    ica_acum = 0
    
    #Inputs Data
    while True:
        co2 = float(input())
        pos+=1
        data = inputs_def(co2)
        if type(data) is tuple:
            value = ica_operation(data)
            ica_acum += value
            alert = alert_generation(value)
            alerts_list.append(alert)
            if alert == 'verde':
                break
       
    #Calculations 
    distribution = (100/pos)/100
    average = ica_acum/pos
    
    #Outputs:
    print(pos)
    print('{0:.2f}'.format(average),alert_generation(average),sep=' ')
    for i in ALERTAS:
        if i[1] in alerts_list:
           times = alerts_list.count(i[1])*distribution
           print(i[1], "{:.2%}".format(times))
        else:
            print(i[1], '0.00%')
            
except BaseException:
    print('¡Error al ingresar datos!')