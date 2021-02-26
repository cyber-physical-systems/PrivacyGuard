import pandas as pd
import os
import random

def status(x) :
    return pd.Series([x.quantile(.05), x.quantile(.10), x.quantile(.15), x.quantile(.20), x.quantile(.25),
                     x.quantile(.30), x.quantile(.35), x.quantile(.40), x.quantile(.45), x.quantile(.50),
                     x.quantile(.55), x.quantile(.60), x.quantile(.65), x.quantile(.70), x.quantile(.75),
                     x.quantile(.80), x.quantile(.85), x.quantile(.90), x.quantile(.95), x.quantile(1)],
                     index=['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65',
                            '70', '75', '80', '85', '90', '95', '100'])


def pgplus(dataframe, low, high, denh, denl, j):
    extend = 0
    q = pd.Series([dataframe['Size'].quantile(low / 100), dataframe['Size'].quantile(high / 100)])
    insert = dataframe[dataframe['Size'] > dataframe['Size'].quantile(high / 100)]
    indexlist = []
    i = 0
    while i < len(insert) - 4:
        if (insert.index[i + 1] - insert.index[i] == 1) and (insert.index[i + 2] - insert.index[i + 1] == 1) and (
                insert.index[i + 3] - insert.index[i + 2] == 1) and (insert.index[i + 4] - insert.index[i + 3] == 1):
            indexlist.extend(
                [insert.index[i], insert.index[i + 1], insert.index[i + 2], insert.index[i + 3], insert.index[i + 4]])
            i += 5
        else:
            i += 1
    print(indexlist)
    sec = 0
    for i in range(0, len(dataframe)):
        sec += 1
        day = 0.1 * random.randint(13, 18)
        night = 0.1 * random.randint(11, 16)
        if (sec > 3600) and (sec < 14400):
            if extend == 0:
                if (dataframe.iloc[i]['Size'] >= q[0]) and (dataframe.iloc[i]['Size'] <= q[1]):
                    dataframe.iloc[i]['Size'] = night * dataframe.iloc[i]['Size']
                    extend = random.randint(0, 3)
            else:
                if dataframe.iloc[i]['Size'] <= q[1]:
                    dataframe.iloc[i]['Size'] = night * dataframe.iloc[i]['Size']
                extend -= 1
        else:
            if extend == 0:
                if (dataframe.iloc[i]['Size'] >= q[0]) and (dataframe.iloc[i]['Size'] <= q[1]):
                    dataframe.iloc[i]['Size'] = day * dataframe.iloc[i]['Size']
                    extend = random.randint(0, 5)
            else:
                if dataframe.iloc[i]['Size'] <= q[1]:
                    dataframe.iloc[i]['Size'] = day * dataframe.iloc[i]['Size']
                extend -= 1
            boo = random.randint(0, denh)
            if boo > denl:
                ins = random.randint(0, len(insert) - 3)
                dataframe.iloc[i - 2]['Size'] = insert.iloc[ins]['Size']
                dataframe.iloc[i - 1]['Size'] = insert.iloc[ins + 1]['Size']
                dataframe.iloc[i]['Size'] = insert.iloc[ins + 2]['Size']
    dataframe.to_csv(save_path + str(j+1) + save_name, index=False, header=False)


def run(low, high, denh, denl):
    global read_path
    global save_path
    global save_name
    read_path = 'C:/penv/PrivacyGuard/data/1dayflow'
    save_path = 'C:/penv/PrivacyGuard/PG+/'
    save_name = '.csv'
    os.chdir(read_path)
    csv_name_list = os.listdir()
    for i in range(0, 20):
        df = pd.read_csv(csv_name_list[i])
        d_col = ['Time', 'Size']
        df.columns = d_col
        print(df)
        print(status(df['Size']))
        pgplus(df, low, high, denh, denl, i)


run(25, 95, 60, 59)
