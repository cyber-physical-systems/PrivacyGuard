import pandas as pd
import os
import glob

read_path = ('')
save_path = ('')

window_size = int(input("Input Window Size: "))

for files in glob.glob(read_path + '*.csv'):

    name = files.split('/')[-1]

    df = pd.read_csv(files)

    df = df[['TIME', 'TotalIn', 'TotalOut', 'Dropcam']]

    for i in range(window_size, 0, -1):
        col_in_name = 'TotalIn_' + str(i)
        df[col_in_name] = 0
    for i in range(1, window_size + 1):
        col_in_name = 'TotalIn' + str(i)
        df[col_in_name] = 0

    for i in range(window_size, 0, -1):
        col_out_name = 'TotalOut_' + str(i)
        df[col_out_name] = 0
    for i in range(1, window_size + 1):
        col_out_name = 'TotalOut' + str(i)
        df[col_out_name] = 0

    print(df.columns)

    for j in range(0 + window_size, len(df) - window_size):
        for k in range(4, 4 + (2 * window_size)):
            temp = df.columns[k]
            window_position = int(temp[-1])
            if k - 4 < window_size:
                df.loc[j, temp] = df.iloc[j - window_position]['TotalIn']
            else:
                df.loc[j, temp] = df.iloc[j + window_position]['TotalIn']
        for k in range(4 + (2 * window_size), len(df.columns)):
            temp = df.columns[k]
            window_position = int(temp[-1])
            if k - (4 + (2 * window_size)) < window_size:
                df.loc[j, temp] = df.iloc[j - window_position]['TotalOut']
            else:
                df.loc[j, temp] = df.iloc[j + window_position]['TotalOut']

    df = df.drop(index=range(len(df) - window_size, len(df)), axis=0)
    df = df.drop(index=range(0, window_size), axis=0)

    df.to_csv(save_path + name, index=False)