from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
import pandas as pd
import csv
from scipy import stats
from statsmodels.tsa.stattools import grangercausalitytests


original = pd.read_csv('C:/penv/PGOnline/pcc/original.csv', header=None)
d_col = ['index', 'Time', 'Size']
original.columns = d_col
original = original.drop(['index'], axis=1)
pg = pd.read_csv('C:/penv/PGOnline/pcc/plus.csv', header=None)
pg.columns = d_col
pg = pg.drop(['index'], axis=1)

df_all = pd.DataFrame(original)


df_pg = pd.DataFrame(pg)

all_size = df_all.iloc[:, 1] .values
pg_size = df_pg.iloc[:, 1].values

corr , _ = pearsonr(all_size, pg_size)
corr1, _ = spearmanr(all_size, pg_size)
#
print(corr,corr1)
