# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:59:55 2018

@author: Sandy
"""
## Import required packages
import sqlite3
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS
from linearmodels.panel import PooledOLS
from linearmodels.panel import BetweenOLS
from linearmodels.panel import RandomEffects
np.random.seed(10)
os.getcwd()
path='D:\\University of Texas at Dallas - Masters\\UTD - Summer Semester 2018\\BUAN6340 - Programming for Data Science\\Assignments\\Third'
os.chdir(path)
## Connect to Wooldridgedb
con = sqlite3.connect("wooldridge.db")
c = con.cursor()
c.execute('SELECT * FROM jtrain')
## Read data into a Pandas Dataframe
jtrain = pd.read_sql('SELECT * FROM jtrain',con)
jtrain.head()
jtrain[jtrain['grant']==1].count()
scrap_panel_pool = smf.ols('scrap~d88+d89+grant+grant_1',data=jtrain).fit()
scrap_panel_pool.summary()
jtrain2=jtrain
jtrain2[:5]
## Define the ID and Time column for Panel Regression
jtrain2=jtrain2.set_index(['fcode','year'])
print(jtrain2.head(5))
exog_vars=['d88','d89','grant','grant_1']
grant_vars=['grant']
exog=sm.add_constant(jtrain2[exog_vars])
grant0=sm.add_constant(jtrain2[grant_vars])
 
## Model Pooled OLS
model_pool=PooledOLS(jtrain2.lscrap,exog)
pooled_res = model_pool.fit()
print(pooled_res)
## Model Fixed Effects -- Entity Effects - True
model_fe=PanelOLS(jtrain2.lscrap,exog,entity_effects=True)
fe_res = model_fe.fit()
print(fe_res)
## Model Fixed Effects -- Entity and Time Effects - True
model_fe=PanelOLS(jtrain2.lscrap,exog,entity_effects=True,time_effects=True)
fe_res = model_fe.fit()
print(fe_res)
## Random Effects Model
model_re=RandomEffects(jtrain2.lscrap,exog)
re_res = model_re.fit()
print(fe_res)
#################################################
## Regress scrap~grant
## Model Pooled OLS
model_pool=PooledOLS(jtrain2.scrap,grant0)
pooled_res = model_pool.fit()
print(pooled_res)
# Model Fixed Effects -- Entity Effects - True
model_fe=PanelOLS(jtrain2.scrap,grant0,entity_effects=True)
fe_res = model_fe.fit()
print(fe_res)
## Model Fixed Effects -- Entity and Time Effects - True
model_fe=PanelOLS(jtrain2.scrap,grant0,entity_effects=True,time_effects=True)
fe_res = model_fe.fit()
print(fe_res)
## Random Effects Model
model_re=RandomEffects(jtrain2.scrap,grant0)
re_res = model_re.fit()
print(fe_res)