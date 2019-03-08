# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:03:01 2018

@author: jap090020
"""

import numpy as np
import scipy as sp
from scipy.stats import norm


def cross(*args):
    x = args[0]
    if len(args)==1:
        y = x
    else:
        y = args[1]
    return(x.T.dot(y))
def ols(X,y):
    return(np.linalg.solve(cross(X),cross(X,y)))
def least_squares(X,y):
    n = X.shape[0]
    b = ols(X,y)
    res = y-X.dot(b)
    RSS = cross(res)
    TSS = y.var()*n
    Rsq = 1-(RSS/TSS)
    sig = np.sqrt(RSS/n)
    #vb = np.linalg.inv(cross(X))*(sig**2)
    vb = X.T.dot(np.diagflat(np.power(res,2))).dot(X)
    vb = np.linalg.inv(cross(X)).dot(vb).dot(np.linalg.inv(cross(X)))
    se = np.sqrt(np.diag(vb))
    tstat = b.T/se
    pval = norm.cdf(-np.abs(tstat))*2
    return(b,se,tstat,pval)

xmean = [5,4,3]
xsd = [1,0.5,2]
n = 200
b = [1,0,2,3]
nsim = 10000

tstats = np.zeros((nsim,1))
for i in range(nsim):
    x = np.random.normal(xmean,xsd,size=(n,3))
    x = np.hstack((np.ones((n,1)),x))
    y = x.dot(b).reshape((n,1)) + (np.random.normal(0,np.abs(x[:,1])**2,size=(1,n)).T)
    y = y.reshape((n,))
    tstats[i] = least_squares(x,y)[2][1]
tstats.mean()
(np.abs(tstats)>1.96).mean()
