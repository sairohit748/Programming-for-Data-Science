# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 19:14:25 2018

@author: jap090020
"""


nstart = 1001
nconverge = 2000
abmax = 10
for a in range(1,abmax):
    for b in range(1,abmax):
        explosion = False
        cycles = []
        for st in range(1,nstart):
            if explosion: break
            x = st
            hail = []
            for i in range(nconverge):
                if x in hail: break
                hail.append(x)
                if x % 2 == 0:
                    x //= 2 
                else:
                    x = a*x + b
            if i == nconverge-1:
                explosion = True
                #print(st,False)
            else:
                #print(st,min(hail[hail.index(x):]))
                newbie = min(hail[hail.index(x):])
                if newbie not in cycles:
                    cycles.append(newbie)
        if explosion:
            print(a,b,False)
        else:
            print(a,b,cycles)



nstart = 1001
nconverge = 2000
abmax = 10
for a in range(1,abmax):
    for b in range(1,abmax):
        for c in range(1,abmax):
            for d in range(1,abmax):
                explosion = False
                cycles = []
                for st in range(1,nstart):
                    if explosion: break
                    x = st
                    hail = []
                    for i in range(nconverge):
                        if x in hail: break
                        hail.append(x)
                        if x % 3 == 0:
                            x //= 3 
                        elif x % 3 == 1:
                            x = a*x + b
                        else:
                            x = c*x + d
                    if i == nconverge-1:
                        explosion = True
                        #print(st,False)
                    else:
                        #print(st,min(hail[hail.index(x):]))
                        newbie = min(hail[hail.index(x):])
                        if newbie not in cycles:
                            cycles.append(newbie)
                if explosion:
                    print(a,b,c,d,False)
                else:
                    print(a,b,c,d,cycles)





r = 3
nstart = 1000
nconverge = 2000
abmax = 10
def hail(seqa,seqb,x):
    if x % r == 0:
        x //= r 
    else:
        x = seqa[x%r-1]*x + seqb[x%r-1]
    return x

def recursive_guy(seqa,seqb):
    if len(seqa) == r-1:
        hailstone(seqa,seqb)
    else:
        for a in range(1,abmax):
            for b in range(1,abmax):
                recursive_guy(seqa+[a],seqb+[b])

def hailstone(seqa,seqb):
    explosion = False
    cycles = []
    for st in range(1,nstart):
        if explosion: break
        x = st
        lst = []
        for i in range(nconverge):
            if x in lst: break
            lst.append(x)
            x = hail(seqa,seqb,x)
        if i == nconverge-1:
            explosion = True
        else:
            newbie = min(lst[lst.index(x):])
            if newbie not in cycles:
                cycles.append(newbie)
    if explosion:
        print(seqa,seqb,False)
    else:
        print(seqa,seqb,cycles)

recursive_guy([],[])
        