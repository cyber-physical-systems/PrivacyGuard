import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
import glob
import csv
import operator

output_path = ''

date = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20']
label = {}
activity = []
num = 0
# threshold = [1,2,3,5,7,10,15,20,25,30,35,40,45,50,55,60,120]
threshold = [3]
for thres in threshold:

    for i in date:

        with open(output_path + str(i) + ".csv") as f:

            reader = csv.DictReader(f)
            for row in reader:
                if row['label'] not in activity:
                    label[row['label']] = 1
                    activity.append(row['label'])

                else:
                    label[row['label']] = label[row['label']] + 1

    # for ac in activity:
    #     if ac != '' :

    # #     if label[ac] != 1:

    #         num = num + label[ac]

    label_sort = dict(sorted(label.items(), key=operator.itemgetter(1), reverse=True))
    #     print(label_sort)

    #     # print(num)
    for key, value in label_sort.items():
        with open(output_path + 'sorted_activity_' + str(thres) + '.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([key, value])
        csvfile.close()




