import pandas as pd

ori = pd.read_csv('C:/penv/PGOnline/data/1dayflow/groundtruth.csv')
print(ori['Size'].sum()/(20000000))


t50 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/50.csv')
print(t50['Size'].sum()/(20000000))
t75 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/75.csv')
print(t75['Size'].sum()/(20000000))
t90 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/90.csv')
print(t90['Size'].sum()/(20000000))#########################################    1G
t91 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/91.csv')
print(t91['Size'].sum()/(20000000))
t92 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/92.csv')
print(t92['Size'].sum()/(20000000))
t93 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/93.csv')
print(t93['Size'].sum()/(20000000))

t94 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/94.csv')
print(t94['Size'].sum()/(20000000))
t95 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/95.csv')
print(t95['Size'].sum()/(20000000)) ########################################    3G
t96 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/96.csv')
print(t96['Size'].sum()/(20000000))
t97 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/97.csv')
print(t97['Size'].sum()/(20000000))
t98 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/98.csv')
print(t98['Size'].sum()/(20000000)) #######################################     4G
t99 = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/99.csv')
print(t99['Size'].sum()/(20000000)) #######################################     6G