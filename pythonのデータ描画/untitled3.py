#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:22:55 2019

@author: fun1018139
"""

import csv
import matplotlib.pyplot as plt

fn = '/Users/fun1018139/Desktop/101.csv'

with open(fn, mode='r', newline='') as f_in:
    reader = csv.reader(f_in)
    data_array = [row for row in reader]

plot_x = []
plot_y1 = []
plot_y2 = []
for i in data_array:
    plot_x.append(i[2])
    plot_y1.append(i[3])
    plot_y2.append(i[4])

plt.plot(plot_x, plot_y1)
plt.plot(plot_x, plot_y2)
plt.show()