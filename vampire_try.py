# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:55:30 2018

@author: Rohit
"""

fang1 =  range(10,100)
fang2 =  range(10,100)

for a in fang1:
    for b in fang2:        
        vampire = a * b
        vamp_str = str(vampire)
        comp = str(a) + str(b)
        lst = []
        if len(comp) == len(vamp_str):
            for i in range(4):
                for j in range(4):
                    if comp[i] == vamp_str[j]:
                        if j not in lst:
                            lst.append(j)
                            break
            if len(lst) == 4:
                print(a, b, vampire, "True")
            
                
               
                
                
    