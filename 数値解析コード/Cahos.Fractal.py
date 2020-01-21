#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:58:46 2019

@author: fun1018139
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
#import math
#初期状態
C1=10*10**-9
C2=10*10**-8
L=2.2*10**-2
m0=-4*10**-4#単位は１/Ω
m1=-8*10**-4
B=1.0
R=2104.2#1800から2200の間でランダムに決める



#def g(v):
#    return m0*v+0.5*(m1-m0)*(abs(v+B)-abs(v-B))

t = 0.0  # tの初期値
DELTA_T = 0.001#刻み幅
MAX_T = 10000#時間の上限

#無次元化するための変数
t=t/(R*C2)
r=C2/C1
a=m1*R
b=m0*R
n=(C2*(R**2))/L

def dxdt(t,x,y):
    f=b*x+(b-a)*(abs(x-1)-abs(x+1))*(1/2)
    return r*(y-x-f)
#dx/dt=r(y-x-f(x))の微分方程式。

def dydt(t,x,y,z): 
    return x-y+z
#dy/dt1=x-y+zの微分方程式。dv1dtはxを微分、dv2dtはvを微分　
def dzdt(t,y):
    return -n*y
#dz/dt1=-nyの微分方程式
v1=0.01#なぜかうまくいくから0.01
v2=0
i=0.0

v1_hist=[v1]
v2_hist=[v2]
i_hist=[i]
#初期値の設定
t_hist = [t]
#ルンゲクッタ法
while t< MAX_T:
    k1 = DELTA_T*dxdt(t,v1,v2)
    l1 = DELTA_T*dydt(t,v1,v2,i)
    m1 = DELTA_T*dzdt(t   ,v2)
    
    k2=DELTA_T*dxdt(t+DELTA_T/2,v1+k1/2,v2+l1/2)
    l2=DELTA_T*dydt(t+DELTA_T/2,v1+k1/2,v2+l1/2,i+m1/2)
    m2=DELTA_T*dzdt(t+DELTA_T/2        ,v2+l1/2)
    
    k3=DELTA_T*dxdt(t+DELTA_T/2,v1+k2/2,v2+l2/2)
    l3=DELTA_T*dydt(t+DELTA_T/2,v1+k2/2,v2+l2/2,i+m2/2)
    m3=DELTA_T*dzdt(t+DELTA_T/2        ,v2+l2/2)
    
    k4=DELTA_T*dxdt(t+DELTA_T,v1+k3,v2+l3)
    l4=DELTA_T*dydt(t+DELTA_T,v1+k3,v2+l3,i+m3)
    m4=DELTA_T*dzdt(t+DELTA_T      ,v2+l3)
    
    v1+=(k1+2*k2+2*k3+k4)/6
    v2+=(l1+2*l2+2*l3+l4)/6
    i +=(m1+2*m2+2*m3+m4)/6
    
    v1_hist.append(v1)
    v2_hist.append(v2)
    i_hist.append(i)
    t+=DELTA_T 
    t_hist.append(t)
    #上の関数定義のところで具体的な関数を求めてしまえば
    #引数についてルンゲクッタ法を行うだけで良い。 
    #今回は二回微分で求めたい関数が見つかっていない非線形微分方程式なので頭を使わないといけない.
    #append関数とは配列の最後に値を代入する関数。
   
    
   
   

# 数値解のプロット
fig1 = plt.figure()
ax = Axes3D(fig1)
#fig = plt.figure(figsize=(20,16))
#ax1 = plt.subplot2grid((3,2),(0,0)) 
#ax2 = plt.subplot2grid((3,2),(1,0))
#ax3 = plt.subplot2grid((3,2),(2,0))
#ax4 = plt.subplot2grid((2,3),(1,1))
#2×2の配列を考え、左上から順に(0,0)(0,1)(1,0)(1,1)と表す。colspanでグラフの横幅を決める。
ax.plot(v1_hist,v2_hist,i_hist,linewidth=0.01)
ax.set_xlabel("v1[V]")
ax.set_ylabel("v2[V]")


#ax2.plot(t_hist,v1_hist,linewidth=0.9)
#ax2.set_xlim(0,100)
#ax3.plot(t_hist,v2_hist,linewidth=0.9)
#ax3.set_xlim(0,100)
#grid関数はグラフの網を表示するかしないかの関数。
plt.rcParams['xtick.direction'] = 'in'
                                  #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in' #y軸
plt.show()