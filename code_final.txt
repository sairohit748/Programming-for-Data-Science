# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 20:43:47 2018

@author: Rohit
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for q in a:
    for w in b:
        cycle_num = []
        z = False
        for st in range(1001):
            x = st
            if x == 0: continue
            lst = []
            lst.append(st)
            for u in range(1000):
                if x % 2 == 0:
                    x //= 2
                    if x in lst:
                        break
                    else:
                        lst.append(x)
                else:
                    x = q * x + w
                    if x in lst:
                        break
                    else:
                        lst.append(x)
                       
            if u == 999:
                z = True
                break
            check = min(lst[lst.index(x):])
            if check not in cycle_num:
                cycle_num.append(check)
        if z:
            print(q, w, "False")
        else:
            print(q, w, len(cycle_num))
            
### with 3 conditions ###
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for m in a:
    for n in b:
        for o in c:
            for p in d:
                cycle_num = []
                z = False
                for st in range(1001):
                    x =st
                    if x == 0: continue
                    lst = []
                    lst.append(st)
                    for u in range(1000):
                        if x % 3 == 0: 
                            x //= 3
                            if x in lst:
                                break
                            else:
                                lst.append(x)
                        elif x % 3 == 1:
                            x = m*x + n
                            if x in lst:
                                break
                            else:
                                lst.append(x)
                        else:
                            x = o*x + p
                            if x in lst:
                                break
                            else:
                                lst.append(x)
                    if u == 999:
                        z = True
                        break
                    check = min(lst[lst.index(x):])
                    if check not in cycle_num:
                        cycle_num.append(check)
                if z:
                    print(m ,n , o , p, "False")
                else:
                    print(m, n, o, p, len(cycle_num))           
                
                    
                        
                        
                    
                    
                
                