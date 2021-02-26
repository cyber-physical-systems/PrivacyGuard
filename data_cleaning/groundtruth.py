import pandas as pd

gt = pd.read_csv('C:/penv/PGOnline/data/1dayflow/groundtruth.csv')
x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
     19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
gt.drop(gt.columns[x], axis=1, inplace=True)
print(gt)

test = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/2550.csv')
print(test)
j = 0
for i in range(0, 28173):
     if gt.iloc[i]['label'] == test.iloc[i]['Label']:
          j = j + 1
print(j)