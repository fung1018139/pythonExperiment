import matplotlib.pyplot as plt
#import numpy as np
#import math

#（１）の条件(conが正の時)
#r=200.0
#l=500.0*(10**-3)
#c=1.0*(10**-6)
#e=5.0
#（２）の条件（conが負の時）
r=100.0
l=1*(10**-3)
c=1*(10**-6)
e=2.0



DELTA_T = 0.0001#刻み幅
MAX_T =200#時間の上限

a=1
b=2
def f1(x,y):
    
    return (x-y)/(x+y)#dq/dt=iの微分方程式。-cos関数を入れればsin関数が描画される。vは引数なので関数を考えてあげないといけない

#def f2(t,q,i): 
#    return (-r/l)*i-(1/(l*c))*q+(e/l)   #di/dt=-R/L-1/LCq+LEの微分方程式。f1はxを微分、f2はvを微分　
    
        


q1=0.01
q2=0
i1=-0.0
i2=-0.0
t = 0.0  # tの初期値

q1_hist =[q1]
q2_hist =[q2]
i1_hist=[i1]
i2_hist=[i2]
t_hist = [t]
    
while t < MAX_T:
    
        k1 = f1(t,q1)
      #  d1 = f2(t,q1,i1)
        
        k2 = f1(t+DELTA_T/2,q1+k1/2)
       # d2 = f2(t+DELTA_T/2,q1+k1/2,i1+d1/2)
        
        k3 = f1(t+DELTA_T/2,q1+k2/2)
        #d3 = f2(t+DELTA_T/2,q1+k2/2,i1+d2/2)
        
        k4 = f1(t+DELTA_T,q1+k3)
        #d4 = f2(t+DELTA_T,q1+k3,i1+d3)
       
        q1 += ((k1+2*k2+2*k3+k4)/6)*DELTA_T
        #i1 += ((d1+2*d2+2*d3+d4)/6)*DELTA_T
        
#        i1_hist.append(i1)
        q1_hist.append(q1)
        t+=DELTA_T 
        t_hist.append(t)
    #上の関数定義のところで具体的な関数を求めてしまえば
    #引数についてルンゲクッタ法を行うだけで良い。 
    #今回は二回微分で求めたい関数が見つかっていない非線形微分方程式なので頭を使わないといけない.
    #append関数とは配列の最後に値を代入する関数。
   
    
   
   

# 数値解のプロット
fig = plt.figure(figsize=(15,8))
ax1 = plt.subplot2grid((2,3),(0,0)) 
#ax2 = plt.subplot2grid((2,3),(0,1))
#ax3 = plt.subplot2grid((2,3),(1,0))
#ax4 = plt.subplot2grid((2,3),(1,1))
#2×2の配列を考え、左上から順に(0,0)(0,1)(1,0)(1,1)と表す。colspanでグラフの横幅を決める。
ax1.plot(t_hist,q1_hist)  
ax1.set_xlabel("t[s]")                     
ax1.grid(True)                      #grid関数はグラフの網を表示するかしないかの関数。

#ax2.plot(t_hist,i2_hist)
#ax2.grid(True)

#ax4.plot(t_hist,x_hist)
#ax4.grid(True)

plt.rcParams['xtick.direction'] = 'in'
                                  #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'                                  #y軸
plt.show()