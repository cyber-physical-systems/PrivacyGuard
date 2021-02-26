import pandas as pd
import os

read_path = 'C:/penv/IPSN/data/groundtruth/PG/PrivacyGuard'
os.chdir(read_path)
file_list = os.listdir()

j = -1
temp = 0
for k in file_list:
    df = pd.read_csv(k)
    j += 1
    print(k, j)
    labelin = pd.read_csv('C:/penv/IPSN/data/groundtruth/In_3.csv', header=None)
    labelout = pd.read_csv('C:/penv/IPSN/data/groundtruth/Out_3.csv', header=None)
    labelin = labelin.drop([0], axis=1)
    labelout = labelout.drop([0], axis=1)
    inn = labelin[1][j]
    inn = inn[1:-1]
    inn = inn + ','

    out = labelout[1][j]
    out = out[1:-1]

    arr = inn + out
    arr = arr.split(',')

    df['label'] = None
    backup = df.columns
    cols = ['Time', 'TotalIn', 'TotalOut', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'Label']
    df.columns = cols
    #print(df.columns[3:-1])
    temp += len(arr)
    for i in range(0, len(arr)):
        if df['Label'][int(arr[i])] != None:
            continue
        for columns in df.columns[3:-1]:
            if df[columns][int(arr[i])] == 1:
                if df['Label'][int(arr[i])] == None:
                    df['Label'][int(arr[i])] = columns
                else:
                    df['Label'][int(arr[i])] += columns
        #print(arr[i], df['TotalIn'][int(arr[i])], df['Label'][int(arr[i])])
    df.columns = backup
    print(df)
    df.to_csv('C:/penv/IPSN/data/groundtruth/PG/RTP/' + k, index=False)