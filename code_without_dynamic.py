# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:17:10 2018

@author: Rohit
"""

a = [3]
b = [3]
result = []
sets = []
for i in a:
    for j in b:
       for x in range(0,101):
           lst = []
           z = True
           count = 0
           lst.append(x)
           print("x:", x)
           if x == 0: continue
           while z:
               if x % 2 == 0:
                   x //= 2
                   if x in lst:
                       print("Looping")
                       print(x)
                       z = False
                   else:
                       count+= 1
                       lst.append(x)

               else:
                   if x == 1:
                       z = False
                   elif ((i % 2 != 0 and  j % 2 ==0 )or (i % 2 == 0 and  j % 2 != 0)):
                           print("This series is definitely exploding")
                           break
                   else:
                       x = i * x +j
                       if  x in  lst:
                           print("Looping")
                           print(x)
                           z = False
                       else:
                           count += 1
                           lst.append(x)
               if count == 999:
                   print("The series is exploding")
                   print(i,j)
                   z = False
           if count < 999 and z == False:
               print("converging", count)
           print("Next ")