# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
from statistics import mode

datos=pd.read_csv('lista1.csv', header=0)
print (datos)
# calculo de la MODA
print('La moda de la NOTA es: ')
print (mode(datos['NOTA']))
print('La moda de la EDAD es: ')
print (mode(datos['EDAD']))
print('La moda de la DPTO es: ')
print (mode(datos['DPTO']))

"""
Calculo de la DESVIACION STANDAR DE CI EDAD Y NOTA
"""
print('La Desviacion estandar CI es: ')
print ((datos['CI']).std())
print('La Desviacion estandar EDAD es: ')
print ((datos['EDAD']).std())
print('La Desviacion estandar NOTA es: ')
print ((datos['NOTA']).std())

"""
DEL PROMEDIO O MEDIA DE  CI EDAD NOTA
"""

print('EL promedio de  CI es: ')
print ((datos['CI']).mean())
print('EL promedio de  EDAD es: ')
print ((datos['EDAD']).mean())
print('EL promedio de  NOTA es: ')
print ((datos['NOTA']).mean())
