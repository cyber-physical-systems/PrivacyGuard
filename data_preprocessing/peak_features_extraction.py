import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
from scipy.stats import variation
import glob
import csv
import os
from scipy.stats import skew

path = ''
output_path = ''
if not os.path.exists(output_path):
    os.makedirs(output_path)

# window_size = [1,2,3,5,7,10,15,20,25,30,35,40,45,50,55,60,120]
window_size = [3]

thres = 2000

date = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20']


def duration_calculation(df_peak, thres, peak, window):
    window_size = window
    peak_duration = 0
    area = 0

    if df_peak[peak] > thres:
        peak_duration = 1
        area = df_peak[peak]
    else:
        peak_duration = 0

    if peak_duration != 0:

        for i in range(1, window_size + 1):

            if df_peak[peak - i] > thres:
                peak_duration = peak_duration + 1
                area = area + df_peak[peak - i] - thres
            else:
                break

        for i in range(1, window_size + 1):

            if df_peak[peak + i] > thres:
                peak_duration = peak_duration + 1
                area = area + df_peak[peak + i] - thres
            else:
                break
    return (peak_duration, area)


#     print(peak_duration)

def activities_top10(thres):
    i = 0
    activity = []
    with open(path + 'sorted_activity_' + str(thres) + ".csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if (i > 0) and (i < 11):
                activity.append(row[0])
            i = i + 1
    return (activity)


# for thres in threshold:
for window in window_size:

    activities = activities_top10(window)
    #     print(activities)
    with open(output_path + str(window) + '_feature.csv', 'w') as new:
        realnames = ['time', 'total_in', 'total_out', 'peak_in_range', 'peak_out_range', 'peak_in_var', 'peak_out_var',
                     'peak_in_std', 'peak_out_std', 'peak_in_duration', 'peak_out_duration',
                     'peak_in_mean', 'peak_out_mean', 'peak_in_area',
                     'peak_out_area', 'peak_in_skew', 'peak_in_skew',
                     'peak_in_cv', 'peak_out_cv', 'label']
        writer = csv.DictWriter(new, fieldnames=realnames)
        writer.writeheader()
    new.close()

    for i in date:

        peaks = []

        df = pd.read_csv(path + str(window) + '/' + str(i) + ".csv")
        df = df[['TIME', 'TotalIn', 'TotalOut', 'label']]
        df_in = df['TotalIn']
        df_out = df['TotalOut']
        lens_df = len(df_in)

        data_in = np.array(df_in)
        data_out = np.array(df_out)

        peaks_in, _ = find_peaks(data_in, height=thres, distance=window)

        for peak_in in peaks_in:
            peaks.append(int(peak_in))

        peaks_out, _ = find_peaks(data_out, height=thres, distance=window)

        for peak_out in peaks_out:
            if peak_out in peaks:
                pass
            else:
                peaks.append(int(peak_out))

        peaks = sorted(peaks)

        for peak in peaks:
            if (peak > window) and (peak < lens_df - window):

                df_peak_in = df_in[peak - window:peak + window + 1]
                df_peak_out = df_out[peak - window:peak + window + 1]

                time = df.iloc[peak]['TIME']
                total_in = df.iloc[peak]['TotalIn']
                total_out = df.iloc[peak]['TotalOut']
                label = df.iloc[peak]['label']

                peak_in_range = df_peak_in.max() - df_peak_in.min()
                peak_in_var = df_peak_in.var()
                peak_in_std = df_peak_in.std()

                peak_out_range = df_peak_out.max() - df_peak_out.min()
                peak_out_var = df_peak_out.var()
                peak_out_std = df_peak_out.std()

                peak_in_mean = df_peak_in.mean()
                peak_out_mean = df_peak_out.mean()

                peak_in_cv = variation(df_peak_in)
                peak_out_cv = variation(df_peak_out)

                peak_in_skew = skew(df_peak_in)
                peak_out_skew = skew(df_peak_out)

                peak_in_duration = duration_calculation(df_peak_in, thres, peak, window)[0]
                peak_out_duration = duration_calculation(df_peak_out, thres, peak, window)[0]

                peak_in_area = duration_calculation(df_peak_in, thres, peak, window)[1]
                peak_out_area = duration_calculation(df_peak_out, thres, peak, window)[1]

                if label in activities:
                    label = activities.index(label)

                    with open(output_path + str(window) + '_feature.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([time, total_in, total_out, peak_in_range,
                                         peak_out_range, peak_in_var, peak_out_var,
                                         peak_in_std, peak_out_std, peak_in_duration, peak_out_duration,
                                         peak_in_mean, peak_out_mean, peak_in_area,
                                         peak_out_area, peak_in_skew, peak_in_skew,
                                         peak_in_cv, peak_out_cv, label])
                    csvfile.close()




