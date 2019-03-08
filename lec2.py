import csv
import numpy as np
from scipy.stats import norm

file = open('bwght.csv')
file.close()

inmat = []
with open('bwght.csv') as file:
    ## Type what you want here and it works without closing the file
    reader = csv.reader(file)
    for line in reader:
        inmat.append(line)     
print(inmat)
#for rows in inmat:
#    rotr = rows[:4]
#    rote = rows[6:]
#    print(rotr)
#    print(rote)
inmat = [row[:4]+row[6:] for row in inmat] 
##['faminc', 'cigtax', 'cigprice', 'bwght'] <- row[:4]
##['parity', 'male', 'white', 'cigs', 'lbwght', 'bwghtlbs', 'packs', 'lfaminc'] <- row[6:]

print(inmat[0])
for ndx,item in enumerate(inmat[0]):
    print(ndx,item)
#for line in inmat[1:]:
#    print(line)
#    np.array(line,dtype=float)
data = np.matrix(inmat[1:],dtype=float)

x = np.array([1,2,3])
print(x)
y = np.array([4,5,6])
print(y)
print(x+y)
print(x*y)

x = [[1,2],[3,4]]
y = [[5],[8]]
x = np.matrix(x)
y = np.matrix(y)
print(x+y)
print(x*y)
print(np.dot(x,y))
print(x.dot(y)) 
print(np.transpose(x))
print(x.transpose())
print(x.T)
print(x.T*x)
print(x.T*y)
print(x.T.dot(x))
print(x.T.dot(y))
print(np.linalg.inv(x.T.dot(x)))
print(np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y)))
print(np.linalg.solve(X.T.dot(X),X.T.dot(y))) 
# np.linalg.solve(A,b) = inv(A)*b
np.linalg.det(x.T.dot(x))
np.linalg.det(np.linalg.inv(x.T.dot(x)))

y = data[:,3]
y
X = data[:,7]
X
n = len(y)
X = np.ones((n,1))
X = np.hstack((np.ones((n,1)),data[:,7]))
X
def cross(*args):
    x = args[0]
    if len(args)==1:
        y = x
    else:
        y = args[1]
    return(x.T.dot(y))
def ols(X,y):
    return(np.linalg.solve(cross(X),cross(X,y)))
cross(X)
cross(X,X)
cross(X,y)


X = np.hstack((np.ones((n,1)),data[:,7],data[:,0],data[:,5]))
b = ols(X,y)
yhat = X.dot(b)
e = y - yhat 
RSS = cross(e)[0,0]
X_0 = np.ones((n,1))
b_0 = ols(X_0,y)
yhat_0 = X_0.dot(b_0)
e_0 = y - yhat_0 
TSS = cross(e_0)[0,0]
Rsq = 1-(RSS/TSS)
print(b)
print(Rsq)
sig = np.sqrt(RSS/n)
sig
vb = np.linalg.inv(cross(X))*(sig**2)
print(vb)
se = np.sqrt(np.diag(vb))
se
tstat = b.T/se
tstat
pval = norm.cdf(-np.abs(tstat))*2
pval

#data = np.matrix(inmat[1:])
#data = np.hstack((data[:,:4],data[:,6:]))
#data = np.matrix(data,dtype=float)

print(data)


