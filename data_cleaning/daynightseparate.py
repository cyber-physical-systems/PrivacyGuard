import pandas as pd

read_path = 'C:/penv/PGOnline/data/unswactivity/new/'
df = pd.read_csv(read_path + 'random96.csv')
df = df[~df.Time.str.contains("14:")]
df = df[~df.Time.str.contains("15:")]
df = df[~df.Time.str.contains("16:")]
df = df[~df.Time.str.contains("17:")]
df = df[~df.Time.str.contains("18:")]
df = df[~df.Time.str.contains("19:")]
df = df[~df.Time.str.contains("20:")]
df = df[~df.Time.str.contains("21:")]
df.to_csv('C:/penv/PGOnline/data/unswactivity/new/daytime/random96_day.csv', index=False)
print(df)