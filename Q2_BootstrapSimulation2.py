# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:34:51 2018

@author:
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
np.random.seed(100) 
pd.set_option('display.max_columns',10)
pd.set_option('display.width',None)
## Betas, Bootstraps are variable
bvec=[-0.1,0,0.1,0.2]
T=100
nsim = 1000
b0 = 1
boots=[10,20,30,50]
sig=0.5
mu_x=1
outp =np.zeros((len(bvec),len(boots),6))
outp.shape
for bdx,b1 in enumerate(bvec):      
    for btx,boot in enumerate(boots):
        reject_boot = 0
        reject_both = 0
        reject_orig=0
        for isim in range(nsim):
            count+=1
            e = np.random.normal(0,sig,size=(T,1))
            x = np.random.normal(mu_x,sig,size=(T,1))
            y=b0+(b1*x)+e
            x = sm.add_constant(x)
            model_orig=smf.OLS(y,x).fit()
            # Create confindence interval for b1
            ci=np.zeros(int(boot))
            for b in range(boot):  ## Bootstrapping to find CI
                # Create a resample index
                resamp=np.random.randint(T, size=int(0.5*T)) #Re-sampling with replacement
                model = smf.OLS(y[resamp],x[resamp]).fit()
                ci[b] = model.params[1]
                #print(model.params[1])
            ci.sort()
            ci_lower = ci[int(boot*0.025)]
            ci_upper = ci[int(boot*0.975)]
            ## Empirical t-tests - Reject Null when CI follows a trend
            if not(0>=ci_lower and 0<=ci_upper): reject_boot+=1
            if not(0>=ci_lower and 0<=ci_upper) and model_orig.pvalues[1]<0.05: reject_both+=1
            if model_orig.pvalues[1]<0.05: reject_orig+=1
        outp[bdx,btx] = np.array((b1,boot,nsim,reject_orig,reject_boot,reject_both))
## Convert to Dataframe for analysis
df=pd.DataFrame(np.vstack(outp))
df.columns=['Betas','Bootstraps','No_of_Simulation','Reject_Actual','Reject_Bootstrap','Reject_Both']
df['Power of the Test(when Beta=0, its Size of Test)']=(df['Reject_Both']/df['No_of_Simulation'])*100
