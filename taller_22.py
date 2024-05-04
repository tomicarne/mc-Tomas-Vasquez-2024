# -*- coding: utf-8 -*-
"""taller 22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aELOcSZe3wiOdTRxLs9jGzHyFgo-_IEW
"""

import copy
from re import S
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression
def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)
    temp = []
    zer = 0
    n = len(b)

    for i in range(n):
        if a[i][i] == 0:
            for k in range(i+1,n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k] , a[i]
                    b[i], b[k] = b[k] , b[i]
                    break
        pivote = a[i][i]
        #Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote


        #Reducción
        for k in range(n):
            if i != k:
                #Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux


    return b







X1= [1,1,2,3,1,2,3,3]
#X1= [0,2,2.5,1,4,7]
X2 = [0,1,1,2,2,3,3,1]
#X2 = [0,1,2,3,6,2]
Y = [0.6,2,0.1,0.3,2.2,2.3,0.8,-1]
#Y = [2.5,5.5,5,0,1.5,13]

sum_x1 =sum_x2= sum_y= sum_x1a2 = sum_x1py =sum_x2py= sum_xy = sum_x2y =sum_x2a2=sum_x1x2=0
for r in range(len(X1)):
  sum_x1 = sum_x1 + X1[r]
  sum_x2 = sum_x2 + X2[r]
  sum_y = sum_y + Y[r]
  sum_x1py = sum_x1py + (X1[r]*Y[r])
  sum_x2py = sum_x2py + (X2[r]*Y[r])
  sum_x1a2 = sum_x1a2 + X1[r]**2
  sum_x2a2 = sum_x2a2 + X2[r]**2
  sum_x1x2 = sum_x1x2 +(X1[r]*X2[r])
a = [[len(X1), sum_x1, sum_x2], [sum_x1, sum_x1a2, sum_x1x2], [sum_x2, sum_x1x2, sum_x2a2]]
b = [sum_y, sum_x1py, sum_x2py]
prom_y = sum_y / len(Y)
c = gaussJordan(a, b)



a0 = c[0]
a1 = c[1]
a2 = c[2]

print ("a0 : ",a0, "\n","a1 : ",a1 , "\n","a2 :",a2)
Sr = St =0
for r in range(len(X1)):
  Sr =Sr + (Y[r] - a0 - (a1*X1[r]) -(a2*X2[r]))**2
  St =St + (Y[r]-prom_y)**2
print("Sr",Sr)
print("St",St)