import fastf1 as f1
import pandas as pd
from datetime import date, time, datetime, timedelta

# Fuente https://europeanvalley.es/noticias/analizar-la-f1-con-python-ultima-vuelta-del-mundial/

# https://www-f1monkey-com.translate.goog/f1-data-analysis-with-python-the-basics/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

# API  https://openf1.org/

f1.Cache.enable_cache(
    'C:/Users/CHIKY/OneDrive/Escritorio/repositorios/F1/Proyctos')

# Cargar la carrera y
race = f1.get_session(2025, 2, 'R')
race.load()


lap = race.laps.pick_driver('HAM')  # obtengo los tiempos de vuelta

# Elijo las columnas del frame
seleccion = lap[['LapNumber', 'Driver', 'DriverNumber', 'LapTime']]


vuelta_rapida = lap = race.laps.pick_driver(
    'HAM')  # .pick_fastest() #vuelta rapida

vuelta_r_ordenada = vuelta_rapida[['LapNumber', 'Driver', 'LapTime']]  # Df

lista_pilotos = ['COL', 'ALB']

# for x in lista_pilotos:
# print(race.laps.pick_driver(x).pick_fastest())
# print('###########')

# obtengo el total de segundos
segundos = vuelta_r_ordenada['LapTime']

for x in segundos:
    total_seconds = x.total_seconds()  # Obtengo el total de segundos
    minutes = int(total_seconds // 60)  # Minutos completos
    seconds = total_seconds % 60  # Segundos restantes
    formatted_time = f"{minutes:01}:{seconds:02.3f}"  # Formato MM:SS.ss
    print(formatted_time)

# for x in vuelta_r_ordenada:
# print(x['lapTime'])  # obtengo el total de segundos

# print(vuelta_r_ordenada.head(60))

# ver forma de formatear el timedelta a minutos y segundos

