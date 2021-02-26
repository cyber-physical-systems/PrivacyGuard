import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/penv/PycharmProjects/PrivacyGuard/data/1dayflow/all.csv', header=None)
d_col = ['Time', 'Size']
df.columns = d_col
# df = df.drop(df.index[3600:])
# df.to_csv('/home/keyangyu/Desktop/1hour/raw.csv', index=False, header=False)
df.index = range(len(df))
x = df.index
y1 = df['Size']
plt.plot(x, y1, color='b')
print(df)
q = pd.Series([df['Size'].quantile(0.35), df['Size'].quantile(0.90)])
insert = df[df['Size'] > df['Size'].quantile(.65)]
indexlist = []
i = 0
while i < len(insert) - 3:
    if (insert.index[i + 1] - insert.index[i] == 1) and (insert.index[i + 2] - insert.index[i + 1] == 1) \
            and (insert.index[i + 3] - insert.index[i + 2] == 1):
        indexlist.extend([insert.index[i], insert.index[i + 1], insert.index[i + 2], insert.index[i + 3]])
        i += 4
    else:
        i += 1
print(indexlist)
extend = 0
for i in range(0, len(df)):
    if extend > 0:
        extend -= 1
        if df.iloc[i]['Size'] < df.iloc[i-1]['Size']:
            df.iloc[i]['Size'] = df.iloc[i - 1]['Size']
            continue


    if (i == 47) or (i == 475) or (i == 1196) or (i == 1829) or (i == 3452):
        df.iloc[i - 3]['Size'] = insert.iloc[0]['Size']
        df.iloc[i - 2]['Size'] = insert.iloc[1]['Size']
        df.iloc[i - 1]['Size'] = insert.iloc[2]['Size']
        df.iloc[i]['Size'] = insert.iloc[3]['Size']
    if (i == 185) or (i == 240) or (i == 2894) or (i == 1435) or (i == 3230):
        df.iloc[i - 3]['Size'] = insert.iloc[8]['Size']
        df.iloc[i - 2]['Size'] = insert.iloc[9]['Size']
        df.iloc[i - 1]['Size'] = insert.iloc[10]['Size']
        df.iloc[i]['Size'] = insert.iloc[11]['Size']
    if (i == 942) or (i == 1789) or (i == 712) or (i == 3131) or (i == 2313):
        df.iloc[i - 3]['Size'] = insert.iloc[15]['Size']
        df.iloc[i - 2]['Size'] = insert.iloc[16]['Size']
        df.iloc[i - 1]['Size'] = insert.iloc[17]['Size']
        df.iloc[i]['Size'] = insert.iloc[18]['Size']

    if (df.iloc[i]['Size'] > q[0]) and (df.iloc[i]['Size'] < q[1]):
        df.iloc[i]['Size'] = q[1]

    if df.iloc[i]['Size'] > q[1]:
        df.iloc[i]['Size'] = df.iloc[i]['Size'] * random.uniform(1.1, 1.3)
        extend = random.randint(3, 7)

# df['Time'] = pd.to_datetime(df['Time'], unit='s')

# df = df.resample('1min').sum()
y2 = df['Size']
plt.plot(x, y2, color='r')
plt.show()
df.to_csv('C:/penv/PycharmProjects/PrivacyGuard/data/1dayflow/reshape.csv', index=False, header=False)
# print(df)