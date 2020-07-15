# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:18:47 2020

@author: ALI
"""

import numpy as np
import pandas as pd

#Cargamos datos
dataset1 = pd.read_csv('lista1.csv')

# variables dependientes e independientes
x = dataset1.iloc[:, :4]
y = dataset1.iloc[:, 4]

# llena con la media si el campo CI esta vacio
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x.values[:, 0:0])
x.iloc[:, 0:0] = imputer.transform(x.values[:, 0:0])


# tranformamos los sexos HOMBRE =0 MUEJER =1
from sklearn.preprocessing import LabelEncoder
label_encoder_x = LabelEncoder()
x.iloc[:, 2] = label_encoder_x.fit_transform(x.values[:, 2])
# tranformamos los DPTO LA PAZ =0 COCHABAMBA =1 SANTA CRUZ =3 
from sklearn.preprocessing import LabelEncoder
label_encoder_x = LabelEncoder()
x.iloc[:, 3] = label_encoder_x.fit_transform(x.values[:, 3])


# tranformamos los nombre en numeros
from sklearn.preprocessing import LabelEncoder
label_encoder_x = LabelEncoder()
x.iloc[:, 1] = label_encoder_x.fit_transform(x.values[:, 1])
