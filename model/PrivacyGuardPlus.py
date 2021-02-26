import pandas as pd
import random


def runsize(colum):
    q = pd.Series([df[colum].quantile(0), df[colum].quantile(0.97)])
    insert = df[df[colum] > df[colum].quantile(.97)]
    indexlist = []
    i = 0
    while i < len(insert) - 3:
        if (insert.index[i + 1] - insert.index[i] == 1) and (insert.index[i + 2] - insert.index[i + 1] == 1):
            indexlist.extend([insert.index[i], insert.index[i + 1], insert.index[i + 2]])
            i += 3
        else:
            i += 1
    print(indexlist)
    extend = 0
    for i in range(0, len(df['Size'])-2):
        if extend > 0:
            extend -= 1
            if df.iloc[i][colum] < df.iloc[i - 1][colum]:
                df.loc[i, colum] = df.loc[i - 1, colum]
                continue
        boo = random.randint(0, 60)
        if (boo > 59) and (len(insert) > 0):
            ins = random.randint(0, len(insert) - 3)
            df.loc[i - 2, colum] = insert.iloc[ins][colum]
            df.loc[i - 1, colum] = insert.iloc[ins + 1][colum]
            df.loc[i, colum] = insert.iloc[ins + 2][colum]

        if (df.iloc[i][colum] > q[0]) and (df.iloc[i][colum] < q[1]):
            df.loc[i, colum] = q[1]
            extend = random.randint(0, 2)

        if df.iloc[i][colum] > q[1]:
            df.loc[i, colum] = df.iloc[i][colum] * random.uniform(1.1, 1.3)
            extend = random.randint(0, 2)
    df[[colum]] = df[[colum]].astype(int)
    df.dropna(inplace=True)
    print(df)


def rundevice(colum):
    print(colum)
    q = pd.Series([df[colum].quantile(0), df[colum].quantile(0.96)])
    insert = df[df[colum] > df[colum].quantile(.96)]
    indexlist = []
    i = 0
    while i < len(insert) - 2:
        if (insert.index[i + 1] - insert.index[i] == 1):
            indexlist.extend([insert.index[i], insert.index[i + 1]])
            i += 2
        else:
            i += 1
    print(indexlist)
    extend = 0
    for i in range(0, len(df[colum])-2):
        if extend > 0:
            extend -= 1
            if df.iloc[i][colum] < df.iloc[i - 1][colum]:
                df.loc[i, colum] = df.loc[i - 1, colum]
                continue
        boo = random.randint(0, 60)
        if (boo > 59) and (len(insert) > 0):
            ins = random.randint(0, len(insert) - 2)
            df.loc[i - 1, colum] = insert.iloc[ins][colum]
            df.loc[i, colum] = insert.iloc[ins + 1][colum]

        if (df.iloc[i][colum] > q[0]) and (df.iloc[i][colum] < q[1]):
            df.loc[i, colum] = q[1]
            # extend = random.randint(0, 2)

        if df.iloc[i][colum] > q[1]:
            df.loc[i, colum] = df.iloc[i][colum] * random.uniform(1.1, 1.3)
            extend = random.randint(0, 2)
    df[[colum]] = df[[colum]].astype(int)
    df.dropna(inplace=True)
    print(df)


df = pd.read_csv('C:/penv/PycharmProjects/PGOnline/data/unswactivity/new/original.csv')
col = df.columns.values.tolist()
runsize('Size')
'''for j in range(2, len(col)-1):
    rundevice(col[j])
for j in range(1, len(col)):
    df[[col[j]]] = df[[col[j]]].astype(int)'''
df.to_csv('C:/penv/PycharmProjects/PGOnline/data/unswactivity/new/plus97.csv', index=False)
