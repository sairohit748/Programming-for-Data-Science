# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
5 == 5
round(0.7) 
round(1.89)
1+2
5-3
5*4
11/2
11//2
11%2
5**2     ###special note
13^4     ###doesn't give you powers

val= 5
val += 1
val

###Strings
val ="Hello"
val += " world"
val
##

##Bytes/Byte Arrays

############
## Lists/Collections
############

list_ex = []
[3]
[6,9]
list_ex
list_ex.append(7) # add one thing to the list
list_ex
not(list_ex)

list_ex.extend([8,9]) #add muliple things to the list
list_ex

len(list_ex) #length of list

list_ex + [10]
list_ex

list_ex += [10]
list_ex

[x**2 for x in list_ex]
##

#################
### operations on lists
#################
list_ex[0]
list_ex[1]
list_ex[-1]
list_ex[1:-1]
list_ex[1:]
list_ex[:-1]
##

##Tuples
tup_ex =("a","b","c","d")
tup_ex[2]
tup_ex.append("f") ##throws error tuples cannot be extended( tuples are immutable )
##

##############
("hello","world")[5>2]
#### bad programming practice
("hello","world")[5<2]
##############

##Dictionaries
dict_ex = {"a":1, "b": 2}
dict_ex["b"]
dict_ex.get("c", 3)
dict_ex
dict_ex["d"] = 4
dict_ex
##

###############
##Control Structures
###############

#IF Statements
if True:
    print("it's true")
    print("it's still true")
else: 
    print("it wasn't true")
print("I run no matter what")

x = 5
while x>0:
    print(x)
    x -= 2
    if x<0:
        x = 6
        #continue
        break
       
for i in range(100):
    print(i)

for y in list_ex:
    print(y)

for ndx, y in enumerate (list_ex):
    print(ndx, y) 
    

def factorial(x): 
    prod = 1
    while x>1:
        prod *= x
        x -= 1
    return prod

factorial(5)
        
list_ex = [1,2,3]
tmp = list(list_ex)

for i in range(len(list_ex)):
    list_ex[i] = list_ex[i]**2
list_ex
tmp
    
    
        
    
    
        
