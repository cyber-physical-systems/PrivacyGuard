import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
import glob
import csv
import os

path = ''
date = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20']
# threshold = [2000,2500,3000]
threshold = [2000]

for thres in threshold:

    peak_path = ''
    if not os.path.exists(peak_path):
        os.makedirs(peak_path)

    # num = 0
    # threshold = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000,50000,55000,60000,65000,70000]
    # threshold = [1000,1500,2000,2500,3000,3500,4000,5000,6000,7000,8000,9000,10000]
    distance = [3]
    for dist in distance:

        for i in date:

            df = pd.read_csv(path + i + '.csv')
            df = df['TotalIn']

            data = np.array(df)

            list_peak = []
            peaks, _ = find_peaks(data, height=thres, distance=dist)
            for peak in peaks:
                list_peak.append(int(peak))

            with open(peak_path + 'In_' + str(dist) + '.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([i, list_peak])
            #             print(i,list_peak)
            csvfile.close()




