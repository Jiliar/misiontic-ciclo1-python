import emuler_enum as p

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
    return average

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
        average.append(promedio)#Problema con puntos flotantes
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
    
    #print(city, '{0:.2f}'.format(max_average), alarm, sep=' ')
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
    
    #print(city, '{0:.2f}'.format(max_average), alarm, sep=' ')
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
        #print(alarm)
    output = {'distribucion_alarmas': alarms_distribution}
    return output
        

def is_float(element):
    flag = True
    try:
        float(element)
    except ValueError:
        flag = False
    return flag

#reto 4
def icas_x_ciudad(ciudad, ciudades, icas_calculados):
    values = []
    alarms = []
    pos = 0
    for i in ciudades:
        if i == ciudad:
            values.append(icas_calculados[pos])
            alarms.append(alert_generation(icas_calculados[pos]))
        pos+=1
    return [values, alarms]

def simple_best_average_calc(info_average):
    max_average = 99999999
    pos = 0
    for i in info_average:
        if float(i) < float(max_average):
            max_average = i
        pos+=1
    
    result = ''
    if max_average == 99999999:
        max_average = 0
    return '{0:.2f}'.format(max_average)

def simple_worst_average_calc(info_average):
    max_average = 0
    pos = 0
    for i in info_average:
        if float(i) > float(max_average):
            max_average = i
        pos+=1
    return '{0:.2f}'.format(max_average)

def clasify_alarms(alerts):
    answer = {}
    acum = '';
    for alert in ALERTAS:
        answer.update({alert[1]: 0})
    
    for aux in answer.keys():
        answer[aux] = alerts.count(aux)
    
    for i in answer.values():
        acum += str(i)+' '
    
    return acum.strip()

def clasify_ica(ciudad,ciudades,promedios_x_ciudad):
    pos = ciudades.index(ciudad)
    menor = 0
    mayor = 0
    igual = 0
    answer = ''
    if pos > -1:
        average = info['info_promedio']['promedios'][pos]
        for i in promedios_x_ciudad[ciudad]:
            if i < average:
                menor += 1
            elif i == average:
                igual += 1
            elif i > average:
                mayor += 1
        answer = str(menor)+' '+str(igual)+' '+str(mayor)
    else:
        answer = '0 0 0'
    
    return answer

#End Functions 
    
# Start Variables Declarations
pos = 0
alerts_list = []
ica_acum = 0
n = 0
info = {}
cities = []
inputs = [] 
cities_exclude = []
alarms = []
ica_values = []
alarmas_x_ica = []
ciudades_no_validas = []      
entradas_no_validas = []
# End Variables Declarations

# Start Input Testing
constants = p.Params()
n = constants.N2
inputsx = constants.INPUTS2
# End Input Testing

n = n.split(' ');
if len(n) == 2:
    if n[0].strip().isnumeric() and n[1].strip().isnumeric():
        if int(n[0].strip()) > 0:
            info = {'cant_ciudades':int(n[0].strip()), 'cant_lecturas' : int(n[1].strip())} 

j = 0
for i in range(info['cant_lecturas']):
    
    city = 0
    co2 = 0
    ica = 0

    j = inputsx[i]
    data = j.split(' ')
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
                    alarmas_x_ica.append(alert_generation(ica)) #reto4
                    alarm = alert_generation(ica)
                    alarms.append(alarm)
                else:
                    cities_exclude.append(city)
            else:
                ciudades_no_validas.append(city)
                entradas_no_validas.append(co2) 
                continue
    else:
        continue

info.update({'ciudades':cities, 'inputs_co2':inputs, 'ica_calculado': ica_values, 'alarmas_x_ica': alarmas_x_ica, 'ciudades_no_encotradas':cities_exclude, 'ciudades_no_validas': ciudades_no_validas, 'inputs_no_validos': entradas_no_validas})   #reto 4 
info.update({'promedio_ica_gral':ica_average_calc(info['ica_calculado'])})
info.update(average_calc(info['cant_ciudades'], info['ciudades'], info['ica_calculado']))
info.update(best_average_calc(info['info_promedio']))
info.update(worst_average_calc(info['info_promedio']))
info.update(alarms_distribution(info['info_promedio']['alarmas']))

#reto 4
output = {}
aux1 = {}
aux2 = {}
for ciudad in info['info_promedio']['ciudades']:
    data = icas_x_ciudad(ciudad, info['ciudades'], info['ica_calculado'])
    aux1.update({ciudad : data[0]})
    aux2.update({ciudad : data[1]})
output.update({'icas_x_ciudad': aux1, 'alarmas_x_ciudad': aux2})
    
info['info_promedio'].update(output)
print_summary(info)


                

print('-'*20,'SALIDA RETO 4:','-'*20,sep='\n')
general = info['info_promedio']
pos = 0
for i in range(1,info['cant_ciudades']+1):
    print(i)
    icas_x_ciudad = general['icas_x_ciudad'][i]
    promedio_ica = '{0:.2f}'.format(general['promedios'][pos])
    print(simple_best_average_calc(icas_x_ciudad), promedio_ica, simple_worst_average_calc(icas_x_ciudad),sep=' ')
    print(clasify_alarms(general['alarmas_x_ciudad'][i]))
    print(clasify_ica(i, general['ciudades'], general['icas_x_ciudad']))
    pos+= 1
        