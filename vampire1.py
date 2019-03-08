# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:22:08 2018

@author: jap090020
"""

r = 3
for fang1 in range(10**(r-1),10**r):
    for fang2 in range(fang1,10**r):
        prod = fang1*fang2
        st1 = str(fang1)
        st2 = str(fang2)
        spr = str(prod)
        sinput = st1+st2
        if len(sinput) != len(spr): continue
        siarray = []
        sparray = []
        for i in range(len(sinput)):
            siarray.append(sinput[i])
            sparray.append(spr[i])
        siarray.sort()
        sparray.sort()
        vampire = True
        for i in range(len(sinput)):
            if siarray[i] != sparray[i]: 
                vampire = False
                break
        if vampire:
            print(fang1,fang2,prod)