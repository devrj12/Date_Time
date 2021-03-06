#!/usr/bin/env python
# LT

import ipdb
import glob
import os
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# os.chdir('/home/dev/Desktop/Test_Path1/2020-11-16-loc-copy')


for filename in sorted(os.listdir('/home/dev/Desktop/Test_Path1')):
    print(filename)
    if filename.endswith("-copy"):
        path = os.path.join('/home/dev/Desktop/Test_Path1/', filename)
        path
        os.chdir(path)

        fnames = glob.glob('*.png')
        fnames.sort()

        f_new = [] #string
        for i, fname in enumerate(fnames):
            f_new.append(fnames[i][17:36])
            

        f_new1 = [] #datetime
        dT = []
        for i, fname1 in enumerate(f_new):
            f_new1.append(datetime.strptime(f_new[i], '%Y-%m-%d-%H-%M-%S'))
            hours = f_new1[i].hour + f_new1[i].minute/60. + f_new1[i].second/3600.
            dT.append(hours)
          


        plt.plot(dT,f_new1,'.b') # plot year-month-day (y-axis) vs hours (dT : x-axis) 
        ax = plt.gca()
         
        #xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        xfmt = mdates.DateFormatter('%H:%M:%S')
        yfmt = mdates.DateFormatter('%Y-%m-%d')
        #ax.xaxis.set_major_formatter(xfmt)
        ax.yaxis.set_major_formatter(yfmt)


#ax.grid(which='major', axis='both', linestyle='-')
plt.title("Chirp-sounding Observations")
plt.xlabel("Local-Time (LT)")
plt.ylabel("Year-Mon-Day")
plt.show()



