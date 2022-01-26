#INICIO IMPORTACIÓN DE LIBRERIAS
import pandas as pd
import numpy as np
import statistics as s
#FIN IMPORTACIÓN DE LIBRERIAS

# INICIO DECLARACIÓN CONSTANTES

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

#FIN DECLARACIÓN CONSTANTES

#INICIO DECLARACIÓN DE FUNCIONES

#INICIO FUNCIONES LOGICA DEL NEGOCIO

#Función para evalular las muestras tomadas por ciudad        
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

#Función para calcular el ICA segun sean las muestras obtenidas por ciudad 
def ica_operation(value):
    val = value[0]
    ica  = (val[2] - val[1]) / (val[4] - val[3]) * (value[1]-val[3]) + val[1]
    return ica

#Función para la generación de alertas dada la evaluación de ICA
def alert_generation(value):
    result = 0
    for val in ALERTAS:
        if (value > val[0][0]) and (value <= val[0][1]):
            result = val[1]
            break
    return result 

    
#FIN FUNCIONES LOGICA DEL NEGOCIO

#INICIO FUNCIONES DE PROPOSITO GENERAL
#Funciones para tratamiento de dataframes
#Función para generar la segmentación de datos de un dataframe segun indices extraidos
def get_segment_data(df, indexes_num, is_dataframe):
    data = df.to_numpy()
    info = []
    for i in indexes_num:
        info.append(data[i].tolist())

    info = get_ica_calc(info)
    
    if is_dataframe == True:
        info = pd.DataFrame(info, columns =['id_city', 'city_name', 'department_name', 'measurement', 'ica_average', 'alarms'])
        
    return info

#Función para calcular ica, returna la lista de entrada con dos columnas extras ica_average y alarm
def get_ica_calc(info):
    for i in info:
        ppm = inputs_def(i[3])
        ica_val = 0
        if type(ppm) is tuple:
            ica_val = ica_operation(ppm)

        i.append(float('{0:.2f}'.format(ica_val)))
        i.append(alert_generation(ica_val))
        
    return info


#Función para extraer los indices de un dataframe
def get_indexes(df, value):
    cities = df['id_city'].to_numpy()
    return np.where(cities == int(value))[0]

#Función para extraer segmento de datos segun hoja de calculo en formato .csv
def get_segment_data_city(value):
    df = pd.read_csv("data.csv")
    indexes = get_indexes(df, value)
    new_df = get_segment_data(df, indexes, True)
    return new_df

def get_specific_stats(val):
        print('mean','{0:.2f}'.format(np.mean(val)) ,sep=' ')
        #print('std','{0:.2f}'.format(np.std(val)) ,sep=' ') #desviación estándar poblacional
        print('std','{0:.2f}'.format(s.stdev(val)) ,sep=' ') #desviación estándar muestral
        print('min','{0:.2f}'.format(np.min(val)) ,sep=' ')
        print('max','{0:.2f}'.format(np.max(val)) ,sep=' ')
    
#Función para la generación de estadisticas segun las medidas extraidas por ciudades
def get_statistics():
    try:
        values = input().strip().split(' ')
        values = [int(x) for x in values]
        values.sort()
        concating = []
        for value in values:
            new_df = get_segment_data_city(value)
            #concating.append(new_df)
            #print(new_df)
            print(new_df['id_city'][0],new_df['city_name'][0],new_df['department_name'][0],sep=' ')
            print('count',len(new_df),sep=' ')
            print('c measurement')
            get_specific_stats(new_df['measurement'])
            print('ica')
            get_specific_stats(new_df['ica_average'])
            print('alerts')
            alerts = new_df['alarms'].to_numpy().tolist()
            for value in ALERTAS:
                print(value[1], alerts.count(value[1]), sep=' ')
        #df1 = pd.concat(concating)        
        #df1.to_excel("output.xlsx") #Exportar datos a excel
    except BaseException:
        print('¡Error al intentar procesar la información!')
            

#FIN FUNCIONES DE PROPOSITO GENERAL

#FIN DECLARACIÓN DE FUNCIONES

#EJECUCIÓN DE FUNCIONES
get_statistics()