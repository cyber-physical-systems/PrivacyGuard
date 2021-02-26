import pandas as pd
import time
import os


read_path = 'C:/penv/PrivacyGuard/merged143/csv'
save_path = 'C:/penv/PrivacyGuard/merged143/csv/cleaned/'
os.chdir(read_path)
csv_name_list = os.listdir()

print(csv_name_list)
for i in range(0, 9):
    df = pd.read_csv(csv_name_list[i])
    x = [0, 2, 3, 4, 6]
    df = df.drop(df.columns[x], axis=1)
    df = df.applymap(str)
    df['Timestamp'] = df['Time'].apply(lambda x: time.mktime(time.strptime(x, '%Y-%m-%d %H:%M:%S.%f')))
    df = df[~df['eth.dst'].str.contains('Broadcast')]
    print(df)
    df.to_csv(save_path + str(i + 1) + '.csv', index=False)
