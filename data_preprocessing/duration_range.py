import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
import glob
import csv

path = ''
output_path = ''

date = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20']


devices = ['Amazon', 'Baby', 'Weather', 'Things', 'Smoke', 'Movement', 'NonIoT',
           'Print', 'CheckBodyCondition', 'ControlLights', 'MultiMedia']

# label = {}
# activity = []
time = 0
for device in devices:

    device_max = 0
    N = 0

    for i in date:

        num = 0

        with open(path + str(i) + ".csv") as f:

            reader = csv.DictReader(f)
            for row in reader:

                if int(float(row[device])) > 0:
                    num = num + 1
                    if num > N:
                        N = num
                        time = row['TIME']

                else:
                    num = 0

    with open(output_path + 'sliding_window.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([device, N, time])
    csvfile.close()





