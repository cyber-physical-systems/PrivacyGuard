import pandas as pd
import numpy as np
import seaborn as sns
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
import glob
import csv

path = ''
devices_In = ['AmazonIn', 'SwitchIn', 'PrinterIn',
              'BabyIn', 'MotionIn', 'scaleIn', 'LIFXIn',
              'WeatherIn', 'SpeakerIn', 'PlugIn',
              'iPhoneIn', 'AndroidIn', 'LaptopIn',
              'MacBookIn', 'InsteonIn', 'DropcamIn',
              'SmartCamIn', 'TabIn',
              'WelcomeIn', 'DayIn']
devices_Out = ['AmazonOut', 'SwitchOut', 'PrinterOut',
               'BabyOut', 'MotionOut', 'scaleOut', 'LIFXOut',
               'WeatherOut', 'SpeakerOut', 'PlugOut',
               'iPhoneOut', 'AndroidOut', 'LaptopOut',
               'MacBookOut', 'InsteonOut',
               'DropcamOut', 'SmartCamOut', 'TabOut',
               'WelcomeOut', 'DayOut']

date = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20']

for i in date:

    with open(path + str(i) + ".csv") as f:

        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        print(len(fieldnames))

        for row in reader:
            total_in = 0
            total_out = 0

            for device_In in devices_In:
                total_in = total_in + int(float(row[device_In]))
            if total_in != int(float(row['TotalIn'])):
                with open('sum_check.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([row['TIME'], (total_in - int(float(row['TotalIn'])))])
                csvfile.close()

            for device_Out in devices_Out:
                total_out = total_out + int(float(row[device_Out]))
            if total_out != int(float(row['TotalOut'])):
                with open('sum_check.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([row['TIME'], (total_out - int(float(row['TotalOut'])))])
                csvfile.close()
















