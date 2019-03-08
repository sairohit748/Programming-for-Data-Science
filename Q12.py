# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 03:02:11 2018

@author: Rohit
"""
### Import np and statsmodel packages for running regression

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
np.random.seed(100)
'''## Define variables to be used in the program
Svec =[0.5,1,1.5]
nsim =1000
Muvec=[1,2,3,4,5]
Sxvec=[0.5,1,1.5]
Tvec = [10,25,50,100,250]
b0=0.5
b1=1
t=50
#nvec = [1,2,3,5,10]
#holding_place = np.zeros((nsim,len(Tvec),len(nvec)))   ## for storing R squared of different combination of T and n
#holding_place_1 = np.zeros((nsim,len(Tvec),len(nvec)))
for mdx,mu_x in enumerate(Muvec):
    for snx,sig_x in enumerate(Sxvec):
        for sdx,sig in enumerate(Svec):
            for tdx,T in enumerate(Tvec):
                for isim in range(nsim):
                    e = np.random.normal(0,sig,size=(T,1))
                    x = np.random.normal(mu_x,sig_x,size=(T,1))
                    x_t=np.transpose(x)
                    y=(b1*x_t)+e
                    x_t = sm.add_constant(x)
                    model_1 = smf.OLS(y,x_t).fit()
  ''''
### Cross Validation  Complete code as explained by professor
sig=0.5
T=50
bigT=T*2
mu_x=1
sig_x=2
k=4
nsim = 1000
kvec = [2,4,8,10]
Tvec = [50]
outp =np.zeros((nsim,len(Tvec),len(kvec),5))
for tdx,T in enumerate(Tvec):
    bigT = T*2
    for kdx,k in enumerate(kvec):
        for isim in range(nsim):
            e = np.random.normal(0,sig,size=(bigT,1))
            x = np.random.normal(mu_x,sig_x,size=(bigT,1))
            x_t=x
            y=b0+(b1*x_t)+e
            x_t = sm.add_constant(x)
            sample = np.random.permutation(bigT)
            train = sample[:int(bigT/2)]
            test = sample[int(bigT/2):]
            ytr = y[train]
            xtr = x_t[train]
            model=smf.OLS(y[train],x_t[train]).fit()
            mspe_true = ((y[test]-model.predict(x_t[test]))**2).mean()
            sample = np.random.permutation(T)
            mspe =np.zeros(k)
            for j in range(k):
                train_l = sample[:int((k-1-j)*T/k)]
                train_u = sample[int((k-j)*T/k):]
                train = np.concatenate((train_l,train_u),0)
                test = sample[int((k-1-j)*T/k):int((k-j)*T/k)]
                model = smf.OLS(ytr[train],xtr[train]).fit()
                mspe[j] = ((ytr[test]-model.predict(xtr[test]))**2).mean()
            mspe_cv = mspe.mean()
            outp[isim,tdx,kdx] = np.array((T,k,mspe_true,mspe_cv,mspe_cv-mspe_true))

outp[:,:,:].mean(0)

mspe



k=4
mspe =np.zeros(k)
for j in range(k):
    train_l = sample[:int((3-j)*T/k)]
    train_u = sample[int((4-j)*T/k):]
    train = np.concatenate((train_l,train_u),0)
    test = sample[int((3-j)*T/k):int((4-j)*T/k)]
    model = smf.OLS(y[train],x[train]).fit()
    mspe[j] = ((y[test]-model.predict(x[test]))**2).mean()
mspe


## Bootstrapping- Roadmap
bvec = [-0.1,0,0.1,0.25]
reject = 0
T=50
nsim = 1000
b0 = 1
for bdx,b1 in enumerate(bvec):
    reject = 0
    reject_boot = 0
    reject_both = 0
    for isim in range(nsim):
        e = np.random.normal(0,sig,size=(T,1))
        x = np.random.normal(mu_x,sig_x,size=(T,1))
        y=b0+(b1*x)+e
        x = sm.add_constant(x)
        model_orig=smf.OLS(y,x).fit()
        if model_orig.pvalues[1]<0.05: reject+=1
        # Create confindence interval for b1
        for boot in boots:
            # Create a resample index
            model = smf.OLS(y[resamp],x[resamp]).fit()
            ci = model.params[1]
        ci.sort()
        ci_lower = ci[int(boots*0.025)]
        ci_upper = ci[int(boots*0.975)]
        if 0>ci_lower and 0<ci_upper: reject_boot+=1
        if 0>ci_lower and 0<ci_upper and model_orig.pvalues[1]<0.05: reject_both+=1

    print(b1,reject,reject/nsim)
