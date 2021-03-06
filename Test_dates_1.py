#!/usr/bin/env python

import ipdb
import glob
import os
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# os.chdir('/home/dev/Desktop/Test_Path1/2020-11-16-loc-copy')


for filename in sorted(os.listdir('/home/dev/Desktop/Test_Path')):
    print(filename)
    if filename.endswith("-copy"):
        path = os.path.join('/home/dev/Desktop/Test_Path/', filename)
        path
        os.chdir(path)

        fnames = glob.glob('*.png')
        fnames.sort()

        f_new = []  # datetime
        dT = []
        for i, fname in enumerate(fnames):
            f_new.append(datetime.utcfromtimestamp(int(fnames[i][17:27])))
            hours = f_new[i].hour + f_new[i].minute/60. + f_new[i].second/3600.
            dT.append(hours)

        #ipdb.set_trace()
        f_new1 = []  # datetime
        for x in range(len(f_new)):
            #f_new1.append(datetime.strptime('20-' + datetime.strftime(f_new[x], '%m-%d'), '%y-%m-%d'))
            f_new1.append(datetime.strptime(datetime.strftime(f_new[x], '%Y-%m-%d'), '%Y-%m-%d'))

        plt.plot(dT, f_new1, '.b')
        ax = plt.gca()

        #xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        xfmt = mdates.DateFormatter('%H:%M:%S')
        yfmt = mdates.DateFormatter('%Y-%m-%d')
        # ax.xaxis.set_major_formatter(xfmt)
        ax.yaxis.set_major_formatter(yfmt)


plt.title("Chirp-sounding Observations")
plt.xlabel("Universal-Time-Coordinated (UTC)")
plt.ylabel("Year-Mon-Day")
plt.show()


