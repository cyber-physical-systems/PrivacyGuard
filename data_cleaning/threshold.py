import pandas as pd
import os


def status(x):
    return pd.DataFrame([x.quantile(.05), x.quantile(.10), x.quantile(.15), x.quantile(.20), x.quantile(.25),
                     x.quantile(.30), x.quantile(.35), x.quantile(.40), x.quantile(.45), x.quantile(.50),
                     x.quantile(.55), x.quantile(.60), x.quantile(.65), x.quantile(.70), x.quantile(.75),
                     x.quantile(.80), x.quantile(.85), x.quantile(.90), x.quantile(.95), x.quantile(.96),
                     x.quantile(.97), x.quantile(.98), x.quantile(.99), x.quantile(1)],
                     index=['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65',
                            '70', '75', '80', '85', '90', '95', '96', '97', '98', '99', '100'])

read_path = 'C:/penv/IPSN/data/groundtruth/30s/'
os.chdir(read_path)
file_list = os.listdir(read_path)
for i in file_list:
    df = pd.read_csv(i)
    temp = df.columns[1]
    data = pd.DataFrame(columns=[temp])
    data[temp] = df[temp]
    data = data.drop(data[data[temp] == 0].index)
    quantile = status(data)
    print(quantile)
    # 53
    for j in range(2, 3):
        temp = df.columns[j]
        data = pd.DataFrame(columns=[temp])
        data[temp] = df[temp]
        data = data.drop(data[data[temp] == 0].index)
        q = status(data)
        quantile = pd.concat([quantile, q], axis=1)
    print(quantile)
    quantile.to_csv('C:/penv/IPSN/data/groundtruth/quantile/30s/' + i)
