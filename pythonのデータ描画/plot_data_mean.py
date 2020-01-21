# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    data = np.loadtxt("/Users/fun1018139/Documents/複雑系科学実験/python/Expeirment1.csv",   #計測データのパスを指定する(これは各自の保存場所に変更)
                      delimiter = ",",                                      #計測データ内の区切り文字はカンマ
                      skiprows = 1,                                         #横1行目は無視
                      usecols = 1,                                          #縦1列目は無視
                      encoding = "utf-8") 
    
    mean = np.average(data)                                                 #計測データの平均   
    div = data - mean                                                       #計測データの偏差(平均からの差)
    
    X_axis = np.arange(0, len(data))                                        #グラフのX軸(今回は計測データそのものをプロットするので計測データ数と同じ要素数) 
    
    ####ここまででグラフの材料は揃ったので以下でグラフの描画と整形を行う################
    
    plt.rcParams['xtick.direction'] = 'inout'                                  #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'                                  #y軸

    plt.xlabel('trial number [time]')                                       #x軸のタイトル
    plt.ylabel('interval [sec]')                                            #y軸のタイトル

    plt.plot(X_axis, data, color='b',                                       #計測データ描画
             label = 'measured_data')
    
    plt.hlines(mean,0, 100, "n", linestyle=":",                             #平均値の水平線描画 第一引数の値を０から１００まで引く
               lw=3, label = "mean = %1.3f" % mean)

    plt.legend()                                                            #グラフの凡例を表示(先程plt.plot内で設定したlabel)
    plt.show()
