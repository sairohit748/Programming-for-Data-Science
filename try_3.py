# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:56:31 2018

@author: Rohit
"""

import csv
import numpy as np 
from scipy.stats import norm

inmat = []
with open('bwght.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        inmat.append(line)        
        
inmat = [row[:5] + row[6:] for row in inmat]


print(inmat[0])

for num,i in enumerate(inmat[0]):
    print(num,i)
    
data = np.matrix(inmat[1:])  
print(data)  
x= np.array([1,2,3])
y = np.array([4,5,6])
print(x*y)
x = [[1,2],[3,4]]
type(x)
x = np.matrix(x)
y = [[1,5],[7,8]]
y = np.matrix(y)
print(x+y)
print(x*y)
print((x.T)*y)