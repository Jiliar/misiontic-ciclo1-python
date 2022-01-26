#Declarations of Constants
                    #C[0]       Il[1]   Ih[2]    BPl[3]   BPh[4]    
MATRIZ_VALORES  = [ ((0, 4.5),      0,      50,     0,      4.4),
                    ((4.5, 9.5),   51,      100,    4.5,    9.4),
                    ((9.5, 12.5),  101,     150,    9.5,    12.4),
                    ((12.5, 15.5), 151,     200,    12.5,   15.4),
                    ((15.5, 30.5), 201,     300,    15.5,   30.4),
                    ((30.5, 40.5), 301,     400,    30.5,   40.4),
                    ((40.5, 50.5), 401,     500,    40.5,   50.4) ]


ALERTAS = [ ((-1,50),     'verde'),
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

def ica_average_calc(lst):
    average = sum(lst) / len(lst)
    return '{0:.2f}'.format(average)

def print_summary(info):
    import json
    print('-'*20,'RESUMEN:','-'*20,json.dumps(info, sort_keys=False, indent=4),sep='\n')
    
def average_calc(cant_ciudades, ciudades, ica):
    output = {}   
    average = []
    cantidades = []
    cities = []
    alarms = []
    for x in range(1,cant_ciudades+1):
        cantidad = 0
        acumulador = 0

        pos = 0
        for z in ciudades:
            if x == z:
                cantidad+=1
                acumulador+=ica[pos]
            pos+=1
        cities.append(x)
        cantidades.append(cantidad) 
        promedio = 0.00  
        if cantidad > 0:
            promedio = acumulador/cantidad
            
        average.append(promedio)     
        alarms.append(alert_generation(promedio))
    
    output['info_promedio'] = {'ciudades':cities, 'cantidad_inputs_x_ciudad':cantidades, 'promedios':average, 'alarmas':alarms}
    
    return output

def worst_average_calc(info_average):
    max_average = 0
    city = ''
    alarm = ''
    pos = 0
    output = {}
    for i in info_average['promedios']:
        if float(i) > float(max_average):
            max_average = i
            city = info_average['ciudades'][pos]
            alarm = info_average['alarmas'][pos]
        pos+=1
    
    print(city, '{0:.2f}'.format(max_average), alarm, sep=' ')
    output['peor_promedio'] = {'ciudad':city, 'promedio':max_average, 'alarma':alarm}
    
    return output


def best_average_calc(info_average):
    max_average = 9999999999999999
    city = ''
    alarm = ''
    pos = 0
    output = {}
    for i in info_average['promedios']:
        if float(i) < float(max_average):
            max_average = i
            city = info_average['ciudades'][pos]
            alarm = info_average['alarmas'][pos]
        pos+=1
    
    print(city, '{0:.2f}'.format(max_average), alarm, sep=' ')
    output['mejor_promedio'] = {'ciudad':city, 'promedio':max_average, 'alarma':alarm}
    
    return output

def alarms_distribution(alerts_list):
    output = {}
    cantidad = len(alerts_list)
    distribution = (100/cantidad)/100
    alarms_distribution = []
    alarm = ''
    for i in ALERTAS:
        if i[1] in alerts_list:
           times = alerts_list.count(i[1])*distribution
           alarm = i[1]+' '+"{:.2%}".format(times)
        else:
            alarm = i[1]+' '+'0.00%'
        alarms_distribution.append(alarm)
        print(alarm)
    output = {'distribucion_alarmas': alarms_distribution}
    return output
        

def is_float(element):
    flag = True
    try:
        float(element)
    except ValueError:
        flag = False
    return flag
#End Functions 
    

#try:
    #Definitions of Variables
pos = 0
alerts_list = []
ica_acum = 0
n = 0
info = {}

while True:
    #n = input('Cantidad de ciudades a analizar y cantidad de lecturas separados por espacios: ')
    n = input('')
    n = n.split(' ');
    if len(n) == 2:
        if n[0].strip().isnumeric() and n[1].strip().isnumeric():
            if int(n[0].strip()) > 0:
                info = {'cant_ciudades':int(n[0].strip()), 'cant_lecturas' : int(n[1].strip())} 
                break
    else:
        continue
 
cities = []
inputs = [] 
cities_exclude = []
alarms = []
ica_values = []
ciudades_no_validas = []      
entradas_no_validas = []
for i in range(info['cant_lecturas']):
    
    city = 0
    co2 = 0
    ica = 0
    while True:
        #data = input('Ingrese ciudad y valor de concentración separados por espacios: ')
        data = input('')
        data = data.split(' ')
        if len(data) == 2:
            if data[0].strip().isnumeric() and is_float(data[1].strip()):
                city = int(data[0].strip())
                co2 = float(data[1].strip())
                ppm = inputs_def(co2)
                if type(ppm) is tuple:
                    if city > 0 and city <= info['cant_ciudades']:
                        inputs.append(co2)
                        ica = ica_operation(ppm)
                        cities.append(city)
                        ica_values.append(ica)
                        alarm = alert_generation(ica)
                        alarms.append(alarm)
                    else:
                        cities_exclude.append(city)
                    break
                else:
                    ciudades_no_validas.append(city)
                    entradas_no_validas.append(co2) 
                    continue
        else:
            continue

info.update({'ciudades':cities, 'inputs_co2':inputs, 'ica_calculado': ica_values, 'ciudades_no_encotradas':cities_exclude, 'ciudades_no_validas': ciudades_no_validas, 'inputs_no_validos': entradas_no_validas})       
info.update({'promedio_ica_gral':ica_average_calc(info['ica_calculado'])})
info.update(average_calc(info['cant_ciudades'], info['ciudades'], info['ica_calculado']))
info.update(best_average_calc(info['info_promedio']))
info.update(worst_average_calc(info['info_promedio']))
info.update(alarms_distribution(info['info_promedio']['alarmas']))
#print_summary(info)

#except BaseException:
#    print('¡Error al ingresar datos!')