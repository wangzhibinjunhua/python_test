# -*- coding: utf-8 -*-
# @Time    : 2016-12-07 10:46
# @Author  : wzb<wangzhibin_x@foxmail.com>
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import csv
import pandas
import seaborn
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import math
def g_h_filter(data,x0,dx,g,h,dt=1.,pred=None):
    x=x0
    results=[]
    for z in data:
        x_est=x+(dx*dt)
        dx=dx
        if pred is not None:
            pred.append(x_est)
        residual=z-x_est
        dx=dx+h*(residual)/dt
        x=x_est+g*residual
        results.append(x)
    return np.array(results)

my_matrix = np.loadtxt(open('ao_gx_061602.txt',"rb"),delimiter=",",skiprows=0)

test_data = np.loadtxt(open('xy_wf06094.txt',"rb"),delimiter=",",skiprows=0)
print(test_data)

testx=np.arange(0,len(test_data[:,0]),1.0)
testy=np.arange(0,len(test_data[:,1]),1.0)
d=335
print(len(testx))
print(testx)

for i in range(0,len(testx)):
    testx[i]=test_data[:,0][i]*cos(d*3.14159/180)+test_data[:,1][i]*sin(d*3.14159/180)
    testy[i]=test_data[:,1][i]*cos(d*3.14159/180)-test_data[:,0][i]*sin(d*3.14159/180)

print(testx)
#x = np.linspace(0,10,100)
#y_vc=test_data[:,0]
#y = np.sin(x)
#z = np.cos(x**2)
x=my_matrix[:,1]
y=my_matrix[:,2]
#print(y)
z=my_matrix[:,3]

#gx=my_matrix[:,4]
#gy=my_matrix[:,5]
#gz=my_matrix[:,6]
t=np.arange(0,len(y),1)

#xyz=[math.sqrt(x[i]*x[i]+y[i]*y[i]+z[i]*z[i]) for i in range(len(x))]
#print(len(t))
#print(xyz)

fig=plt.figure(figsize=(8,4))

#print(t)
y_filter=np.arange(0,len(y),1)
x_filter=np.arange(0,len(y),1)
z_filter=np.arange(0,len(y),1)
for i in t:
    if(i<7):
        y_filter[i]=y[i]
        x_filter[i] = x[i]
        z_filter[i] = z[i]
    if(i>=7):
        x_filter[i]=x[i]*0.0779+x[i-1]*0.1124+x[i-2]*0.1587+x[i-3]*0.1867+x[i-4]*0.1867+x[i-5]*0.1587+x[i-6]*0.1124+x[i-7]*0.0779
#        print(x[i])
        y_filter[i] = y[i] * 0.0779 + y[i - 1] * 0.1124 + y[i - 2] * 0.1587 + y[i - 3] * 0.1867 + y[i - 4] * 0.1867 + y[
                                                                                                               i - 5] * 0.1587 + \
               y[i - 6] * 0.1124 + y[i - 7] * 0.0779
        z_filter[i] = z[i] * 0.0779 + z[i - 1] * 0.1124 + z[i - 2] * 0.1587 + z[i - 3] * 0.1867 + z[i - 4] * 0.1867 + z[
                                                                                                               i - 5] * 0.1587 + \
               z[i - 6] * 0.1124 + z[i - 7] * 0.0779


#print(y)

#y=y*(-1)
#x=abs(x)
#y=abs(y)

plt.plot(t, y_filter, label="$a-y$",color="red",linewidth=0.5)
plt.plot(t, x_filter, label="$a-x$",color="blue",linewidth=0.5)
plt.plot(t, z, label="$a-z$",color="green",linewidth=0.5)
#plt.plot(t, my_matrix[:,4], label="$gyr-x$",color="y",linewidth=1)
#plt.plot(t, my_matrix[:,5], label="$gyr-y$",color="c",linewidth=1)
#plt.plot(t, my_matrix[:,6], label="$gyr-z$",color="b",linewidth=1)
#plt.plot(test_data[:,0],test_data[:,1] , label="$track$",color="red",linewidth=1)

#plt.plot(testx,testy , label="$track1$",color="blue",linewidth=1)
#qiaodan
#plt.plot(test_data[:,0][0:50],test_data[:,1][0:50] , label="$track$",color="blue",linewidth=1)
#plt.plot(test_data[:,0][50:100],test_data[:,1][50:100] , label="$track$",color="red",linewidth=1)
#plt.plot(test_data[:,0][100:150],test_data[:,1][100:150] , label="$track$",color="green",linewidth=1)
#plt.plot(test_data[:,0][150:200],test_data[:,1][150:200] , label="$track$",color="y",linewidth=1)
#end
#axl = fig.add_subplot(111)
#axl.scatter(test_data[:,0],test_data[:,1],s=100,c='r',marker='o')

#plt.plot(t, y, label="$a-y$",color="red",linewidth=0.5)
#plt.plot(t, x, label="$a-x$",color="blue",linewidth=0.5)
#plt.plot(t, z, label="$a-z$",color="green",linewidth=0.5)

#plt.plot(t, gx, label="$gx$",color="red",linewidth=0.5)
#plt.plot(t, gy, label="$gy$",color="blue",linewidth=0.5)
#plt.plot(t, gz, label="$gz$",color="black",linewidth=1)

#plt.plot(t, xyz, label="$v$",color="black",linewidth=0.5)
plt.xlabel("Time(s)")
plt.ylabel("v")
#plt.title("G-sensor")
#plt.ylim(-20, 20)


plt.xlabel(t)
#plt.xticks(range(0,88))
#plt.yticks(range((int)(min(y)),(int)(max(y))))

plt.legend()
plt.show()









