# -*- coding: utf-8 -*-
"""
@author: ali
"""
from math import sqrt
def desviacion_estandar(valores, media):
    suma = 0
    for valor in valores:
        suma += (valor - media)**2
        
    res = suma / (len(valores)-1)
    return sqrt(res)
def calcular_media(valores):
    suma = 0
    for valor in valores:
        suma += valor
        
    return suma/len(valores)

if __name__ == "__main__":
    valor_ci = [6011293, 1234567, 7654321, 5678901, 3456789, 9876543, 
               6574839, 7685940, 7768593,  7984612, 7654839, 
               6573910, 8663916, 8975312, 9375192, 9856212, 9986351, 
               8736512, 8451241, 8385323, 8766264, 9846263, 9999443, 9998883]
    media_ci = calcular_media(valor_ci)
    resultado_ci = desviacion_estandar(valor_ci, media_ci)
    print('La desviacion estandar de CI es: {}'.format(resultado_ci))
    print('La media es de CI es: {}'.format(media_ci))
    
    
    valor_nota = [65, 66, 75, 34, 65, 74, 86, 55, 51, 45, 50, 66, 
                  75, 89, 90, 45, 65, 76, 88, 66, 75, 89, 90, 65]
    media_nota = calcular_media(valor_nota)
    resultado_nota = desviacion_estandar(valor_nota, media_nota)
    print('La desviacion estandar de NOTA es: {}'.format(resultado_nota))
    print('La media es de NOTA es: {}'.format(media_nota))
    
    
    valor_edad = [25, 22, 23, 24, 25, 25, 23, 21, 22, 22, 31, 23, 
                  24, 20, 21, 24, 22, 25, 21, 23, 24, 20, 21, 24]
    media_edad = calcular_media(valor_edad)
    resultado_edad = desviacion_estandar(valor_edad, media_edad)
    print('La desviacion estandar de EDAD es: {}'.format(resultado_edad))
    print('La media es de EDAD es: {}'.format(media_edad))
    
    
    
    
    
    
    
    
    