#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:25:17 2020

@author: fun1018139
"""

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import matplotlib.animation as animation
 


C1=1.0*10**-8
C2=1.0*10**-7
L=2.2*10**-2
m0=-4*10**-4#単位は１/Ω
m1=-8*10**-4
b=1.0
R=2200#1800から2200の間でランダムに決める


v1=0.0
v2=0.0
i=0.0

t = 0.0  # tの初期値
t1=t/(R*C2)
x=v1/b
y=v2/b
z=(R*i)/b
r=C2/C1
A=m1*R
B=m0*R
n=(C2*R**2)/L
 
# rorenz equation
def lorenz(x, y, z, p=10, r=28, b=8/3):
    f=B*x+0.5*(B-A)*(abs(x-1)-abs(x+1))
    x_dot =  r*(y-x-f)
    y_dot = x-y+z  
    z_dot = -n*y
    return np.array([x_dot, y_dot, z_dot])
 
 
t=0             ##### 初期時間######
dt = 0.01       ##### 微分間隔######
stepCnt = 10000 ######時間ステップ##
delta = 500      ######遅延時間＃####
 
 
# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))
 
# Setting initial values
xs[0], ys[0], zs[0] = (0.1, 0.5, 1.2)
k0=[0,0,0]
k1=[0,0,0]
k2=[0,0,0]
k3=[0,0,0]
 
########x(t)のデータ作成####################
f = open('xdata.csv', 'w') 
csvWriter = csv.writer(f)
# Stepping through "time".
 
 
for i in range(stepCnt-2*delta):
    x,y,z=xs[i],ys[i],zs[i]
 
    k0 = dt * lorenz(x,y,z)
    k1 = dt * lorenz(x+k0[0]/2., y+k0[1]/2., z+k0[2]/2.)
    k2 = dt * lorenz(x+k1[0]/2., y+k1[1]/2., z+k1[2]/2.)
    k3 = dt * lorenz(x+k2[0], y+k2[1], z+k2[2])
 
    dx = (k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0
    dy = (k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0
    dz = (k0[2]+2.0*k1[2]+2.0*k2[2]+k3[2])/6.0
    xs[i+1] = xs[i] + dx
    ys[i+1] = ys[i] + dy
    zs[i+1] = zs[i] + dz
    listData = []   
    listData.append(x)  
    csvWriter.writerow(listData)  
    
    
########x(t-δ)のデータ作成####################
f = open('xdata2.csv', 'w') 
csvWriter = csv.writer(f)
# Stepping through "time".
    
for i in range(stepCnt-delta):
    x,y,z=xs[i],ys[i],zs[i]
 
    k0 = dt * lorenz(x,y,z)
    k1 = dt * lorenz(x+k0[0]/2., y+k0[1]/2., z+k0[2]/2.)
    k2 = dt * lorenz(x+k1[0]/2., y+k1[1]/2., z+k1[2]/2.)
    k3 = dt * lorenz(x+k2[0], y+k2[1], z+k2[2])
 
    dx = (k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0
    dy = (k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0
    dz = (k0[2]+2.0*k1[2]+2.0*k2[2]+k3[2])/6.0
    
    xs[i+1] = xs[i] + dx
    ys[i+1] = ys[i] + dy
    zs[i+1] = zs[i] + dz
    listData2 = [] 
    if i >= 500: 
        listData2.append(x)  
        csvWriter.writerow(listData2)  
 
    
########x(t-2δ)のデータ作成####################
f = open('xdata3.csv', 'w') 
csvWriter = csv.writer(f)
# Stepping through "time".
    
for i in range(stepCnt):
    x,y,z=xs[i],ys[i],zs[i]
    
    k0 = dt * lorenz(x,y,z)
    k1 = dt * lorenz(x+k0[0]/2., y+k0[1]/2., z+k0[2]/2.)
    k2 = dt * lorenz(x+k1[0]/2., y+k1[1]/2., z+k1[2]/2.)
    k3 = dt * lorenz(x+k2[0], y+k2[1], z+k2[2])
 
    dx = (k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0
    dy = (k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0
    dz = (k0[2]+2.0*k1[2]+2.0*k2[2]+k3[2])/6.0
    
    xs[i+1] = xs[i] + dx
    ys[i+1] = ys[i] + dy
    zs[i+1] = zs[i] + dz
    listData3 = []   
    if i >= 1000:
        listData3.append(x)  
        csvWriter.writerow(listData3)  
 
  
###########all-time-datasiries(graph-setting)##################     
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xs, ys, zs,c='m')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
f.close()
plt.show()
plt.savefig("Lorenz-alltimesireies.png")    
 
f = open('xdata.csv', 'rb')
f = open('xdata2.csv', 'rb')
f = open('xdata3.csv', 'rb')
 
##########embedding-theory-datasireis(graph-setting)#############
x = np.loadtxt("xdata.csv", unpack=True)
y = np.loadtxt("xdata2.csv", unpack=True)
z = np.loadtxt("xdata3.csv", unpack=True)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z,c='m')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Takens embedding '$\delta=500$'")
f.close()
plt.show()
plt.savefig("Lorenz-embedding-500.png")