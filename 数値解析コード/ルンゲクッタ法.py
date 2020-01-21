#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:16:11 2019

@author: fun1018139
"""

import matplotlib.pyplot as plt
#(1)の条件
r=200.0
l=500.0*(10**-3)
c=1.0*(10**-6)
e=5.0
#（２）の条件 
#r2=450.0
#l2=500*(10**-3)
#c2=10*(10**-6)
#e2=5.0

#条件式
def con(l,r,c):
    return 1/(l*c)-((r/l)/2)**2

con=con(l,r,c)

#微分するべき関数を書く
def f1(t,q,i):
    return i    #dq/dt=iの微分方程式。

def f2(t,q,i): 
        return (-r/l)*i-(1/(l*c))*q+(e/l)   #di/dt=-R/L-1/LCq+LEの微分方程式。
class Analysis:
#初期値の設定
    DELTA_T = 0.000001#刻み幅
    MAX_T = 0.02#時間の上限
    q=0
    i1=-0.0
    i2=-0.0
    t = 0.0 # tの初期値
    q_hist = [q]
    i1_hist = [i1]
    i2_hist = [i2]
    t_hist = [t]
    
#メソッド１〜条件式〜
    def con(l,r,c):
        return 1/(l*c)-((r/l)/2)**2
#メソッド２〜微分方程式〜
 #微分するべき関数を書く
    def f1(t,q,i):
        return i    #dq/dt=iの微分方程式。
    def f2(t,q,i):
        return (-r/l)*i-(1/(l*c))*q+(e/l)   #di/dt=-R/L-1/LCq+LEの微分方程式。
#メソッド３〜ルンゲクッタ法の利用〜
    
    
