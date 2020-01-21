#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:08:14 2020

@author: fun1018139
"""
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
#三次元に拡張したコード
fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(azim=30)

d1=pd.read_csv('/Users/fun1018139/Documents/複雑系科学実験/2019実験/2019実験７/data1.csv')
d2=pd.read_csv('/Users/fun1018139/Documents/複雑系科学実験/2019実験/2019実験７/data2.csv')

n1=0.75
n2=0.25
n3=0.25
n4=(5**0.5)/4
A=((n1**2)+(n2**2))**0.5
B=(1-(n4**2))**0.5

x=d1['myaku']
y=d1['myaku2']
z=d1['myaku3']
w=d1['myaku4']
d=d1
p=d2['myaku']
q=d2['myaku2']
r=d2['myaku3']
s=d2['myaku4']

x=p
y=q
z=r
w=s
d=d2

x1=[]
y1=[]
z1=[]
for t in d:
    x1=(n2*x-n1*y)/A
    y1=(n1*n3*x)/(A*B)+(n2*n3*y)/(A*B)-(A/B)*(z)
    z1=(n4/B)*((n1*x)+(n2*y)+(n3*z))-B*w
    
    x1.append(x1)
    y1.append(y1)
    z1.append(z1)
ax.plot(x1,y1,z1,color='r',linewidth=0.5)
    