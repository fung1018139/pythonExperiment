# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


if __name__ == '__main__':

    data = np.loadtxt("/Users/fun1018139/Documents/複雑系科学実験/2019実験/python/Expeirment1.csv",#計測データのパスを指定する(これは各自の保存場所に変更)
                      delimiter = ",",                                      #計測データ内の区切り文字はカンマ
                      skiprows = 1,                                         #横1行目は無視
                      usecols = 1,                                          #縦1列目は無視
                      encoding = "utf-8") 
    data_min = data.min()                                                   #計測データの最小値
    data_max = data.max()                                                   #計測データの最大値

    mean = np.average(data)                                                 #計測データの平均   
    std_div = np.std(data)                                                  #計測データの標準偏差
    
    X_axis = np.arange(data_min, data_max, 0.01)   
                       #グラフのX軸(データの最小最大の間を0.01で刻む)
    ####ここまででグラフの材料は揃ったので以下でグラフの描画と整形を行う################
    
    plt.rcParams['figure.figsize'] = 10,6
    plt.rcParams['xtick.direction'] = 'in'                                  #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'                                  #y軸

    plt.xlabel('interval [sec]')                                            #x軸のタイトル
    plt.ylabel('frequency [times]')                                         #y軸のタイトル
    
    
    ret = plt.hist(data, range = (data_min, data_max),
                   label = 'hist')    #ヒストグラム描画とヒストグラムを構成する情報(各階級値とその出現回数)を記録
    
    bins_width = ret[1][1] - ret[1][0]                                      #自動で決まった各階級の幅を取得
    magnification = bins_width * np.sum(ret[0])                             #各階級の幅と計測回数の積から倍率を計算
    
    norm_plot = norm.pdf(X_axis, mean, std_div) * magnification             #計測データの平均と標準偏差から正規分布の数列を作る
                                                                            #単に標準正規分布を描画すると面積が１になっているので先程計算した倍率でヒストグラムの面積とそろえる
      
    plt.plot(X_axis, norm_plot, color='r',                                  #正規分布描画
             label = 'normal_distribution')         
                              
    plt.vlines([mean],0,50,"k",
               label='mean')
    plt.plot(mean+std_div,19.4,mean-std_div,19.4,marker = '.',
             label = 'std_div')
   
    plt.text(data_min + 0.01, norm_plot.max(),                              #グラフにテキストを追加 x座標は計測データの最小値付近 y座標は標準正規分布の最大値付近
             "mean = %1.3f" % mean,                                         #内容は先ほど計算した平均値の小数点以下第3位まで
             size = 15,                                                     #フォントサイズは15(任意)
             color = "k")          
                                   #色は黒 
    
    plt.text(data_min , norm_plot.max()-1.8,                        #グラフにテキストを追加 上のテキストと重ならないよう少しずらす
             "std_div = %1.3f" % std_div, 
             size = 15,
             color = "k")
  
   

    plt.legend()                                                            #グラフの凡例を表示(先程plt.plot内で設定したlabel)
    plt.show()
