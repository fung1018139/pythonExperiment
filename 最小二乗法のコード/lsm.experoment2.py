# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

G = np.array([0.001,	0.000333333,0.001219512,0.001098901])           #実験データ : 抵抗の逆数(コンダクタンス,Gで表す)
r_V = np.array([0.165289256,0.148148148,0.170068027,0.168350168])         #実験データ : 測定した電圧の逆数
data_min=G.min()
data_max=G.max()
############### 与えられた各実験データをベクトルと考える
G_ = np.array([G,np.ones(len(G))])  #実験データのベクトルに単位ベクトルを結合(足し算ではない)
G_t = G_.T                           #上で作ったG_ベクトルを転置しておく
a,b = np.linalg.lstsq(G_t,r_V,rcond=None)[0]   #最小二乗解を G_t * x - r_V となるベクトル x を求めることで解いてくれる。x = (a,b)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.xlabel('G(1/Ω)')
plt.ylabel('r_V(1/V)')
plt.xlim(0.0001,0.00123)
plt.ylim(0.14,0.18)


print('内部抵抗')
print(a/b)
print('起電力')
print(1/b)
print('電圧と起電力の比')
print(b/(b+a))


plt.scatter(G,r_V,color="k") #x座標G,y座標r_Vの点を全要素で描画します(散布図)
plt.plot( [0, np.max(G)+0.08],[b, a * (np.max(G)+0.08) +b]) #x座標[0~Gの最大値まで],y座標[b ~ (a * x + b)]までの直線を引く
plt.show()