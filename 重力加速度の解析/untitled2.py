import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/fun1018139/Desktop/実験 2/10°　おもり3.csv')

x=df['time']
y=df['radians']
z=df['acc']

fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))

axL.set_xlabel("time")
axL.set_ylabel("radians")
axL.scatter(x,y)

axR.set_xlabel("time")
axR.set_ylabel("acc")
axR.set_xlim(12.5,25.0)
axR.set_ylim(0.2,0.5)
axR.scatter(x,z)

#plt.plot(x, 0.05*np.sin(x*4.38+0.6)+0.35,'r')


plt.show()
